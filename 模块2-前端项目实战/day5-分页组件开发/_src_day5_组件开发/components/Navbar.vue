
<template>
<div class="logo">
  <i class="el-icon-apple"></i>
  测试平台
</div>
<el-menu
  class="el-menu-demo"
  mode="horizontal"
  background-color="#545c64"
  text-color="#fff"
  active-text-color="#ffd04b"
>
  <el-menu-item id="avatar">
  <el-dropdown>
  <el-avatar :size="size" :src="circleUrl"></el-avatar>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item icon="el-icon-setting">设置</el-dropdown-item>
      <el-dropdown-item icon="el-icon-turn-off" divided @click="quit">退出</el-dropdown-item>
    </el-dropdown-menu>
  </template>
  </el-dropdown>  
  </el-menu-item>
</el-menu>
</template>

<script>

import {logout} from '@/httplib'
export default {
  setup() {
    function quit(){
      logout()
    }
    return {
      quit,
      size: 32,
      circleUrl:
          'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
    };
  },
};
</script>

<style>
.logo{
  width: 200px;
  background-color: rgb(255, 208, 75);
  float: left;
}
#avatar{
  width: 96px;
  text-align: center;
  float: right;
}
</style>
