import axios from 'axios'  //引入ajax库-axios
import router from '../router'
import { ElMessage } from 'element-plus'  //导入消息框

axios.defaults.validateStatus=(status)=>{
  return status >=200 && status < 400 // 设置200-399之间的响应码为正常
}
axios.defaults.baseURL = 'http://120.27.146.185:8076'; //设置Host


//登录
function login(username,password){
  // 基本使用方法axios(config) config参考https://axios-http.com/zh/docs/req_config
  axios({
    method: 'post',
    url: '/api/login/',
    data:{
      username,
      password
    }
  }).then(
    //处理正常响应
    function(response){
      //成功后跳转到首页
      // console.log(response.data)
      ElMessage.success(response.data.msg)
      router.push('/')
      localStorage.setItem('islogin','yes')  //浏览器设置登录状态
    }
  ).catch(
    //处理异常响应，根据状态码，默认情况非2开头的响应码会在这里处理
    function(error){
      // console.log(error.response)
      ElMessage.error(error.response.data.error)
    }
  )
}

// 登出
function logout(){
  axios({
    method: 'get',
    url: '/api/logout/'
  }).then(()=>{
    //返回到登录
    router.push('/login')
    ElMessage.info('退出登录')
    localStorage.setItem('islogin','no')
  })
}

export {login,logout}