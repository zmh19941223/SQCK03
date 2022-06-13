    //普通的变量赋值方法
    testList = [1,2,3,4]
    // let a =testList[0]
    // let b =testList[1]
    // let c =testList[2]

    //解构赋值--类似于解包的概念
    let [a,b,c]=testList

    // console.log(c)
    // 解构赋值还可以用于对象
    const obj = {
      name:'haiwen',
      age: '22',
      addr: '南京'
    }
    let {name,age}=obj  // 把对象的属性逐个提取出来
    // 如果接收的变量少于对象属性，没有任何问题
    // 如果接收的变量多余对象属性，多出来的变量为undefined
    // console.log(age)

    // 对象的常规形式
    const obj2={
      name: name,  //属性名和属性值相同时，可以触发变量的简写
      age: age
    } 
     // 对象的简写形式
    const obj3={    
      name,
      age
    }
    // console.log(obj3.age)

    // 扩展运算符
    let person = {...obj}  //取出当前对象的所有属性，复制一份给另一个对象
    obj.name='12312312'
    // console.log(person)

    // 数组的扩展运算符
    let list2 = [...testList]  //将列表元素挨个复制到list2数组
    let list3 = {...testList}  //解构成对象挨个放到list3对象中，index作为key,value就等于value
    testList.push('hello')
    // console.log(list2)
    // console.log(list3)

    // 传统函数
    const hello = function(name){
      console.log('hello',name)
    };

    //箭头函数省略funtion 可以不用return
    // 左边是入参,右边是要运算或返回的部分
    // (arg1,arg2,arg3)=>{js表达式}
    // 如果只有1个入参，可以省略大括号
    // 如果{}内只有1行可以省略{}
    const hello2 = (name)=>{
      console.log('hello',name)
    }   

    // hello('better')
    // hello2('wwww')
    // 箭头函数的返回值
    const getName = ()=>{return 'haiwen'}
    // console.log(getName())

    //箭头函数没有自己的this
    // this再面向对象语言中表示的是当前对象
    const teacher={
      teach1(){
        console.log('传统模式',this) // 当前对象
      },// 对象里面定义函数不用加function
      teach2: ()=>{
        console.log('箭头模式',this) // 顶层对象window
      } //建议调用箭头函数时，不要使用this,会出现bug
    }
    teacher.teach1()
    teacher.teach2()