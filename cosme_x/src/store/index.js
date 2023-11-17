import { createStore } from 'vuex';

export default createStore({
  state: {
    chromeVersion: null,
    chromeDriverVersion: null,
    // 你可以在这里添加其他的状态变量
  },
  mutations: {
    setChromeVersion(state, version) {
      state.chromeVersion = version;
    },
    setChromeDriverVersion(state, version) {
      state.chromeDriverVersion = version;
    },
    // 你可以在这里添加其他的 mutation 函数
  },
  actions: {
    updateChromeVersion({ commit }, version) {
      commit('setChromeVersion', version);
    },
    updateChromeDriverVersion({ commit }, version) {
      commit('setChromeDriverVersion', version);
    },
    // 你可以在这里添加其他的 action 函数
  },
  getters: {
    chromeVersion: (state) => state.chromeVersion,
    chromeDriverVersion: (state) => state.chromeDriverVersion,
    // 你可以在这里添加其他的 getter 函数
  }
});
