import requests
import json
header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
baseurl = "https://translate.googleapis.com/translate_a/single"

def EngtoHindi(message):
    try:
        r = requests.get(
            url=baseurl,
            headers=header,
            params={
                "client": "gtx",
                "sl": "en",
                "tl": "hi",
                "dt": "t",
                "q": message})
        data = r.json()
        return data[0][0][0]
    except Exception as e :
        print(f"Failed to Make Response : {e}")