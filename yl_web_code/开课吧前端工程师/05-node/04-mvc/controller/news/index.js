const newsModel = require("../../service/news");
module.exports = {
    async index(ctx) {
        let p = ctx.query.p || 1;
        let perPage = 5;
        // let newsData = 
        // ctx.body = "新闻呈现的主页111"
        let newsData = await newsModel.getData(p, perPage);
        // console.log(newsData);
        let totalCount = await newsModel.getTotal();
        // console.log(totalCount);
        let pCount = Math.ceil(totalCount / perPage);
        await ctx.render("./news/index.pug", {
            newsData,
            pCount
        });
    },
    async detail(ctx) {
        // ctx.body = "新闻详细页面";
        await ctx.render("./news/detail.pug");
    }
}