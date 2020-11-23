const Router = require("koa-router");
const newsController = require("../controller/news");
let router = new Router({
    prefix:"/news"
});
// newsController.index == (ctx){
//     ctx.body = "新闻呈现的主页111"
// }
router.get("/",ctx=>{ctx.redirect("/news/index")});
router.get("/index",newsController.index);
router.get("/detail",newsController.detail);
module.exports = router;