---
title: "Exploring AI-Driven Web Crawling: A Beginner’s Journey"
description: Follow my hands-on journey as I dive into the world of AI-powered web crawling. From understanding core concepts to testing real tools and building small experiments, this blog documents my discoveries, challenges, and insights while exploring how artificial intelligence is reshaping how we gather and analyze information online.
date: 2025-11-14
image: /blog/explore-ai-crawling/hero.png
minRead: 3
author:
  name: Niklas Grieger
  avatar:
    src: /profile.jpg
    alt: Niklas Grieger
---

## My journey

I'm building a plattform for the bitcoin community. On feature of this will price comparison app for bitcoin related products. To show all the products I need to crawl many different e-commerce websites. \
I know traditional crawling and that you have to define the css schema of the website so the crawler can find the article information. A big disadvantage of this the structure of the website can change, you have to recognize the change and change the css schema.
I started researching about AI web crawling and found ton's of tools to use. I can be overwhelming and it's not easy to find a solution that fits my needs.

## Challenges

### I will have 1000+ different websites with bitcoin related products that I wanna crawl. Each website has 10k products or more

Problem 1: I cannot crawl all of these products and save them, that would be insane to save in a database\
Problem 2: All of these websites are having different designs\
Problem 3: These website are not all e-commerce pages, they can also be e-sim provider, domain provider etc.\
\
Idea for Problem 1: I will scrape only the search page of each website e.g https://webshop.de/search?q=product1 so I will have a smaller playload to save.\
Idea for Problem 2: I will try to find a good AI toll and define a prompt to find the correct data on each website. As alternative I will use the CSSShema extraction from Crawl4AI.\
No Idea for Problem 3: This will be challenging to crawl with AI cause the parameter are totally different

### Exploring AI web crawlers

## Thunderbolt

> <https://thunderbit.com/>

This was the first tool I found. I installed their Chrome Extention and tried it in one e-commerce shop search page.

<div class="flex items-center flex-col sm:flex-row">
  <img alt="Thundebit AI Crawler" src="/blog/explore-ai-crawling/thunderbit.png" class="object-contain" width="250"/>
  <span>It worked great! I defined the fields and one prompt per field. No css shema required. I could even define that the crawler does paging.</span>
</div>

There is just one downside: **Thunderbit has no API** and it's just usable as a Chrome extention for manual crawling and export.
In my case I need to dynamically crawl different websites in different structure. So this tool is **not** working for my case.\
Anyway I can recommend this tool if you just have one or some websites to crawl and are fine with the manual effort to export the result to .csv or other formats.

## BrowserAI

> <https://www.browse.ai/>

I tried this tool by settings up a robot on their website. It extracted the data as I wanted **but** some information as the price were missing.
<img alt="Browser AI missing data" src="/blog/explore-ai-crawling/browser-ai-first-robot-missing-data.png" class="object-contain" width="250"/>

Additionally the pricing doesn't make sense for my case since I have 1000+ different websites.
<img alt="Browser AI pricing" src="browser-ai-pricing.png" class="object-contain" width="250"/>

## Firecrawl

This tool is promising since it is developer friendly by offering a Rest API with crawling and scraping functionalities.
On their website I could try the API's but turns out the data was often not correct or missing. The missing data comes probably from lazy loading of the website, but Firecrawl does not offer a good handling of lazy loading yet.\
\
I tried their Rest API with postman but I had missing data, the task was running very long and occurs to timeouts, and all my credits were accidently used by one API call.\
\
I think firecrawl is on a good way, is highly customizable, and offer llm extraction by API call. But the incorrect data and lazy loading handling is **not** good enough for my case.\
\
Additionally I had the problem to scrape with an defined json array. When you define only one json object it works fine in the playground - see the video.\
May I give it another try in the future
<video height="240" controls>
  <source src="/blog/explore-ai-crawling/firecrawl-playground.mp4" type="video/mp4">
</video>

## Crawl4AI - my solution for now

TBD...