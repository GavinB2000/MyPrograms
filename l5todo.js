// WRITE YOUR CODE HERE
const http = require('http');
const url = require('url');
var list = [];
const reqHandler = (req,res)=>{
  switch(req.method){
    case'POST':
      let item = '';
      req.setEncoding('utf-8');
      req.on('data',(chunk)=>{
        item +=chunk;
      });
      req.on('end',()=>{
        list.push(item);
        console.log(list);
        res.end('OK\n');
      });
      break;

    case'GET':
      if (list.length === 0){
        res.end("Your To-Do list is empty. Well Done!!!");
      } else {
        let list2 = list.map((element, index)=>{
          return `${index+1}) ${element}`
        }).join('\n')
        res.end(list2);
      }
      break;

    case'DELETE':
      path = url.parse(req.url).pathname;
      let i = parseInt(path.slice(1), 10);
       if (path === '/' || path === ''){
        res.end('Missing index for item to be deleted');
      } else if (isNaN(i)){
        res.end('Invalid index value')
      } else if (!list[i]){
        res.end('Item not found');
      } else{
        list.splice(i-1,1);
        res.end('OK\n');
      }
      break;

    case'PUT':
      res.end('In Put');
      break;
  }
}

const server = http.createServer(reqHandler);
server.listen(3000,()=>{
  console.log("the server is listening on port 3000")
});