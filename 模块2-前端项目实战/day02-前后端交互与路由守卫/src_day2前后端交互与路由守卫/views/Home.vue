<template>
  <div class="home">
    <button @click="quit">点我退出</button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'  //引入ajax库-axios
import {logout} from '../httplib'

export default {
  name: 'Home',
  components: {
  },
  setup(){
    function quit(){
      logout()
    }
    return{
      quit
    }
  }
}
</script>
