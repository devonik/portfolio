---
title: "How Claude Skills + MCP Track My Capital Gains Tax"
description: I run ETFs through two brokers that don't talk to each other. Here's how a Claude skill and an MCP-backed tracker keep them reconciled against one shared tax-free allowance.
date: 2026-08-24
image: /blog/capital-gains-tracker-claude-skills-mcp-hero.png
minRead: 6
author:
  name: Niklas Grieger
  avatar:
    src: /profile.jpg
    alt: Niklas Grieger
---

I run ETF sales through Interactive Brokers and keep a savings account earning interest at Trade Republic. Both count against the same German tax-free allowance for capital gains - 1,000 EUR a year for a single filer, called the Sparerpauschbetrag. Neither broker knows the other exists.

IBKR doesn't withhold German tax at all - nothing gets deducted automatically, I have to file it myself. Trade Republic does withhold, but only against whatever allowance I've configured there specifically. If I sell an ETF on IBKR without knowing how much of the shared allowance Trade Republic has already used, I'm guessing at a number I could actually go check.

So I built a Claude skill for the sell-side decision, and connected it to a small MCP-backed tracker so both brokers show up in one combined view.

## The skill picks the position, not just the amount

The actual decision - which ETF to sell, how many shares - isn't arbitrary. I hold several overlapping global-equity ETF positions across a couple of index trackers, and selling the wrong one costs more tax than it needs to.

The skill sorts the redundant positions by **unrealized gain percentage** and sells the lowest one first - that minimizes the taxable gain per euro withdrawn, since I'm indifferent between them for diversification purposes. It also protects whichever position is the largest, treating that as the portfolio's actual core, unless the smaller positions can't cover the target amount on their own.

One rule the skill enforces without me having to remember it: Germany requires **FIFO accounting per custody account** (paragraph 20 EStG). I can't hand-pick "sell my newest, least-appreciated shares" within a single position - the broker's UI might let you select lots, but the tax treatment ignores that selection entirely. The lever that actually works is choosing between positions, not tranches within one.

A market order also means the recommended share count and the price it actually fills at are two separate numbers - close, but rarely identical. The skill logs the trade using the confirmed execution values once the order is filled, not the pre-trade estimate.

## Checking the real allowance instead of assuming one

Checking the real allowance used to mean opening both broker apps and doing the math by hand. After the skill recommends a sale, it now calls a `get_capital_gains_summary` tool against a small MCP server before it tells me anything about tax impact. That server reads a structured markdown file I keep in Google Drive - one entry per realized sale, with the gain, the 30% Teilfreistellung exemption equity funds get, and the resulting taxable base - and returns the running total against the 1,000 EUR allowance.

::capital-gains-flow-diagram
::

Logging a sale is a `create_capital_gain` call with the ticker, shares, price, and cost basis. The skill does this once IBKR confirms the order as filled, then reports the updated allowance back to me in the same reply.

## What the allowance check actually caught

I hadn't expected Trade Republic to be the problem. It used to reconcile against the allowance and remit whatever tax was owed automatically, which is part of why I'd stopped paying close attention to it after moving most trading to IBKR.

Parsing my Trade Republic transaction export showed several rows from January with an already-withheld capital gains tax and no allowance column populated at all - the allowance had been exhausted by a string of ETF sales before I'd even opened IBKR that year. Some of those rows were missing the realized-gain figure directly, likely partial-lot allocations in the export. Rather than guess, I back-calculated the taxed amount from the actual withheld tax: German capital gains tax is a flat 25% (plus a 5.5% solidarity surcharge on top of that), so dividing the withheld amount by 0.25 gives the taxable base that generated it.

Combined across both brokers, this year's taxable base already sits past the allowance. Every further realized gain gets taxed immediately in full from here - no buffer left, and I'm the one who has to set that money aside since IBKR won't do it for me.

## The pattern, not the tax specifics

None of this is tax advice, and the Trade Republic figure is a documented estimate pending the official year-end statement, not a filed number. The German tax rules aren't what's reusable here. The setup is: a skill that encodes a narrow, opinionated domain workflow (which position, how many shares, which legal rule blocks which shortcut), paired with a tool call that checks real persisted state before the skill says anything confident about the outcome.

The alternative - assuming the allowance based on whichever broker's UI I happened to have open - is exactly how I ended up past it without noticing.