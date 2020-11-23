const mysql2 = require('mysql2');
let data = require('./data/data.json');
const connection = mysql2.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'kkb',
});
// connection.query('SELECT * FROM news', (err, res) => {
//   if (err) {
//     return console.log(err);
//   }
//   console.log(res);
// });
// async function fn() {
//   const [rows, fields] = await connection.promise().query('SELECT * FROM news');
//   console.log(rows);
// }
// fn();

data.forEach(async (v) => {
  const [rows] = await connection
    .promise()
    .query('INSERT INTO news(title,imgUrl,`from`,newTime) VALUES (?,?,?,?)', [v.title, v.imgUrl, v.from, v.newTime]);
  console.log(rows);
});
// async function fn() {
//   const [rows] = await connection
//     .promise()
//     .query('INSERT INTO news(title,imgUrl,`from`,newTime) VALUES (?,?,?,?)', [
//       v.title,
//       'http://d.ifengimg.com/w144_h80_q70/x0.ifengimg.com/ucms/2019_43/BCC395191A1AEBFA4F7A69CC4B11D71235F4CA1A_w750_h376.jpg',
//       v.from,
//       v.newTime,
//     ]);
// }
// fn();
