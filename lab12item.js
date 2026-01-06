// PART 2 FOR ASSIGNMENT #6
exports.add = (db, params, cb)=>{
  let sql = `INSERT INTO items (name, price, stock, category) VALUES (?, ?, ?, ?)`;
  let values = [params.name, params.price, params.stock, params.category];
  db.query(sql, values, (err, results)=>{
    if (err)
      cb(500, 'INTERNAL SERVER ERROR', `Error: ${err.message}`);
    else 
      cb(200, 'OK', 'Item added successfully');
  });
}

exports.display = (db, cb)=>{
  let sql = `SELECT * FROM items`;
  db.query(sql, (err, results)=>{
    if (err)
      cb(500, 'INTERNAL SERVER ERROR', `Error: ${err.message}`);
    else
      cb(200, 'OK', results);
  });
}

exports.delete = (db, params, cb)=>{
  let sql = `DELETE FROM items WHERE id = ?`;
  let values = [params.id];
  db.query(sql, values, (err, results)=>{
    if (err)
     cb(500, 'INTERNAL SERVER ERROR', `Error: ${err.message}`);
    else 
      cb(200, 'OK', 'Item deleted successfully');
  });
}

exports.getItemStock = (db, params, cb)=>{
  let sql = `CALL GetItemStock(?,  @totalStock);SELECT @totalStock`;
  let values = [params.id];
  db.query(sql, values, (err, results) => {
    if (err) {
       cb(500, 'INTERNAL SERVER ERROR',`Error: ${err.message}`);
    } else {
       cb(200, 'OK', results[1][0][`@totalStock`]);
    }
});
}

exports.borrowBook = (db, params, cb) =>{
    let sql = `SELECT * FROM books where borrowed_by IS NULL and id = ?`;
    let values = [params.book_id, params.user_id];
    db.query(sql, values, (err, results)=>{
        if (err) {
            cb(`Error: ${err.message}`);
        } else if (results.user_id === params.user_id) {
            cb(`The book with the ID: ${params.book_id} is currently not available for borrowing.`)
        }
    });
}