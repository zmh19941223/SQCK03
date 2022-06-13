<template>
  <div class="home">
    <el-container class="main">
      <el-aside :width="tabWidth + 'px'">
        <div>
          <div class="isClossTab" @click="isClossTabFun">
            <i
              :class="
                isCollapse ? 'el-icon-d-arrow-right' : 'el-icon-d-arrow-left'
              "
            ></i>
          </div>
          <el-menu
            :class="'menu'"
            default-active="1-4-1"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
            :collapse="isCollapse"
            background-color="#0c0d0e"
            text-color="#fff"
            active-text-color="#ffd04b"
            router
          >
            <el-menu-item index="home">
              <i class="el-icon-s-order"></i>
              <span slot="title">公告</span>
            </el-menu-item>
            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span slot="title">松勤课程</span>
              </template>
              <el-menu-item-group>
                <span slot="title">课表</span>
                <el-menu-item index="getLesson">课程查询</el-menu-item>
                <el-menu-item index="2-2">选项2</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group title="分组2">
                <el-menu-item index="2-3">选项3</el-menu-item>
              </el-menu-item-group>
              <el-submenu index="2-4">
                <span slot="title">选项4</span>
                <el-menu-item index="2-4-1">选项1</el-menu-item>
              </el-submenu>
            </el-submenu>
            <el-menu-item index="3">
              <i class="el-icon-menu"></i>
              <span slot="title">导航二</span>
            </el-menu-item>
            <el-menu-item index="4">
              <i class="el-icon-setting"></i>
              <span slot="title">导航三</span>
            </el-menu-item>
          </el-menu>
        </div>
      </el-aside>
      <el-container>
        <el-header class="main-header">
          <el-dropdown>
            <span class="el-dropdown-link">
              <img src="" alt="" />
            </span>
            <el-dropdown-menu slot="dropdown">
              <div @click="logout">
                <el-dropdown-item>退出登录</el-dropdown-item>
              </div>
            </el-dropdown-menu>
          </el-dropdown>
        </el-header>
        <el-main>
          <div></div>
          <router-view></router-view>
        </el-main>
        <el-footer class="main-footer" height="50px">
          <p>松勤教育管理系统</p>
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script src="./index-style.js"></script>

<style scoped lang='scss'>
@import "./index.scss";
</style>