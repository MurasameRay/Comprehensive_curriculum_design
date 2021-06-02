<template>
  <div class="layout">
    <Layout>
      <Header>
        <Menu
          mode="horizontal"
          theme="dark"
          active-name="1"
        >
          <div class="layout-logo">
            <img
              type="image/png"
              src="../assets/images/head.png"
              width="50"
              height="40"
            >
          </div>


             <el-breadcrumb-item>
               <div class="layout-nav">
                 用户名：
                 {{showUserName}}
               </div>
            </el-breadcrumb-item>

        </Menu>
      </Header>
      <Layout>
        <!-- <Sider
          hide-trigger
          :style="{background: '#fff'}"
        >
          <Menu width="auto">
            <MenuGroup title="项目管理">
              <MenuItem
                to="/management/project_list"
                name="1"
              >
              <Icon type="md-heart" />
              Project List
              </MenuItem>
            </MenuGroup>
            <MenuGroup title="标注管理">
              <MenuItem
                to="/annotation"
                name="6"
              >
              <Icon type="md-leaf" />
              Annotation
              </MenuItem>
            </MenuGroup>
          </Menu>
        </Sider> -->
        <Layout :style="{padding: '0 24px 24px'}">
          <!-- <Breadcrumb :style="{margin: '24px 0'}">
                        <BreadcrumbItem>Home</BreadcrumbItem>
                        <BreadcrumbItem>Components</BreadcrumbItem>
                        <BreadcrumbItem>Layout</BreadcrumbItem>
          </Breadcrumb>-->
          <Content :style="{padding: '24px', minHeight: '280px', background: '#fff'}">
            <router-view></router-view>
          </Content>
        </Layout>
      </Layout>
    </Layout>
  </div>
</template>
<script>
  const axios = require("axios");
  import urlSetting from "../setting";

  export default {
  data() {
    return {
      showEditModal: false,
      showAddModal: false,
      queryData: {},
      columns1: [
        {
          title: "ID",
          key: "id",
          _display: false
        },
        {
          title: "Username",
          key: "username"
        },
        {
          title: "Project Id",
          key: "project_id"
        },
        {
          title: "Name",
          key: "name"
        },
        {
          title: "Password",
          key: "password"
        },
      ],
      data1: [],
      editData: {
        id: "",
        username: "",
        name:"",
        password:"",
        project_id: "",
      },
      createProjectOption: {
        isShow: false
      }
    };
  },
  computed:{
    showUserName(){
        return localStorage.getItem('username');
    }
  },
  mounted() {
    this.search();
  },
  methods: {  
    search() {
      axios
        .get(urlSetting.username_url)
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            this.data1 = response.data.results;
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        });
    },
    findUser() {
      axios
        .get(urlSetting.username_url+"zht"+'/')
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            this.data1 = response.data.results;
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        });
    },
  },
};
</script>



<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
}
.layout-logo {
  width: 100px;
  height: 30px;
  border-radius: 3px;
  float: left;
  position: relative;
  top: 15px;
  left: 20px;
}
.layout-nav {
  float: right;
  padding-left: 800px;
  width: 1000px;
  margin: 0 auto;
  margin-right: 20px;
  color:red;
  font-size: 20px;
  font-family: FangSong;
  text-shadow: 2px 2px 2px grey;
}
</style>
