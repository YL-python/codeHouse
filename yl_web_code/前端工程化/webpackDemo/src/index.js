import('./index.scss')
import afn from './a.js'
import Logo from './logo.png';

console.log("hello webpack!!!!!!")
afn()

if (process.env.NODE_ENV === "production") {
  console.log("production")
}
if (process.env.NODE_ENV === "development") {
  console.log("development")
}