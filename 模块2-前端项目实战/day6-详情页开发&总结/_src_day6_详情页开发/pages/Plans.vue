<template>
  <main-layout></main-layout>
</template>

<script>
import MainLayout from "../components/common/MainLayout.vue";
import { getPlans } from "@/httplib";
import { ref ,onMounted,provide} from "vue";

export default {
  components: {
    MainLayout,
  },
  setup() {
    // 表格展示的字段信息
    const columns = [
      {
        title: "计划名称", //列的标题
        field: "name", //数据的字段名
      },
      {
        title: "项目",
        field: "environment.project.name",
      },
      {
        title: "测试人员",
        field: "executor.username",
      },
      {
        title: "测试环境",
        field: "environment.desc",
      },
      {
        title: "状态",
        field: "status",
      },
      {
        title: "执行次数",
        field: "exec_counts",
      },
      {
        title: "描述",
        field: "desc",
      },
    ];
    const tableData = ref([]);
    const total = ref(0)
    //读取后台请求：
    function sync_data(page_size, page_index) {
      getPlans(page_size, page_index).then(function (resp) {
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
  },
};
</script>