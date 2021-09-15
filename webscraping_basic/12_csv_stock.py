import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

for page in range(1,2): # 1~ 4페이지까지
    res = requests.get(url + str(page))
    res.raise_for_status() # 접근에 문제가 없는지 확인
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터 skip ==> tr밑에 td가 하나인거는 의미없는 데이터
            continue
        data = [column.get_text().strip() for column in columns] # strip쓰면 \n 같은 불필요한거 지워줌
        print(data)