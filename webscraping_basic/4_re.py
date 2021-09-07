# 정규식
import re

p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case
# ^ (^de) : 문자열의 시작 의미 -> desk, destination 
# $ (se$) : 문자열의 끝 -> case, base

# m = p.match("case")
# # print(m.group()) # 매치되지 않으면 에러가 발생

def print_match(m):
    if m: # 매치가 되었을때
        print("m.group() : ", m.group()) # 일치하는 문자열 반환
        print("m.string : ",m.string) # 입력받은 문자열을 그대로 반환
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 인덱스
        print("m.end() : ", m.end()) # 일치하는 문자열의 끝 인덱스
        print("m.span() : ", m.span()) # 일치하는 문자열의 시작과 끝 인덱스
    else:
        print("매칭되지 않았습니다.")    
# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인, 처음에 매칭되면 그 뒤는 상관없음
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인(포함되는지)
# print_match(m)

# lst = p.findall("gool care cafe") # findall : 일치하는 모든 것을 리스트로 반환
# print(lst)

# 정규식 사용 순서
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인(포함되는지)
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case
# ^ (^de) : 문자열의 시작 의미 -> desk, destination 
# $ (se$) : 문자열의 끝 -> case, base