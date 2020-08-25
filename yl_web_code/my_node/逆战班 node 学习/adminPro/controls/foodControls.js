// 数据库相关代码抽离

const foodModel = require('../db/model/foodModel')

// 插入
let insertFood = async (obj) => {
    let result = await foodModel.insertMany(obj);
    return result;
    // return 的值会传给 then方法做参数，出错会把错误对象传给catch方法做参数
}

// 查询全部
let findAllFood = async ()=>{
    let result = await foodModel.find();
    return result;
}

// 根据id查询
let findById = async (_id)=>{
    let result = await foodModel.find({_id});
    return result;
}

// 根据ID删除
let delFoodById = async (_id)=>{
    let result = await foodModel.deleteOne({_id:_id});
    return result;
}

// 修改
let updateFood = async (_id, updateInfo) => {
    let result = await foodModel.updateOne({_id:_id},updateInfo);
    return result;
}

// 分页查询
let findFoodByPage = async (page, pageSize) => {
    let all = await foodModel.find();
    let totalFood = all.length;
    // let totalPage = totalFood % pageSize==0 ?  Math.floor(totalFood / pageSize) : Math.ceil(totalFood / pageSize);
    let totalPage = Math.ceil(totalFood / pageSize);
    let foodList = await foodModel.find().skip(Number((page -1)*pageSize)).limit(Number(pageSize));
    return {foodList,totalFood,totalPage};
}

// 分类查询
let findFoodByType = async (foodType)=>{
    let result = await foodModel.find({foodType});
    return result;
}   

// 模糊查询
let findFoodByKw = async (kw,page, pageSize)=>{
    // 通过正则表达式匹配
    let re = new RegExp(kw)
    let foodList = await foodModel.find({
        $or:[
            {price:{$regex:re}},
            {name:{$regex:re}},
            {img:{$regex:re}},
            {foodType:{$regex:re}},
            {desc:{$regex:re}}
        ]
    }).skip(Number((page -1)*pageSize)).limit(Number(pageSize));
    let totalFood = foodList.length;
    let totalPage = Math.ceil(totalFood / pageSize);
    return {foodList,totalFood,totalPage};
}

module.exports = {
    insertFood,
    findAllFood,
    delFoodById,
    updateFood,
    findFoodByPage,
    findFoodByType,
    findFoodByKw,
    findById
}