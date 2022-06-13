module.exports = {
    devServer: {
        overlay: {
            warning: false
        },
        proxy: {
            '/api': {
                // 此处的写法，目的是为了 将 /api 替换成 http://120.55.190.222:7080/api
                target: 'http://120.55.190.222:7080/api',
                // 允许跨域
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/api': ''
                }
            }
        }
    }
}