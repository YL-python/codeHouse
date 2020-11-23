// 数据操作；
const mysql2 = require('mysql2');
const connection = mysql2.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'kkb',
});

module.exports = {
  async getData(p, perPage) {
    // [rows]
    let [rows] = await connection.promise().query(`SELECT * FROM news LIMIT ${(p - 1) * perPage},${perPage}`);
    return rows;
  },
  async getTotal() {
    let [rows] = await connection.promise().query(`SELECT * FROM news`);
    return rows.length;
  },
};
