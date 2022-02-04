# addres = "http://naver.com"

# rule1 = addres[addres.index("n") : addres.index(".")]
# rule2 = addres[addres.index("n") : addres.index("n") + 3]
# print("생성된 비밀번호 : ", str(rule2)+str(len(rule1))+str(rule1.count("e"))+"!")

# rule1 = addres.replace("http://", "")
# rule2 = rule1[:rule1.find(".")]

# password = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + str("!")
# print("{0} 사이트의 비밀번호는 {1}입니다.".format(addres, password))



#####리스트#########
# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.find("조세호")) # 리스트, 튜플, 딕셔너리 자료형에서는 find사용하게 되면 AttributeError 발생. -> index 함수 사용
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


#######사전###########
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))
# # print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# del cabinet["A-3"]
# print(cabinet)

# print(cabinet.keys())

# print(cabinet.values())

# print(cabinet.items())

# cabinet.clear()
# print(cabinet)



##########튜플########### (list와 다르게 내용 변경이나 추가 못함. 대신 빠름)
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print((name, age, hobby))




#########세트############# (중복 불가, 순서 없음)
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# print(java & python)
# print(java.intersection(python))

# print(java | python)
# print(java.union(python))

# print(java - python)
# print(java.difference((python)))

# python.add("김태호")
# print(python)

# java.remove("김태호")
# print(java)



##########자료 구조의 변경############
# menu = {"커피", "우유", "쥬스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))




#########퀴즈###########
# from random import *
# lst = list(range(1,21))
# shuffle(lst)

# chicken = sample(lst, 1)
# lst = list(set(lst) - set(chicken))
# coffee = sample(lst, 3)

# print("""
# 치킨 당첨자 : {0}
# 커피 당첨자 : {1}
# -- 축하 드립니다 --
# """.format(chicken, coffee))




#########if#########
# weather = input("오늘 날씨는 어때요?")  # input은 항상 문자 형태로 값을 받음
# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp :
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30 :
#     print("괜찮은 날씨에요")
# elif 0  <= temp < 10 :
#     print("외투를 챙기세요")
# else :
#     print("너무 추워요 나가지 마세요")



############for###############
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(1, 6) :
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks :
#     print("{0}, 커피가 준비되었습니다.".format(customer))




###########while#############
# customer = "토르"
# index = 5
# while index >= 1 :
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True :
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비되었습니다. ".format(customer))
#     person = input("이름이 어떻게 되세요?")




###########continue, break############
# absent = [2, 5]
# no_book = [7]

# for student in range(1, 11) :
#     if student in absent :
#         continue # 조건 만족 시에도 다음 반복문 진행
#     elif student in no_book :
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break # 조건 만족 시 반복문 종료
#     print("{0}, 책을 읽어봐".format(student))




##########한줄 for###################
# students = list(range(1,6))
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)




###########퀴즈#############
# from random import *


# customer = range(1, 51)
# customer_count = 0

# for choozen_customer in customer :
#     time = randint(5, 50)
#     if 5 <= time <= 15 :
#         print("[0] {0}번쨰 손님 (소요시간 : {1}분)".format(choozen_customer, time))
#         customer_count += 1
#     else :
#         print("[ ] {0}번쨰 손님 (소요시간 : {1}분)".format(choozen_customer, time))

# print("총 탑승객 : {0} 분".format(customer_count))





#########함수#############
# def open_account() :
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money) :
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money) :
#     if balance >= money :
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else :
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))

# def withdraw_night(balance, money) :
#     commission = 100
#     return commission, balance - money - commission


# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))




###########함수 기본값 설정###########
# def profile(name, age, main_lang) :
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile(name, age=17, main_lang="파이썬") :
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang) :
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")



###########가변인자#############
# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print("이름 : {0}]\t나이 : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language) :
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     for lang in language :
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "kotlin", "Swift", "", "", "")





########지역변수 전역변수##########
# gun = 10

# def checkpoint(soldiers) : 
#     global gun # 전역 공간에 있는 gun 변수 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers) :
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))




########퀴즈##########

# def std_weight(height, gender) :
#     if gender == "남자" :
#         man_std = height * height * 22
#         print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height * 100, round(man_std, 2)))
#     elif gender == "여자" :
#         woman_std = height * height * 21   
#         print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height * 100, round(woman_std, 2)))
#     else :
#         print("잘못된 입력입니다.")


# human_height = float(input("키를 입력하세요(m)"))
# human_gender = input("성별을 입력하세요.(남자 or 여자)")
# std_weight(human_height, human_gender)




#########표준 입출력##########
# import sys

# print("Python", "Java", "JavaScript", sep=",", end="?")
# print("무엇이 더 재미있을까요?")

# print("Python", "Java", file=sys.stdout) # 표준 출력으로 문장이 찍힘
# print("Python", "Java", file=sys.stderr) # 표준 err로 문장이 찍힘...

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items() :
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 21) : 
#     print("대기번호 : ", str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 :")
# print("입력하신 값은 ", answer, "입니다.")




#########출력 포멧#########
# print("{0: >10}".format(500)) # 빈 공간은 스페이스로 하되, 오른쪽 정렬하면서 10자리 공간 확보
# print("{0: >+10}".format(500)) # 빈 공간은 스페이스로 하되, 오른쪽 정렬하면서 10자리 공간 확보. 양수일 떈 +, 음수일 땐 -로 표시
# print("{0:_<10}".format(500)) # 빈공간은 _로 하되, 왼쪽 정렬하면서 공간 10개 확보
# print("{0:,}".format(100000000000)) # 3자리마다 , 찍어주기
# print("{0:^<+30,}".format(1000000000000000))

# print("{0:f}".format(5/3)) # 소수점 표시
# print("{0:.2f}".format(5/3)) # 소수점 2째 자리까지 표시




##########파일 입출력###########
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 일고 커서는 다음 줄로 이동
# print(score_file.readline()) 
# print(score_file.readline()) 
# print(score_file.readline()) 
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line :
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")

# score_file.close()



##########pickle##########
# import pickle
# profile_file = open("profile.pickle", "wb") # 피클을 쓰기 위해서는 binary 타입 반드시 설정 해줘야 됨. 코딩은 따로 필요 없음.and
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()




##########with########### 파일을 매번 닫을 필요가 없음.
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())



#########퀴즈###########
# def write_report(week):
#     with open("{0}주차.txt".format(week), "w", encoding="utf8") as report_file:
#         report_file.write("""
#         - {0} 주차 주간보고 -
#         부서 :
#         이름 :
#         업무 요약 :
#         """.format(week))

# week_report = int(input("몇개 주차까지의 보고서가 필요합니까?"))

# for weeks in range(1,week_report + 1):
#     write_report(weeks)




########클래스######### 
# name = "마린"
# hp = 40
# damage = 5
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)


class Unit:
    def __init__(self, name, hp, damage): # __init__ 파이썬에서 사용하는 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # class로 만들어 지는 변수를 객체라고 함.
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


