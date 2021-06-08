import iView from 'iview';
import 'iview/dist/styles/iview.css';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
//导入全局样式表
import './assets/css/globe.css'
import store from './store'
Vue.config.productionTip = false
Vue.use(iView);
Vue.use(require('vue-shortkey'));

Vue.use(ElementUI)
Vue.config.productionTip = false

//配置axios全局使用
import axios from 'axios'
// axios.defaults.baseURL='http://0.0.0.0:8000/api/'
// 将vue的原型http对象设置未axios，以后用这个原型就可以直接使用
let protocol = window.location.protocol; //协议
   let host = window.location.host; //主机
   let reg = /^localhost+/;
   if(reg.test(host)) {
      //若本地项目调试使用
       axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';
   } else {
       //动态请求地址             协议               主机
       axios.defaults.baseURL = protocol + "//" + host  +":8000/api/";
   }
Vue.prototype.$http = axios

new Vue({
  router,
    store,
  render: h => h(App)
}).$mount('#app')

// 添加请求拦截器，在请求头中加token
axios.interceptors.request.use(
  config => {
    if (localStorage.getItem('Authorization')) {
      config.headers.Authorization = localStorage.getItem('Authorization');
    }

    return config;
  },
  error => {
    return Promise.reject(error);
  });


//http reponse拦截器

axios.interceptors.response.use(
  response =>{
    return response;
  },
  error=>{
    if(error.response){
      switch(error.response.status){
        case 201:
          localStorage.removeItem('Authorization');
     /*     router.push('/views/login');*/
          router.replace({
            path: '/login',
            query: {redirect: router.currentRoute.fullPath}//登录成功后跳入浏览的当前页面
          })
      }
    }

  }
)
