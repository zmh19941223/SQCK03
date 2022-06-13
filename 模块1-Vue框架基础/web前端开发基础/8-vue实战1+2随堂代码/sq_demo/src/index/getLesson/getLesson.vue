<template>
  <div>
    <div style="height: 50px">
      <el-breadcrumb separator="/" class="crumbs">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>课程查询</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="search bar6">
      <el-form :model="ruleForm" ref="ruleForm">
        <el-input
          v-model="ruleForm.pageSize"
          type="text"
          placeholder="展示多少行数据,默认为5"
        />
        <el-button type="button" @click="getLesson()"></el-button>
      </el-form>
    </div>
    <div>
      <table class="el-table el-table--fit el-table--border table-detail">
        <thead>
          <tr>
            <th width="100px">次序</th>
            <th>课程</th>
            <th>描述</th>
          </tr>
        </thead>
        <tbody>
          <!--eslint-disable-next-line-->
          <tr v-for="lesson in lessons">
            <td width="100px" v-text="lesson.id"></td>
            <td v-text="lesson.name"></td>
            <td v-text="lesson.desc"></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      lessons: [],
      ruleForm: {
        pageSize: "",
      },
    };
  },

  methods: {
    getLesson() {
      if (this.ruleForm.pageSize == "") {
        var page_size = 5;
      } else {
        var page_size = this.ruleForm.pageSize;
      }

      let data = {
        action: "list_course",
        pagenum: 1,
        pagesize: page_size,
      };

      try {
        this.$axios.get("/mgr/sq_mgr/", { params: data }).then((respone) => {
          if (respone.data.retcode === 0) {
            this.$message.success("查询成功");
            this.lessons = respone.data.retlist;
          } else {
            this.$message.error(respone.data.reason);
          }
        });
      } catch (err) {
        this.$message.error(err);
      }
    },
  },
};
</script>


<style scoped lang="scss">
@import "./style.scss";
</style>