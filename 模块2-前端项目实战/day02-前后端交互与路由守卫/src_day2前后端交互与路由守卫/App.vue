<template>
  <div id="nav">
    <!-- <haiwen></haiwen> -->
    <!-- <afeng></afeng> -->
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
    <!-- <router-link to="/haiwen">Haiwen</router-link>
    <hr>
    <router-link to="/afeng">Afeng</router-link> -->
  </div>
  <!-- 组件显示的出口，根据用户输入的path显示对应的组件 -->
  <router-view/>  <!-- 负责显示路径对应的组件内容 -->

</template>

<script>
//导入组件--vue后缀名可以不写 @可以表示src所在的路径
import Haiwen from '@/views/Haiwen'
import Afeng from '@/views/Afeng'

export default {
  //注册组件
  components:{
    Haiwen,
    Afeng
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
