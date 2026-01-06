// PART 1 FOR ASSIGNMENT 6
exports.add = (db, params, cb)=>{
  let sql = `INSERT INTO items (name, price, stock, category) VALUES (?, ?, ?, ?)`;
  let values = [params.name, params.price, params.stock, params.category];
  db.query(sql, values, (err, results)=>{
    if (err)
      cb(`Error: ${err.message}`);
    else 
      cb(results);
  });
}

exports.display = (db, cb)=>{
  let sql = `SELECT * FROM items`;
  db.query(sql, (err, results)=>{
    if (err)
      cb(`Error: ${err.message}`);
    else
      cb(results);
  });
}

exports.delete = (db, params, cb)=>{
  let sql = `DELETE FROM items WHERE id = ?`;
  let values = [params.id];
  db.query(sql, values, (err, results)=>{
    if (err)
      cb(`Error: ${err.message}`);
    else 
      cb(results);
  });
}
