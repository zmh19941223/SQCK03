<template>
  <main-layout :tableData="tableData" :columns="columns"></main-layout>
</template>

<script>
import MainLayout from '../components/common/MainLayout.vue'
import {getRequest} from '@/httplib'
import { ref } from 'vue';

export default {
  components:{
    MainLayout
  },
    setup(){
     // 表格展示的字段信息
    const columns =[
      {
        title: '请求方法',  //列的标题
        field: 'method',      //数据的字段名
      },{
        title: '请求路径',  
        field: 'url',     
      },{
        title: '请求体参数',  
        field: 'data',     
      },{
        title: 'URL参数',  
        field: 'params',     
      },{
        title: '请求头',  
        field: 'headers',     
      }
    ]
    const tableData = ref([])
    //读取后台请求：
    getRequest().then(
       function(resp){
         tableData.value = resp.data.retlist  //拿到后台返回的retlist
       }
     )
     return {
       columns,
       tableData,
     }
  }
}
</script>