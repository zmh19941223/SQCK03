<template>
  <div ref="bg" class="bg"></div>
</template>

<script>
import {getCurrentInstance, onMounted, onBeforeUnmount, ref,} from 'vue'
//导入canvas-nest包
import CanvasNest from 'canvas-nest.js'
//color: 线条颜色, 默认: '0,0,0' ；三个数字分别为(R,G,B)，注意用,分割
//pointColor: 交点颜色, 默认: '0,0,0' ；三个数字分别为(R,G,B)，注意用,分割
//opacity: 线条透明度（0~1）, 默认: 0.5
//count: 线条的总数量, 默认: 150
//zIndex: 背景的z-index属性，css属性用于控制所在层的位置, 默认: -1
export default {
  setup(){
    //定义粒子图的配置项
    const config={
      color: "18,156,255",   // R,G,B,数字范围是0-255
      opacity: 0.7,          // 不透明度
      count: 150,
      zIndex: -1,
      pointColor: "255,0,0"
    }
    //获取模板引用
    const bg = ref(null)

    //等组件加载完再画图
    onMounted(()=>{
      //获取当前组件的实例对象getCurrentInstance()
      
      // 初始化粒子效果对象,参数1：背景元素引用，参数2：配置项
      getCurrentInstance().cn = new CanvasNest(bg.value,config)  //为页面背景画粒子效果图
    })
    // 回收粒子效果，在组件销毁阶段
    onBeforeUnmount(()=>{
      // console.log('回收粒子效果，在组件销毁阶段')
      getCurrentInstance().cn.destroy()
    })

    return{
      bg
    }
  }
}
</script>

<style scoped>
.bg{
  width: 100vw;   
  height: 100vh;
}
</style>