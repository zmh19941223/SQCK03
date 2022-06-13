<template>
  <el-row justify="center">
    <el-col :span="24">
      <breadcrumb></breadcrumb>
    </el-col>
  </el-row>
  <el-row>
    <el-col :span="24">
      <tables></tables>
    </el-col>
    <el-col>
      <pagination></pagination>
    </el-col>
  </el-row>
</template>

<script>
import Breadcrumb from './Breadcrumb.vue'
import Tables from './Tables.vue'
import Pagination from './pagination.vue'

export default {
  components:{
    Breadcrumb,
    Tables,
    Pagination
  },
}
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>