import Vue from 'vue'
import VueRouter from 'vue-router'
import annotation from '../components/annotation/annotation'
import document_list from '../components/document/document_list'
import index from '../components/index'
import create_label from '../components/label/create_label'
import label_list from '../components/label/label_list'
import create_project from '../components/project/create_project'
import data_export from '../components/project/data_export'
import data_import from '../components/project/data_import'
import project_base from '../components/project/project_base'
import project_status from '../components/project/project_status'
import login from "../components/login";
import user_manage from '../components/manage/user_manage'
import project_list_manager from '../components/project/project_list_manager'
import project_list from '../components/project/project_list'
import register from '../components/register'
Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    redirect:'/login'
  },
  {
    path:'/login',
    component:login
  },
  {
    path:'/register',
    component:register
  },
  // {
  //   path: "/",
  //   redirect: "/management/project_list"
  // },
  {
    path: '/management/',
    component: index,
    children: [
	  {
	    path: 'project_list_manager',
	    component: project_list_manager,
	  },
	  {
        path: 'project_list',
        component: project_list,
      },
	  
      {
        path: 'create_project',
        component: create_project
      },
      {
        path: 'label_list',
        component: label_list
      },
	  {
	    path: 'manage',
	    component: user_manage
	  },
      {
        path: 'create_label',
        component: create_label
      }
    ]
  },
  {
    path: '/project/:id/',
    component: project_base,
    children: [
      {
        path: 'labels',
        component: label_list
      },
      {
        path: 'documents',
        component: document_list
      },
      {
        path: 'status',
        component: project_status
      },
      {
        path: 'import',
        component: data_import
      },
      {
        path: 'export',
        component: data_export
      },
    ]
  },
  {
    path: '/annotation/:id/',
    component: annotation
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


// 导航守卫
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
router.beforeEach((to, from, next) => {
  if (to.path === '/login' || to.path === '/register') {
    next();
  } else {
    let token = localStorage.getItem('Authorization');

    if (token === null || token === '') {
      next('/login');
    } else {
      next();
    }
  }
});

export default router
