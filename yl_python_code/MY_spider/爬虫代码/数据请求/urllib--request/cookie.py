import urllib.request

url="https://www.yaozh.com/member/"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
        "Cookie":"acw_tc=2f624a2015541292167687270e7850fa0debd21eb39ae370774ba306f5730f; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1554129192; _ga=GA1.wallhaven_spider.1435628393.1554129192; _gid=GA1.wallhaven_spider.1512661686.1554129192; MEIQIA_VISIT_ID=1JGlGXrYTUrdAu7ws4xmjy9Cjt5; MEIQIA_EXTRA_TRACK_ID=1JGlGVANEKkwLBug5dsCDeFfdRi; yaozh_logintime=1554129280; yaozh_user=723060%09%E6%97%A2%E8%A7%81%E5%90%9B%E5%AD%901102; yaozh_userId=723060; _gat=konachan_spider; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1554129255; yaozh_uidhas=konachan_spider; yaozh_mylogin=1554129286; acw_tc=2f624a2015541292167687270e7850fa0debd21eb39ae370774ba306f5730f; MEIQIA_VISIT_ID=1JGlGXrYTUrdAu7ws4xmjy9Cjt5; MEIQIA_EXTRA_TRACK_ID=1JGlGVANEKkwLBug5dsCDeFfdRi; PHPSESSID=f3jshq48rj31bi3ivmk9cpsue7"
        }
request = urllib.request.Request(url,headers=head)
response = urllib.request.urlopen(request)
data=response.read()
with open("cookie.html","wb") as f:
    f.write(data)
