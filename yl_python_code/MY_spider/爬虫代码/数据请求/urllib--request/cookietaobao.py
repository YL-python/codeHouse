import urllib.request

url="https://cart.taobao.com/cart.htm?prepvid=200_11.15.101.201_385_1554130092113&extra=&spm=a231o.7076277%2Fb.1997525049.1.242d4608CrstRN&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739&pid=mm_26632322_6858406_107180850312&clk1=045dd234956455ababf0dd4dc114de5f&unid=&source_id=&app_pvid=200_11.15.101.201_385_1554130092113"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
        "Cookie":"t=ad299bf58faed186e06b0600e2c6d16a; cookie2=1ad1c772d2d283fb2102631bdce178c7; v=0; _tb_token_=555b3e757333e; UM_distinctid=169d95e928e36b-0105ab92b9ec04-70193c4f-e1000-169d95e928f49d; cna=PyshFTbJz3cCAW9PCsY9FSKR; unb=3489280393; sg=231; _l_g_=Ug%3D%3D; skt=bde79da400a12843; cookie1=UIXzo5XKIc7bgwxY07%2FZxf53brkOFTp5hsypp022VWo%3D; csg=72b70c1f; uc3=vt3=F8dByEnb3tXsPxMPSRI%3D&id2=UNQ%2F31l0C4mENA%3D%3D&nk2=txAg1DzSIkdeqDP1&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; existShop=MTU1NDEzMDA5Mg%3D%3D; tracknick=%5Cu4E91%5Cu80E1%5Cu4E0D%5Cu559C0412; lgc=%5Cu4E91%5Cu80E1%5Cu4E0D%5Cu559C0412; _cc_=VT5L2FSpdA%3D%3D; dnk=%5Cu4E91%5Cu80E1%5Cu4E0D%5Cu559C0412; _nk_=%5Cu4E91%5Cu80E1%5Cu4E0D%5Cu559C0412; cookie17=UNQ%2F31l0C4mENA%3D%3D; tg=0; ubn=p; mt=ci=35_1; thw=cn; ucn=unszyun; _m_h5_tk=6fad3347dad649aed4af46ac25195d24_1554139812867; _m_h5_tk_enc=2f53a18cb39881776ca3d9acdd8d38eb; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTZ4M4gjXfcUw%3D%3D&cart_m=0&tag=8&lng=zh_CN; swfstore=9574; l=bBrWpRLVv-69XrBbBOCNNuI8arbO9IRvMuPRwNDXi_5It6Y_y07Oli5rnFv6Vj5R_O8B4yyY4s99-etk1; isg=BCwseYAnXF2m50hhEt0OF-hM_QqeTdDp0aexPYZtBVd6kcybrvEDHyYrtRmMUQjn; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-konachan_spider%26_ato%3D0; whl=-konachan_spider%260%260%261554130172223"
        }
request = urllib.request.Request(url,headers=head)
response = urllib.request.urlopen(request)
data=response.read()
with open("cookie_taob.html","wb") as f:
    f.write(data)
