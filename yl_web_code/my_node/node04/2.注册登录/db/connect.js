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