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
          <el-input v-model="loginForm.username" prefix-icon="el-icon-user"></el-input>
        </el-form-item>
        <!--        密码-->
        <el-form-item prop="password">
          <el-input v-model="loginForm.password" prefix-icon="el-icon-key" type="password"></el-input>
        </el-form-item>
        <!--        按钮区域-->
        <el-form-item class="btns">
          <el-button type="primary" @click="Login">标注员登录</el-button> 
		  <el-button type="primary" @click="Loginm">管理员登录</el-button>
		  <el-button type="info" @click="Register">注册</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>


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
