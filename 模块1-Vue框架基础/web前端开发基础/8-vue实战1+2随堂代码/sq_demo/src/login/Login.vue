<template>
  <div>
    <vue-particles
      color="#556"
      :particleOpacity="0.7"
      :particlesNumber="150"
      shapeType="polygon"
      :particleSize="2"
      linesColor="#555"
      :linesWidth="1"
      :lineLinked="true"
      :lineOpacity="0.4"
      :linesDistance="150"
      :moveSpeed="2"
      :hoverEffect="true"
      hoverMode="grab"
      :clickEffect="false"
      clickMode="push"
      class="lizi"
    />

    <div id="login-container">
      <div style="text-align: center; height: 50px">登录</div>
      <!-- 使用Element-UI创建组件-->
      <el-form
        :model="ruleForm"
        status-icon
        :rules="rules"
        ref="ruleForm"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item label="账号" prop="user">
          <el-input
            type="text"
            v-model="ruleForm.user"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="pass">
          <el-input
            type="password"
            v-model="ruleForm.pass"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm()">提交</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<style lang="scss">
body {
  width: 100%;
  background-color: rgb(239, 239, 239);
}
.lizi {
  position: fixed;
  top: 0;
  width: 100%;
}
</style>

<script>
import qs from "qs";
//import Cookies from "js-cookie";

export default {
  name: "login",
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入账户"));
      } else {
        if (this.ruleForm.pass !== "") {
          this.$refs.ruleForm.validateField("pass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        user: "auto",
        pass: "sdfsdfsdf",
      },
      rules: {
        user: [{ validator: validatePass, trigger: "blur" }],
        pass: [{ validator: validatePass2, trigger: "blur" }],
      },
      isLogin: false,
    };
  },
  methods: {
    submitForm() {
      let data = qs.stringify({
        username: this.ruleForm.user,
        password: this.ruleForm.pass,
      });

      this.$axios.post("/mgr/loginReq", data).then((respone) => {
        if (respone.data.retcode === 0) {
          this.$message.success("登录成功");
          this.$cookies.set("isLogin", true);
          this.$router.push({ path: "/home" });
        } else {
          // this.$message.error("登录失败");
          this.$message.error(respone.data.reason);
        }
      });
    },

    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>

<style scoped>
#login-container {
  width: 400px;
  height: 290px;
  background: #e5e9f2;
  position: absolute;
  left: 50%;
  top: 50%;
  margin-left: -220px;
  margin-top: -170px;
  border-radius: 5px;
  padding-top: 40px;
  padding-right: 40px;
}
</style>