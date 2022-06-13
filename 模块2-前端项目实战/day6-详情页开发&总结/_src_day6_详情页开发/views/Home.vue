<template>
  <layout>
    <!-- 具名插槽-v-slot:插槽名称 简写 #插槽名称 -->
    <template #header>
      <navbar></navbar>
    </template>

    <template #aside>
      <sidebar></sidebar>
    </template>

    <template #main> 
      <router-view></router-view>
    </template>
  </layout>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'  //引入ajax库-axios
import {logout} from '../httplib'
import Layout from '@/components/Layout'
import Navbar from '../components/Navbar.vue'
import Sidebar from '../components/Sidebar.vue'
export default {
  name: 'Home',
  components: {
    Layout,
    Navbar,
    Sidebar,
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
