import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);

const key ='Authorization'
const store = new Vuex.Store({
 
  state: {
    // 存储token
    Authorization: localStorage.getItem(key) ? localStorage.getItem(key) : ''
  },
 
  mutations: {
    // 修改token，并将token存入localStorage
    changeLogin (state, user) {
      state.Authorization = user.Authorization;
      localStorage.setItem(key, user.Authorization);
    },
    removeStorage(state){
     state.token =null;
     localStorage.removeItem(key);
   }
  }
});
export default store;