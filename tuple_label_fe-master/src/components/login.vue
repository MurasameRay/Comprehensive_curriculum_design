<template>
  <div class="login_container" >
    <div class="login_box" onmouseover="this.style.opacity=0.9" onmouseout="this.style.opacity=0.5">
      <!-- 头像区域 -->
      <div class="avatar_box">
        <img src="../assets/images/logo.png" alt="" >
      </div>
      <!-- 登录表单区域 -->
      <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="0px" class="login_form">
        <!--        用户名-->
        <el-form-item prop="username">
          <el-input placeholder="请输入用户名" v-model="loginForm.username" prefix-icon="el-icon-user"></el-input>
        </el-form-item>
        <!--        密码-->
        <el-form-item prop="password">
          <el-input placeholder="请输入密码" v-model="loginForm.password" prefix-icon="el-icon-key" type="password"></el-input>
        </el-form-item>
        <!--        按钮区域-->
        <el-form-item class="btns">
          <el-button type="primary" @click="Login">标注员登录</el-button> 
		  <el-button type="primary" @click="Login_admin">管理员登录</el-button>
		  <el-button type="info" @click="Register">注册</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';
  export default {
    data() {
      return {
        // 数据绑定对象
        loginForm: {
          username: 'zht',
          password: '123456',
          admin_id: '0'
        },
        // 验证规则对象
        loginFormRules: {
          //验证用户
          username: [
            {required: true, message: '请输入用户名', trigger: 'blur'},
            {min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '请输入登录密码', trigger: 'blur'},
            {min: 3, max: 15, message: '长度在 3 到 15 个字符', trigger: 'blur'}
          ],
        }
      }
    },
    methods: {
      ...mapMutations(['changeLogin','removeStorage']),
      Login: function () {
        // 预验证
        this.$refs.loginFormRef.validate(async valid => {
          //未验证通过则直接return
          if (!valid) return;
          //不加await的化不会打印出数据，await只能用于async修饰的函数   //this.loginForm
          const response = await this.$http.post('/login/', this.loginForm).catch(() => this.$message.error("登录失败,请联系Tel:"))
          // {data:res}解构，将得到的返回值的data解构为res
          console.log(response.data)
          // console.log(res.meta.statusText)
          //从res的元数据中得到返回状态
          if (response.status !== 200) {return;}
          if (response.data.token) {
            this.userToken = 'Ray ' + response.data.token;
            // token = localStorage.getItem('Authorization');
            // 将用户token保存到vuex中
            localStorage.setItem('username', this.loginForm.username);
            this.changeLogin({Authorization: this.userToken});
            this.$router.push({
              path:'/management/project_list',
                params:{
                  username:'zht'
                }
              });
          }
          else this.removeStorage();
          if (response.data.error) {return this.$message.error(response.data.error)}
        });
      },
	  
	  Login_admin:function() {
        // 预验证
        this.$refs.loginFormRef.validate(async valid => {
          //未验证通过则直接return
          if (!valid) return;
          //不加await的化不会打印出数据，await只能用于async修饰的函数   //this.loginForm
          const response = await this.$http.post('/login_admin/', this.loginForm).catch(() => this.$message.error("登录失败,请联系Tel:"))
          // {data:res}解构，将得到的返回值的data解构为res
          console.log(response.data)
          // console.log(res.meta.statusText)
          //从res的元数据中得到返回状态
          if (response.status !== 200) {return;}
          search_adminID();
          if (response.data.token) {
            this.userToken = 'Ray ' + response.data.token;
            // token = localStorage.getItem('Authorization');
            // 将用户token保存到vuex中
            this.changeLogin({Authorization: this.userToken});
            localStorage.setItem('username', this.loginForm.username);
            this.$router.push({
              path:'/management/project_list_manager',
                params:{
                  username:'zht'
                }
              });
          }
          else this.removeStorage();
          if (response.data.error) {return this.$message.error(response.data.error)}
        });
      },
      search_adminID() {
      axios
        .get(`${urlSetting.admin_url}?username=${localStorage.getItem('username')}`)
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            localStorage.setItem('admin_id', response.data.results[0].id);
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        });
    },
      //重置登录表单
      // resetLoginForm() {
      //   // console.log(this)
      //   // ui框架自带的form表单方法
      //   this.$refs.loginFormRef.resetFields();
      // },
     Register:function(){
              // 预验证 
                  this.$router.push({
                    path:'/register',
                  });
                }
            
    }
  }

</script>
<!--加上scoped是将样式应用于此组件，不加是全局-->
<style lang="less" scoped>

  .login_container {
    background-color: rgba(21, 35, 242, 0.25);
    background-image:url(../assets/images/background_img.jpg);
    height: 100%;
  }

  .login_box {
    width: 450px;
    height: 300px;
    background-color: white;
    border-radius: 3px;
    /*容器内居中*/
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.5;
    transition: opacity 1s;
    .avatar_box {
      height: 130px;
      width: 130px;
      border: 1px solid #eee;
      border-radius: 50%;
      padding: 10px;
      /*边框阴影*/
      box-shadow: 0 0 10px #ddd;
      position: absolute;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: #fff;

      img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background-color: #eee;

      }
    }

    .login_form {
      position: absolute;
      bottom: 0;
      width: 100%;
      padding: 0 20px;
      box-sizing: border-box;
    }

    .btns {
      display: flex;
      justify-content: flex-end;
    }
  }
</style>
