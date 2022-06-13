<template>
  <main-layout></main-layout>
</template>

<script>
import MainLayout from '../components/common/MainLayout.vue'
import {getReports} from '@/httplib'
import { ref ,onMounted,provide} from "vue";

export default {
  components:{
    MainLayout
  },
    setup(){
     // 表格展示的字段信息
    const columns =[
      {
        title: '测试计划',  //列的标题
        field: 'plan.name',      //数据的字段名
      },{
        title: '测试人员',  
        field: 'trigger.username',     
      },{
        title: '开始时间',  
        field: 'create_time',     
      },{
        title: '结束时间',  
        field: 'update_time',     
      },{
        title: '报告详情',  
        field: 'desc',     
      }
    ]
    const tableData = ref([]);
    const total = ref(0)
        //读取后台请求：
    function sync_data(page_size, page_index) {
      getReports(page_size, page_index).then(function (resp) {
        tableData.value = resp.data.retlist; //拿到后台返回的retlist
        total.value = resp.data.total
      });
    }
    //组件加载后自动更新一次数据
    onMounted(() => {
      sync_data(5, 1);
    });
    provide("total", total);
    provide("sync_data", sync_data);
    provide("columns", columns);
    provide("tableData", tableData);
  }
}
</script>