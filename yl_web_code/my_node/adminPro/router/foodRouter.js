/*
    食品中间件
        增
        删
        改
        查  分页，模糊，分类
*/
const express = require('express')
const router = express.Router()
const path = require('path')
const fs = require('fs')
const {
    insertFood,
    findAllFood,
    delFoodById,
    updateFood,
    findFoodByPage,
    findFoodByType,
    findFoodByKw
} = require('../controls/foodControls')

/**
 * @api {post} /admin/food/add   管理平台添加菜品
 * @apiName add
 * @apiGroup Food
 *
 * @apiParam {String} name 菜品名字.
 * @apiParam {String} price 菜品价格.
 * @apiParam {String} desc 菜品的描述.
 * @apiParam {String} img 菜品的图片地址.
 * @apiParam {String} foodType 菜品的种类.
 *
 * @apiSuccess {String} err 状态码.
 * @apiSuccess {String} msg  信息提示.
 * 
 * @apiError {String} err 状态码.
 * @apiError {String} msg  信息提示.
 */
router.post('/add',(req, res) => {
    // 接收数据
    let {name,price,img,desc,foodType} = req.body 
    // 处理数据 插入数据库
    insertFood(
        {name,price,img,desc,foodType}
        ).then(()=>{
            res.send({err:0,msg:'插入成功'}
        )}).catch((err)=>{
            console.log(err)
            res.send({err:-1,msg:'插入失败请重试'})
        })
    // 返回数据
})

// 查询所有
router.post('/findAll',(req, res) => {
    findAllFood()
        .then((allFood)=>{
            res.send({err:0, msg:'查询全部成功', list:allFood});
        }).catch((err)=>{
            console.log(err);
            res.send({err:-1,msg:'查询全部失败请重试'});
        })
})

// 根据ID 删除一个
router.post('/delOne',(req, res) => {
    let { _id } = req.body
    delFoodById(_id)
        .then((allFood)=>{
            res.send({err:0, msg:'删除一个成功'});
        }).catch((err)=>{
            console.log(err);
            res.send({err:-1,msg:'删除一个失败请重试'});
        })
})

// 修改菜品
router.post('/update',(req, res) => {
    let {_id,name,price,img,desc,foodType} = req.body 
    updateFood(
        _id,
        {name,price,img,desc,foodType}
        ).then(()=>{
            res.send({err:0,msg:'修改成功'}
        )}).catch((err)=>{
            console.log(err)
            res.send({err:-1,msg:'修改失败请重试'})
        })
})

// 分页查询
router.post('/page',(req, res) => {
    let page = req.body.page || 1;
    let pageSize = req.body.pageSize || 3;
    findFoodByPage(page,pageSize)
        .then((data)=>{
            res.send({
                err:0, msg:'查询成功', 
                list:data.foodList, 
                maxPage:data.totalPage, 
                total:data.totalFood
            });
        }).catch((err)=>{
            console.log(err);
            res.send({err:-1,msg:'查询失败请重试'});
        })
})

// 分类查询
router.post('/findByType',(req, res) => {
    let {foodType} = req.body;
    findFoodByType(foodType)
        .then((list)=>{
            res.send({err:0, msg:'查询成功', list:list});
        }).catch((err)=>{
            console.log(err);
            res.send({err:-1,msg:'查询失败请重试'});
        });
})

// 模糊查询
router.post('/findByKw',(req, res) => {
    let kw = req.body.kw || '';
    findFoodByKw(kw)
        .then((list)=>{
            res.send({err:0, msg:'查询成功', list:list});
        }).catch((err)=>{
            console.log(err);
            res.send({err:-1,msg:'查询失败请重试'});
        });
})

module.exports = router;