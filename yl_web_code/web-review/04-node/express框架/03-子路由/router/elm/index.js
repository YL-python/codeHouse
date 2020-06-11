const express = require('express')
let router=express.Router()

// 数据
const appData = require('./data.json')
const seller = appData.seller
const goods = appData.goods
const ratings = appData.ratings

router.get('/seller', (req, res)=>{
	res.json({
		errno:0,
		data: seller
	})
})

router.get('/goods', (req, res)=>{
	res.json({
		errno:0,
		data: goods
	})
})

router.get('/ratings', (req, res)=>{
	res.json({
		errno:0,
		data: ratings
	})
})

module.exports = router;