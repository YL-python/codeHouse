const express = require('express')
const app = express();

app.get("/", (req, res) => {
  res.send("hello world")
})

const post = 3000;
app.listen(post, () => {
  console.log(`express start at http://localhost:${post}`);
})