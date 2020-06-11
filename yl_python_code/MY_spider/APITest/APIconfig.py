import json

app_id = "hmnqziklvnthnckr"
app_secret = "TFZnZVdMSVdCdUlVUEhaOFVQOHBZdz09"
HOST = "https://www.mxnzp.com/api"


def json_format(json_str):
    return json.dumps(json.loads(json_str), indent=4, separators=(',', ':'), ensure_ascii=False)
