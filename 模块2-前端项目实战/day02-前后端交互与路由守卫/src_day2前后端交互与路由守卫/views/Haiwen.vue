<template>
  <div class="hai">
      <h3>hello {{yourname}}</h3>
  </div>
  
</template>

<script>
export default {
  //组件的名称
  name: 'Haiwen',
  //组合式API
  setup(){
    let yourname='海文'

    return{
      yourname
    }
  }
}
</script>

<style scoped>
.hai{
  width: 800px;
  height: 800px;
  background:antiquewhite;
}
</style>