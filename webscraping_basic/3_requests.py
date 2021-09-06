import requests
res = requests.get("http://google.com")
res.raise_for_status() # 여기서 문제가 안 생기면 그 뒤로 진행

print("응답코드 : ", res.status_code) # 200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 : ", res.status_code, "]")

# res.raise_for_status() # 문제가 생겻을때 오류를 내뱉고 프로그램을 끝내줌
# print("웹 스크래핑을 진행합니다.")

print(len(res.text))
# print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
