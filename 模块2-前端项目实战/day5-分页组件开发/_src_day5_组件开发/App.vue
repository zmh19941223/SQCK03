<template>
  <!-- 组件显示的出口，根据用户输入的path显示对应的组件 -->
   <!-- 负责显示路径对应的组件内容 -->
  <router-view/> 
</template>

<script>
//导入组件--vue后缀名可以不写 @可以表示src所在的路径
import Haiwen from '@/views/Haiwen'
import Afeng from '@/views/Afeng'


export default {
  //注册组件
  components:{
    Haiwen,
    Afeng,
  }
}
</script>


