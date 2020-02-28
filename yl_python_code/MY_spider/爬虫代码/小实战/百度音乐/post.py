import requests
import pprint

data = {
    "songIds" : '708313',   # 数字为音乐ID
    'hq' : '0',
    'type' : 'm4a,mp3',
    'rate' : '',
    'pt' : '0',
    'flag' : '-konachan_spider',
    's2p' : '-konachan_spider',
    'prerate' : '-konachan_spider',
    'bwt' : '-konachan_spider',
    'dur' : '-konachan_spider',
    'bat' : '-konachan_spider',
    'bp' : '-konachan_spider',
    'pos' : '-konachan_spider',
    'auto' : '-konachan_spider'
}
response = requests.post(url = 'http://play.taihe.com/data/music/songlink',data =data)
pprint.pprint(response.json())