<template>
  <main-layout :tableData="tableData" :columns="columns"></main-layout>
</template>

<script>
import MainLayout from '../components/common/MainLayout.vue'
import {getCases} from '@/httplib'
import { ref } from 'vue';

export default {
  components:{
    MainLayout
  },
    setup(){
     // 表格展示的字段信息
    const columns =[
      {
        title: '用例名称',  //列的标题
        field: 'config.name',      //数据的字段名
      },{
        title: '所属项目',  
        field: 'config.project.name',     
      },{
        title: '文件路径',  
        field: 'file_path',     
      },{
        title: '创建时间',  
        field: 'create_time', 
        icon: 'el-icon-time',  //图标信息-非必填    
      },{
        title: '更新时间',  
        field: 'update_time',
        icon: 'el-icon-time',  //图标信息-非必填     
      }
    ]
    const tableData = ref([])
    //读取后台请求：
    getCases().then(
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