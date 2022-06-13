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

function common_get(url,page_size,page_index){
  return axios({
    method: 'get',
    url,
    params: {
      page_size,
      page_index
    }
  })
}

//获取用例数据
function getCases(page_size=5,page_index=1){
  return common_get('/api/cases/',page_size,page_index)
}

//获取web接口数据
function getRequest(page_size=5,page_index=1){
  return common_get('/api/requests/',page_size,page_index)
}

//获取报告数据
function getReports(page_size=5,page_index=1){
  return common_get('/api/reports/',page_size,page_index)
}


//获取测试计划
function getPlans(page_size=5,page_index=1){
  return common_get('/api/plans/',page_size,page_index)
}


//获取用例详情--根据用例ID获取单个用例数据
function caseDetail(case_id){
  return axios({
    method:'get',
    url: `/api/cases/${case_id}/`
  })
}

export {login,logout,getCases,getRequest,getReports,getPlans,caseDetail}