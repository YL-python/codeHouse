const express = require('express')
const path = require('path')
const app = express();

app.use('/static', express.static(path.join(__dirname, 'public')))

app.get("/", (req, res) => {
  res.send("hello world")
})

const post = 3000;
app.listen(post, () => {
  console.log(`express start at http://localhost:${post}`);
})