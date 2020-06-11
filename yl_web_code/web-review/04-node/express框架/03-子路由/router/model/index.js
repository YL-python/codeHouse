const express = require('express')
const path = require('path')
let router = express.Router()

router.get('/req', (req, res) => {
	console.log(req);
	res.send("req")
})

router.get('/res', (req, res) => {
	console.log(res);
	res.send("res")
})

router.get('/render', (req, res) => {
	res.render('index.html')
})

router.get('/index', (req, res) => {
	res.sendFile(__dirname + '/index.html');
})

module.exports = router;