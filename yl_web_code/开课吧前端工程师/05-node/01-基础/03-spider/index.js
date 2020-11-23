const http = require('http');
const cheerio = require('cheerio');
const fs = require('fs');
let webUrl = 'http://news.ifeng.com/';
http.get(webUrl, (res) => {
  let str = '';
  res.on('data', (chunk) => {
    str += chunk;
  });
  res.on('end', () => {
    // console.log(str);
    formatData(str);
  });
});

function formatData(html) {
  let $ = cheerio.load(html);
  //    console.log( $(".news-stream-basic-news-list li").length );
  let arr = [];
  $('.news-stream-basic-news-list li').each((k, v) => {
    let obj = {
      id: k + 1,
      title: $(v).find('a').text(),
      imgUrl: 'http:' + $(v).find('img').attr('src'),
      from: $(v).find('.news-stream-newsStream-mr10').text(),
      newTime: $(v).find('time').text(),
    };
    //    console.log(obj);
    arr.push(obj);
  });
  fs.writeFileSync('./data.json', JSON.stringify(arr));
}
