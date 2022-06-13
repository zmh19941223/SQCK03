
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
      <sidebar-item :routes="route_list"></sidebar-item>
      <el-menu-item @click="switch_side">
        <i class="el-icon-arrow-left" v-if="iscollapse===false"></i>
        <i class="el-icon-arrow-right" v-else></i>
      </el-menu-item>
  </el-menu>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import SidebarItem from './common/SidebarItem.vue'
export default {
  components:{
    SidebarItem
  },
  setup() {
    //获取路由信息
    const router = useRouter() //路由器
    const route_list = router.options.routes[0].children //从home获取二级路由列表
    const iscollapse=ref(false) // 测边栏显示状态 收起/展开
    function switch_side(){
      iscollapse.value = !iscollapse.value
    }
    return {
      iscollapse,
      switch_side,
      route_list
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
