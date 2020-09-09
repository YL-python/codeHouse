const combineRouters = require('koa-combine-routers')

import demoRouter from './demoRouter'

export default combineRouters(demoRouter)
// combineRouters 把路由统一管理在index.js中只需要一次引入就行
