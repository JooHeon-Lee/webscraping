import requests
url = ""
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status() # 여기서 문제가 안 생기면 그 뒤로 진행

with open("test.html", "w", encoding="utf8") as f:
    f.write(res.text)
