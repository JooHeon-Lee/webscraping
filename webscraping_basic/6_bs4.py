import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup객체가 갖고있는것 중 첫번재 a태그 return
# print(soup.a.attrs) # a 태그의 속성을 가져옴
# print(soup.a["href"]) # a태그의 href 값 가져옴

# print(soup.find("a", attrs={"class" : "Nbtn_upload"})) # class="Nbtn_upload" 인 a element를 찾음
# print(soup.find(attrs={"class" : "Nbtn_upload"}))  # 태그는 생략가능

# print(soup.find("li", attrs={"class" : "rank01"}))
# rank1 = soup.find("li", attrs={"class" : "rank01"}) # 객체로 받아서 a태그만 뽑아낼수있음
# print(rank1.a.get_text())

# print(rank1.next_sibling) 개행이 있으면 next_sibling 두번 해줘야함
# rank2 = rank1.next_sibling.next_sibling # next_sibling => 자식요소 가져옴
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling 
# print(rank2.a.get_text())

#print(rank1.parent) # 부모 요소 가져옴

# rank2 = rank1.find_next_sibling("li") # next_sibling하는데 조건에 해당하는거만 찾음 즉, 개행은 안찍힘
# print(rank2.a.get_text())

# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

##여러개 가져오고싶을때
 # print(rank1.find_next_siblings("li")) # rank1기준으로 형제를 모두 가져옴

webtoon = soup.find("a", text="조조코믹스-킹스앱스 7화") # a태그의 텍스트를 토대로 찾을 수 있음.
print(webtoon)