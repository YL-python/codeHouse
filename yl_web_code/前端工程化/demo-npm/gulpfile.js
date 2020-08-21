const { src, dest, series, watch } = require('gulp');
const browserSync = require('browser-sync').create();
const reload = browserSync.reload;
const plugins = require('gulp-load-plugins')();
const del = require('del');
/*
有了这个插件，gulp-uglify => plugins.uglify = require('gulp-uglify');
并且只能使用gulp-为前缀的一些插件
*/

/*压缩js文件 uglifyjs*/
function js(cb) {
  src('js/*.js')
    //下一个处理环节,混淆js
    .pipe(plugins.uglify())
    //下一个处理环节，输出到指定目录下
    .pipe(dest('./dist/js'))
    .pipe(reload({ stream: true }))
  cb()
}

/*对scss、less编译 压缩 输出css文件*/
function css(cb) {
  src('css/*.scss')
    .pipe(plugins.sass({ outputStyle: 'compressed' }))
    .pipe(plugins.autoprefixer({
      cascade: false,
      remove: false
    }))
    .pipe(dest('./dist/css'))
    .pipe(reload({ stream: true }))
  cb()
}

/*监听文件变化*/
function watcher(cb) {
  watch('js/*.js', js)
  watch('css/*.scss', css)
  cb()
}

/*清空dist目录*/
function clean(cd) {
  del('./dist')
  cd()
}

//server task
function serve(cb) {
  browserSync.init({
    server: {
      baseDir: './'
    }
  })
  cb()
}

exports.scripts = js
exports.styles = css
exports.clean = clean

exports.default = series([
  clean,
  js,
  css,
  serve,
  watcher
])