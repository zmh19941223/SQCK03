<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column type="selection" width="55"> </el-table-column>
    
    <el-table-column :label="item.title" width="180" :key="index" v-for="(item,index) in columns">
      <template #default="scope">
        <i class="item.icon" v-if="item.icon"></i>
        <span style="margin-left: 10px">{{ scope.row[item.field] }}</span>
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


export default {
  props:{
    columns: Array,
    tableData: Object
  },
  setup(){

    function handleEdit(index, row) {
      console.log(index, row);
    }
    function handleDelete(index, row) {
      console.log(index, row);
    }
    return{
      handleEdit,
      handleDelete
    }
  }
};
</script>

<style>
</style>
