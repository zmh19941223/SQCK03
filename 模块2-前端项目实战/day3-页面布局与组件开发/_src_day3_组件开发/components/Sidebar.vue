
<template>
  <el-menu
    router
    :uniqueOpened="true"
    :collapse="iscollapse"
    default-active="2"
    class="sidebar"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
  >
      <el-menu-item index="/cases">
        <i class="el-icon-s-order"></i>
        <template #title>测试用例</template>
      </el-menu-item>
      <el-menu-item index="/request">
        <i class="el-icon-s-promotion"></i>
        <template #title>web接口</template>
      </el-menu-item>
      <el-menu-item index="/plans">
        <i class="el-icon-s-flag"></i>
        <template #title>测试计划</template>
      </el-menu-item>
      <el-menu-item index="/reports">
        <i class="el-icon-s-data"></i>
        <template #title>测试报告</template>
      </el-menu-item>
      <el-menu-item @click="switch_side">
        <i class="el-icon-arrow-left" v-if="iscollapse===false"></i>
        <i class="el-icon-arrow-right" v-else></i>
      </el-menu-item>
  </el-menu>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const iscollapse=ref(false) // 测边栏显示状态 收起/展开
    function switch_side(){
      iscollapse.value = !iscollapse.value
    }
    return {
      iscollapse,
      switch_side
    };
  },
};
</script>

<style>
.sidebar{
  /* 撑起菜单栏高度 */
  height: 100vh;
}
</style>
