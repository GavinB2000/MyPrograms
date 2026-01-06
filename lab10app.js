// PART 1 for assignment 6
const mysql = require('mysql2');
const items = require('./lib/items.js');


// Check the number of arguments
if (process.argv.length < 3){
  console.log('Error: Number of arguments are less than 4');
  return;
}
if (process.argv.length !== 4 && process.argv[2] === "DISPLAY") {
    console.log("Error: DISPLAY operation requires 4 arguments");
    return;
}

if ((process.argv[2] === "ADD" || process.argv[2] === "DELETE") && process.argv.length !== 5) {
    console.log("Error: ADD and DELETE operations require 5 arguments");
    return;
}

const operation = process.argv[2];
const tableName = process.argv[3];
const params = JSON.parse(process.argv[4] || '{}');


const db = mysql.createConnection({
  host: '127.0.0.1',
  user: 'root',
  port: 3306,
  database: 'ShopDB'
});

db.connect((err)=>{
  if(err){
    return console.log(`Error: ${err.message}`);
  }
  console.log(`Connection successful!!!`);
});

switch(operation) {
    case 'ADD': if (tableName === 'items'){
      items.add(db, params, (results)=>{
        console.log(results);
      });
    }else {
      console.log('Invalid table name');
    }
      break;
    case 'DISPLAY': if (tableName === 'items'){
      items.display(db, (results)=>{
        console.log(results);
      });
    }else {
      console.log('Invalid table name');
    }
      break;
    case 'DELETE': if (tableName === 'items'){
      items.delete(db, params, (results)=>{
        console.log(results);
      });
    }else {
      console.log('Invalid table name');
    }
      break;
    default: // Invalid operation
      console.log('Unknown command. Try "DISPLAY", "ADD", or "DELETE".');
  }


db.end((err)=>{
  if(err){
    return console.log(`Error: ${err.message}`);
  }
  console.log(`Closing Connection ...`);
});


