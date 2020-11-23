// 主入口 单入口；
// mvc ？model：模型层  view：视图层  controller：控制层；
const Koa = require("koa");
const views = require("koa-views");
const static = require("koa-static");
const router = require("./router");
const koaBody = require("koa-body");
let app = new Koa();
app.use(views(__dirname+"/views",{extension:'pug'}));
app.use(static(__dirname+"/static"));
app.use(koaBody({
    multipart:true   //允许上传文件
}));
router(app);
app.listen(4000);


