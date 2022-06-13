<template>
  <el-container>
    <el-header>
      <!-- 这里插入顶栏 -->
      <slot name="header"></slot>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <!-- 这里插入测边栏 -->
        <slot name="aside"></slot>
      </el-aside>
      <el-main>
        <!-- 这里插入主页面区域 -->
        <slot name="main"></slot>
      </el-main>
    </el-container>
  </el-container>
</template>

<style>
  body{
    margin: 0px !important;
  }
  .el-header{
    padding:0px !important;
  }
  .el-header,
  .el-footer {
    background-color: #b3c0d1;
    color: var(--el-text-color-primary);
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #e9eef3;
    color: var(--el-text-color-primary);
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #e9eef3;
    color: var(--el-text-color-primary);
    text-align: center;
    line-height: 160px;
  }

  body > .el-container {
    margin-bottom: 40px;
  }


</style>