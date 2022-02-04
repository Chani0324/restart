# print("다시 시작")
# print("first phase : go to developer")


# print(5)
# print(-10)
# print(5*3)


# print('restart')
# print("hello"*3)


# print(5 > 10)
# print(10 < 5)
# print(not True)


# name = "연탄이"
# animal = "강아지"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집", animal, "이름은", name, "예요")
# print(name, "는", str(age), "살이며", hobby, "좋아해요")
# print(name, "는 어른일까요?", str(is_adult))

# station = "사당"
# print(station, "행 열차가 들어오고 있습니다.")

# station = "신도림"
# print(station, "행 열차가 들어오고 있습니다.")

# station = "인천공항"
# print(station, "행 열차가 들어오고 있습니다.")


# print(2**3) # 2^3
# print(5%3) # 5를 3으로 나눈 나머지
# print(5//3) # 5를 3으로 나눈 몫
# print(3 == 3) # True
# print(1 != 3) # Tre

# print((3 > 0) and (3 < 5))
# print((3 > 0) & (3 < 5))

# print((3 > 0) or (3 > 5))
# print((3 > 0) | (3 > 5))

# number = 2
# number = number + 3

# number = 2
# number += 3


# print(abs(-5))
# print(pow(4, 2))
# print(max(5, 12))
# print(min(5, 12))
# print(round(3.14))
# print(round(3.55))

# from math import *
# print(floor(4.99))
# print(ceil(4.99))
# print(sqrt(16))


# from random import *

# print(random()) # 0.0 이상 1.0 미만의 값을 생성
# print(int(random() *10))

# print(randrange(1, 11)) # 1부터 11미만의 정수값 생성
# print(randint(1, 10))

# from random import  *
# print("오프라인 스터디 모임 날짜는 매월", str(randint(4,28)), str(randint(4,28)), str(randint(4,28)), "일로 선정되었습니다.")



# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)


# jumin = "990120-1234567"

# print("성별 :", jumin[7])
# print("연도 : ", jumin[0:2]) # 0부터 2번째 직전까지의 값 출력
# print("월 : ", jumin[2:4])
# print("일 : ", jumin[4:6])

# print("생년월일 : ", jumin[:6])
# print("뒤 7자리 : ", jumin[7:])
# print("뒤 7자리 : ", jumin[-7:])



# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java"))

# print(python.count("n"))


# print("나는 %d살입니다." % 20)  # 정수값만 문장 중간에 넣기 가능
# print("나는 %s을 좋아해요." % "파이썬")  # 문자열 문장 중간에 넣기 가능. 숫자 상관없음. str
# print("Apple은 %c로 시작해요." % "A")   # 한글자만 문장 중간에 넣기 가능
# print("나는 %s와 %s 좋아해요" %("파란", "빨간"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}와 {} 좋아해요".format("파란", "빨간"))
# print("나는 {0}와 {1} 좋아해요".format("파란", "빨간"))
# print("나는 {1}와 {0} 좋아해요".format("파란", "빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 \"나도코딩\"입니다.")
# print("C://User//restart")


# addres = "http://naver.com"

# rule1 = addres[addres.index("n") : addres.index(".")]
# rule2 = addres[addres.index("n") : addres.index("n") + 3]
# print("생성된 비밀번호 : ", str(rule2)+str(len(rule1))+str(rule1.count("e"))+"!")

# rule1 = addres.replace("http://", "")
# rule2 = rule1[:rule1.find(".")]

# password = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + str("!")
# print("{0} 사이트의 비밀번호는 {1}입니다.".format(addres, password))



# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # print(subway.find("조세호")) # 리스트, 튜플, 딕셔너리 자료형에서는 find사용하게 되면 AttributeError 발생. -> index 함수 사용
# print(subway.index("조세호"))

# subway.append("하하") # 리스트 맨 끝에 추가
# print(subway)

# subway.insert(1, "정형돈") # 리스트에서 몇 번쨰에 들어가고 뭐가 들어가는지 설정
# print(subway)

# print(subway.pop()) # 리스트 끝에서 하나씩 제외시킴
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)


# num_list = [5,2,3,1,4]
# num_list.sort() # 순서 정렬
# print(num_list)

# num_list.reverse() # 순서 역정렬
# print(num_list)

# num_list.clear() # 리스트 내용 제거
# print(num_list)



# mix_list = ["조세호", 20, True]
# num_list = [5,2,3,1,4]
# mix_list.extend(num_list) # 리스트 + 리스트 구조
# print(mix_list)

# mix_list.insert(2, num_list) # 리스트 안에 리스트가 또 들어가는 구조
# print(mix_list)



