//source like string

let list = '["www.globo.com","www.youtube.com","www.facebook.com","www.yahoo.com","br-playground.digitalhouse.com"]'

//### USING callback ###
//1st function: function to add http
let addHttp = (url) => 'http://'+url;

//2nd function: using function addHttp to add http 
let joinUrl = (list, func) => {
  let endList = [];
  for (i=0; i<list.length;i++){
    endList.push(func(list[i]))
  }
  return endList
}


//showing list before convertion
console.log(`\nNow list is a string:\n${list}\nThe type of list is: ${typeof(list)}`)

//convert list to array
list = JSON.parse(list)

//showing after convertion
console.log(`\nNow list is an array:\n${list}\nThe type of list is: ${typeof(list)}\nThe zero element is ${list[0]} and the last one is ${list[list.length-1]}`)

//add http to urls
list = joinUrl(list,addHttp)

//showing list after added http
console.log(`\nNow in the array list there are http:\n${list}`)

//convertion back to string
list = JSON.stringify(list)

//showing list after convertion to string
console.log(`\nNow list is a string:\n${list}\nThe type of list is: ${typeof(list)}`)



//#### Without using callback - How to get the same solution in less lines ####
let anotherJoin = (arr) => {
  let endList = []
  for (i=0; i<arr.length; i++){
    endList.push('http://'+
    arr[i])  
  }
  return endList
}

console.log(JSON.stringify(anotherJoin(JSON.parse(list))))


//-------------------- New callback
let hello = () => console.log("Hello");
setTimeout(hello,5000)
