const Router = require('koa-router')
const router = new Router()

import demoController from '../api/demoController'

router.get('/demo', demoController.demo)

export default router
