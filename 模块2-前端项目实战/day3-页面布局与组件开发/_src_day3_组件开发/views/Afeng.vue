<template>
  <h3 class="feng">hello {{yourname}}</h3>
</template>

<script>
export default {
  //组件的名称
  name: 'Afeng',
  //组合式API
  setup(){
    let yourname='afeng'

    return{
      yourname
    }
  }
}
</script>


<style scoped>
.feng{
  width: 800px;
  height: 800px;
  background:blue;
}
</style>