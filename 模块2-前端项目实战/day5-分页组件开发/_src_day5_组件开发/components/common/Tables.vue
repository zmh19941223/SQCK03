<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column type="selection" width="55"> </el-table-column>
    
    <el-table-column :label="item.title" width="180" :key="index" v-for="(item,index) in columns">
      <template #default="scope">
        <i class="item.icon" v-if="item.icon"></i>
        <span style="margin-left: 10px">{{field_value(scope.row,item.field) }}</span>
      </template>
    </el-table-column>

    <el-table-column label="操作">
      <template #default="scope">
        <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
          >编辑</el-button
        >
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)"
          >删除</el-button
        >
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import { inject } from '@vue/runtime-core';


export default {
  props:{
    columns: Array,
    tableData: Object
  },
  setup(){
    const columns = inject('columns')
    const tableData = inject('tableData')

    function field_value(obj,fields){
      //定义一个临时对象
      let temp_obj= obj
      //根据点来分割多级字段
      for(const item of fields.split('.')){
        //通过Reflect反复获取字段
        temp_obj=Reflect.get(temp_obj,item) 
      }
      return temp_obj
    }

    function handleEdit(index, row) {
      console.log(index, row);
    }
    function handleDelete(index, row) {
      console.log(index, row);
    }
    return{
      handleEdit,
      handleDelete,
      field_value,
      columns,
      tableData
    }
  }
};
</script>

<style>
</style>
