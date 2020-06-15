srt = '"country":"\u8428\u5c14\u74e6\u591a"'

function ascii2native(strAscii) {
  var output = "";
  var posFrom = 0;
  var posTo = strAscii.indexOf("\\u", posFrom);
  while (posTo >= 0) {
    output += strAscii.substring(posFrom, posTo);
    output += toChar(strAscii.substr(posTo, 6));
    posFrom = posTo + 6;
    posTo = strAscii.indexOf("\\u", posFrom);
  }
  output += strAscii.substr(posFrom);
  return output;
}

function reconvert(str) {
  str = str.replace(/(\\u)(\w{1,4})/gi, function ($0) {
    return (String.fromCharCode(parseInt((escape($0).replace(/(%5Cu)(\w{1,4})/g, "$2")), 16)));
  });
  str = str.replace(/(&#x)(\w{1,4});/gi, function ($0) {
    return String.fromCharCode(parseInt(escape($0).replace(/(%26%23x)(\w{1,4})(%3B)/g, "$2"), 16));
  });
  str = str.replace(/(&#)(\d{1,6});/gi, function ($0) {
    return String.fromCharCode(parseInt(escape($0).replace(/(%26%23)(\d{1,6})(%3B)/g, "$2")));
  });

  return str;
}

console.log(ascii2native(srt));
console.log(reconvert(srt));