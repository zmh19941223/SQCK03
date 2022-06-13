<template>
  <el-menu-item :index="item.path" :key="index" v-for="(item,index) in routes">
    <i :class="item.meta.icon"></i>
    <template #title>{{item.meta.title}}</template>
  </el-menu-item>
</template>

<script>
export default {
  props:{
    routes: Array  //接收父组件的传参
  }
}
</script>