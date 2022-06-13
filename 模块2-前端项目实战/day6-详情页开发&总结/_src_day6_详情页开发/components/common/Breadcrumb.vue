
<template>
  <el-breadcrumb separator-class="el-icon-arrow-right">
    <el-breadcrumb-item
      :key="index"
      v-for="(route, index) in currentRouteList"
      :to="{ path: route.path }"
      >{{ route.meta.title }}</el-breadcrumb-item
    >
    <!-- <el-breadcrumb-item><a href="/">活动管理</a></el-breadcrumb-item> -->
  </el-breadcrumb>
</template>

<script>
import { useRoute } from "vue-router";
export default {
  setup() {
    //获取当前路由信息
    const route = useRoute();
    const currentRouteList = route.matched; //当前路由列表(包括所有上级路由)
    return {
      currentRouteList,
    };
  },
};
</script>

<style>
</style>
