<template>
  <main-layout v-if="$route.path==='/cases'"></main-layout>
  <router-view v-else></router-view>
</template>

<script>
import MainLayout from "../components/common/MainLayout.vue";
import { getCases } from "@/httplib";
import { onMounted, provide, ref } from "vue";

export default {
  components: {
    MainLayout,
  },
  setup() {
    // 表格展示的字段信息
    const columns = [
      {
        title: "用例名称", //列的标题
        field: "config.name", //数据的字段名
      },
      {
        title: "所属项目",
        field: "config.project.name",
      },
      {
        title: "文件路径",
        field: "file_path",
      },
      {
        title: "创建时间",
        field: "create_time",
        icon: "el-icon-time", //图标信息-非必填
      },
      {
        title: "更新时间",
        field: "update_time",
        icon: "el-icon-time", //图标信息-非必填
      },
    ];
    const tableData = ref([]);
    const total = ref(0);
    //读取后台请求：
    function sync_data(page_size,page_index){
      getCases(page_size,page_index).then(function (resp) {
        tableData.value = resp.data.retlist; //拿到后台返回的retlist
        total.value = resp.data.total; //拿到总条数信息用于分页
      });
    }
    //组件加载后自动更新一次数据
    onMounted(()=>{
      sync_data(5,1)
    })
    //提供下层组件需要的数据，参数1：数据名称，参数2：数据内容
    provide('total',total)
    provide('sync_data',sync_data)
    provide('columns',columns)
    provide('tableData',tableData)
  },
};
</script>