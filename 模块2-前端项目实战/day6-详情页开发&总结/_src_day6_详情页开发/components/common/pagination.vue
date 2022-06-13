<template>
  <el-pagination
    background
    layout="sizes, prev, pager, next"
    :total="total"
    :page-size="page_size"
    :page-sizes="[5, 10, 20]"
    v-model:currentPage="page_index"
    @size-change="handleSizeChange"
    @current-change="handleCurrentChange"
  >
  </el-pagination>
</template>

<script>
import { ref } from "@vue/reactivity";
import { inject } from '@vue/runtime-core';
export default {
  setup() {
    const page_index = ref(1); //当前页码
    const page_size = ref(5)   //当前页显示条数
    const total = inject('total')
    const sync_data = inject('sync_data')

    //处理页面条数更改
    function handleSizeChange(size){
      // console.log('page_size',size);
      page_size.value=size //更新当前页显示条数
      sync_data(page_size.value,page_index.value)
    }
    //处理页码更新
    function handleCurrentChange(index){
      // console.log('page_index',index);
      page_index.value=index
      sync_data(page_size.value,page_index.value)
    }
    return {
      page_index,
      page_size,
      handleSizeChange,
      handleCurrentChange,
      total
    };
  },
};
</script>