// PART 2 FOR ASSIGNMENT #6

const http = require('http');
const {URL} = require('url');
const mysql = require('mysql2');
const items = require('./lib/items.js');


function CreateConnectionObject(){
const db = mysql.createConnection({
      host: '127.0.0.1',
      user: 'root',
      port: 3306,
      database: 'ShopDB',
      multipleStatements: true
    });
  return db;
}

function closeDBConnection(db){
  db.end((err)=>{
  if(err){
    return console.log(`Error: ${err.message}`);
  }
});
}


const reqHandler = (req, res)=>{
    const db = CreateConnectionObject();
    db.connect((err)=>{
  if(err){
    return console.log(`Error: ${err.message}`);
  }
  });
  const baseUrl = `http://${req.headers.host}/`;
  const {pathname, searchParams} = new URL(req.url, baseUrl);
  const normalizedPath = pathname.split('/')[1];
  const entries = searchParams.entries();
  const params = Object.fromEntries(entries);
  const {method} = req;

  switch(method) {
    case 'POST': if (normalizedPath === 'items'){
      items.add(db, params, (statusCode, statusMessage, response)=>{
        res.writeHead(statusCode, statusMessage,{'content-type' : 'text/plain'} );
        res.end (response);
        closeDBConnection(db);
      });
    }else {
      res.writeHead(405, 'NOT ALLOWED', {'content-type' : 'text/plain'} );
      res.end ('Invalid path'); 
      closeDBConnection(db);
    }
      break;
    case 'GET': if (pathname === '/items/stock' || pathname === '/items/stock/'){
      items.getItemStock(db, params, (statusCode, statusMessage, response)=>{
        res.writeHead(statusCode, statusMessage,{'content-type' : 'application/json'} );
        if (statusCode === 200){
           response = `The stock for the item with ID: ${params.id} is ${response}`;
        }
        res.end (response);
        closeDBConnection(db);
      });
    }else {
      res.writeHead(405, 'NOT ALLOWED', {'content-type' : 'text/plain'} );
      res.end ('Invalid path'); 
      closeDBConnection(db);
    }
      break;
    case 'DELETE': if (normalizedPath === 'items'){
      items.delete(db, params, (statusCode, statusMessage, response)=>{
      res.writeHead(statusCode, statusMessage,{'content-type' : 'text/plain'} );
      res.end(response);
      closeDBConnection(db);
      });
    }else {
      res.writeHead(405, 'NOT ALLOWED', {'content-type' : 'text/plain'} );
      res.end ('Invalid path'); 
      closeDBConnection(db);
    }
      break;
    default: // Invalid operation
      res.writeHead(405, 'NOT ALLOWED', {'content-type' : 'text/plain'} );
      res.end ('Invalid method');
      closeDBConnection(db);
  }

}

const server = http.createServer(reqHandler);

server.listen(3030, ()=>{
  console.log('Sever listening on port 3030');
});





