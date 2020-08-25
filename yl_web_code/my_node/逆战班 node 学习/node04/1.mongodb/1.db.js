const mongoose = require('mongoose')
mongoose.connect('mongodb://nodeAdmin:root@120.26.39.212:27017/node', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})

// 数据库链接对象
var db = mongoose.connection
db.on('error', () => {
    console.log("数据库链接失败！")
});
db.once('open', () => {
    console.log('数据库连接成功！');
});

// 创建schema对象 相当于创建表头
const foodSchema = new mongoose.Schema({
    name: {
        type: String
    },
    age: {
        type: Number
    }
});
// schema对象中声明的字段就是需要的字段 多余的不被处理

// 将schema对象和数据集合进行关联
// mongoose.model(要关联的集合名,schema对象 );
// 要关联的集合名如果写的是单数形式 mongoose 自动的编程复数形式
var foodModel = mongoose.model('foods', foodSchema)

// 插入操作
// foodModel.insertMany({
//     name: '你好'
// }).then((data) => {
//     console.log('插入结果', data)
// }).catch((err) => {
//     console.log('err', err)
// })

// 查询全部操作
// foodModel.find().then((data) => {
//     console.log('查询全部结果', data)
// }).catch((err) => {
//     console.log('catch', err)
// })

// 条件查询操作
// foodModel.find(
//     { _id: '5e7f05d634677805d40a0852' }
// ).then((data) => {
//     console.log('条件查询结果', data)
// }).catch((err) => {
//     console.log('catch', err)
// })

// 删除操作
// foodModel.remove(
//     { _id: '5e7f05d634677805d40a0852' }
// ).then((data) => {
//     console.log('删除结果', data)
// }).catch((err) => {
//     console.log('catch', err)
// })

// 更新操作
foodModel.updateOne(
    { _id: '5e7f10f967656a005c11d7ac' }, 
    { $set: { name: '咒怨' } }
).then((data) => {
    console.log('更新结果', data)
}).catch((err) => {
    console.log('err', err)
})