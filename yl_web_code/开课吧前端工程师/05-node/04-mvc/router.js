// const Router = require("koa-router");
// let router = new Router();
// router.get("/index",ctx=>{
//     ctx.body = "主页"
// });
// app.use(router.routes());
const newRouter = require("./routers/newsRouter");
const adminRouter = require("./routers/adminRouter");
module.exports = function(app){
    app.use(newRouter.routes());
    app.use(adminRouter.routes());
}