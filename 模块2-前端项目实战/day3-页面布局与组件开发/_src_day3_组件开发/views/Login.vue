
<template>
  <background></background>
  <div class="title">测试平台</div>
  <div class="login-form">
      <!-- 表单最外层el-form -->
  <el-form :model="form" label-width="60px" :rules="rules" validate-on-rule-change ref="loginForm">
    <div class="text-header">登录</div>
    <!-- 接下来 el-form需要直接嵌套el-form-item -->
    <el-form-item label="账号" prop="account">
      <!-- 一个输入框一个el-form-item -->
      <el-input
        v-model="form.account"
        placeholder="请输入用户名"
      ></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="psw">
      <el-input
        v-model="form.psw"
        placeholder="请输入密码"
        show-password
        @keyup.enter="submit"
      ></el-input>
    </el-form-item>
    <el-form-item>
      <!-- 两个按钮用1个 -->

      <!-- 加了show-password  type="password" 可以不用加了 -->
      <el-button type="primary" @click="submit">提交</el-button>
      <el-button @click="reset">重置</el-button>
    </el-form-item>
  </el-form>
  </div>

</template>

<script>
import { ref,reactive } from "vue";
import Background from '../components/Background.vue'
import {login} from '../httplib'
export default {
  components:{
    Background
  },
  setup() {
    // const account = ref("");
    // const psw = ref("");
    // 表单元素的引用
    const loginForm = ref(null)
    // 表单数据对象	
    const form= reactive({
      account: '',
      psw: ''
    })
    function submit() {
      console.log("点我提交");
      login(form.account,form.psw)
    }
    function reset() {
      console.log("点我重置-清空用户名和密码框");
      // account.value = ""; //修改ref包裹的数据通过value
      // form.account="" // reactive包裹的数据不需要value
      // form.psw = "";
      //自带的恢复初始值的方法--需要通过表单元素的引用调用该方法
      loginForm.value.resetFields() 
    }
    // 表单输入验证规则--要求必须输入
    const rules={
      // 对象的属性需要就对应表单数据对象的元素
      account:[
        {
          required: true ,//表示必须输入
          message: "请输入用户名",  //提示信息
          trigger: "blur" , //触发器  失去焦点的时候触发
        },
      ],
      psw:[
        {
          required: true ,//表示必须输入
          message: "请输入密码",  //提示信息
          trigger: "blur" , //触发器  失去焦点的时候触发
        },
      ],
    }
    return {
      // account,
      // psw,
      form,
      submit,
      reset,
      rules,
      loginForm
    };
  },
};
</script>

<style scoped>
.text-header {
  text-align: center;
  font-size: 20px;
  color: rgb(16, 16, 16);
  margin-bottom: 50px;
}
.login-form {
  position: absolute;
  width: 400px;
  height: 400px;
  top: 200px;
  right: 300px;
  border-radius: 10px;
  box-shadow: 1px 1px 5px #333;
  display: flex;
  justify-content: center;
  align-items: center;
}
.title {
  position: absolute;
  width: 400px;
  height: 80px;
  top: 50px;
  right: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 60px;
  font-family: "Microsoft Yahei";
  color: rgb(13, 104, 139);
}
.el-form-item {
  color: black;
}
</style>
