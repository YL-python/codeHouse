const {
  src,
  dest,
  series,
  watch
} = require("gulp")
// gulp-uglify => plugins.uglify  === require("gulp-uglify")
const del = require("del")
const plugins = require("gulp-load-plugins")()
const browserSync = require("browser-sync").create()
const reload = browserSync.reload

const onError = (err) => {
  console.log(err);
}

// 压缩和uglify JS
function js(cb) {
  src("js/*.js")
    .pipe(plugins.plumber({
      errorHandler: onError
    }))
    .pipe(plugins.uglify())
    .pipe(plugins.rename({
      extname: '.min.js'
    }))
    .pipe(dest('./dist/js'))
    .pipe(reload({
      stream: true
    }))
  cb() // 一个 回调函数 给 gulp自己处理不然会抛出一个异常
}

// 对 scss/less编译，压缩，输出scc文件
function css(cb) {
  src("css/*.scss")
    .pipe(plugins.plumber({
      errorHandler: onError
    }))
    .pipe(plugins.sass({
      outputStyle: "compressed"
    }))
    .pipe(plugins.autoprefixer({
      cascade: false,
      remove: false
    }))
    .pipe(dest('./dist/css'))
    .pipe(reload({
      stream: true
    }))
  cb()
}

// 处理 html 的变化
function html(cb) {
  src("./*.html")
    .pipe(plugins.plumber({
      errorHandler: onError
    }))
    .pipe(dest('./dist/'))
    .pipe(reload({
      stream: true
    }))
  cb()
}

// 监听文件的变化
function watcher() {
  watch("./js/*.js", js)
  watch("./css/*.scss", css)
  watch("*.html", reload)
}

// 删除dist目录中多余的内容
function clean(cb) {
  del('./dist')
  cb()
}

// server 任务
function serve(cb) {
  browserSync.init({
    server: {
      baseDir: "./"
    }
  })
  cb()
}

exports.scripts = js
exports.styles = css
exports.html = html
exports.clean = clean
exports.default = series([
  clean, html, js, css, serve, watcher
])