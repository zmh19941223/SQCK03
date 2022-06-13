export default {
    data() {
        return {
            isCollapse: true,
            tabWidth: 64,
            test1: 1,
            intelval: null,
        };
    },
    methods: {
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },

        isClossTabFun() {
            clearInterval(this.intelval);
            if (!this.isCollapse) {
                this.intelval = setInterval(() => {
                    if (this.tabWidth <= 64) clearInterval(this.intelval);
                    this.tabWidth -= 8;
                }, 1);
            } else {
                this.tabWidth = 200;
            }
            this.isCollapse = !this.isCollapse;
        },

        logout() {
            this.$cookies.remove("isLogin");
            this.$message.success("已退出登录");
            this.$router.push({ path: "/" });
        },
    },
};