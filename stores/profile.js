import axios from "~/plugins/axios";

export const state = () => ({
  data: null,
  loading: true,
});

export const mutations = {
  setData(state, data) {
    state.data = data;
  },
  setLoading(state, loading) {
    state.loading = loading;
  },
};

export const actions = {
  async get({ state, commit }) {
    console.log(state.data);
    if (state.data !== null) {
      // Prevent double load
      return state.data;
    }
    const { data } = await axios.get("/api/profile/get").finally(() => {
      commit("setLoading", false);
    });

    commit("setData", data);
  },
};
