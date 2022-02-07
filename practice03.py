from random import *
# class Unit:
#     def __init__(self, name, hp, damage): # __init__ 파이썬에서 사용하는 생성자
#         self.name = name  # 멤버 변수. class 내에서 정의된 함수
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5) # class로 만들어 지는 변수를 객체라고 함.
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True  # 외부에서 clocking 이라는 함수를 임의로 추가함. 확장한 개체에 대해서만 적용.

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# class Unit:
#     def __init__(self, name, hp, speed): # __init__ 파이썬에서 사용하는 생성자
#         self.name = name  # 멤버 변수. class 내에서 정의된 함수
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(self.name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

        
# class AttackUnit(Unit):  # Unit의 내용을 상속받아서 만듦.
#     def __init__(self, name, hp, speed, damage): # __init__ 파이썬에서 사용하는 생성자
#         Unit.__init__(self, name, hp, speed)  # Unit에서 상속받아서 name, hp를 사용
#         self.damage = damage
    
#     def attack(self, location):  # class 앞에서는 self를 무조건 사용한다고 생각.
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))


# firebat1 = AttackUnit("파이어뱃", 50 ,16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(self.name, location, self.flying_speed))


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)   # Flyable에 있는 fly함수를 사용

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")


# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# class Tank(AttackUnit):
#     seize_developed = False
    
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
#         if self.seize_mode == False:
#             print("{0} : 시즈 모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False


# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
#         else:
#             print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
#             self.clocked = True


# m1 =  Marine()
# m2 =  Marine()
# m3 =  Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_developed = True
# print("[알림]탱크 시즈모드 개발이 완료 되었습니다.")

# for unit in attack_units:
#     if isinstance(unit, Marine):  # isinstance : 객체가 어떤 class의 객체인지 확인
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# for unit in attack_units:
#     unit.attack("1시")

# for unit in attack_units:
#     unit.damaged(randint(5, 20))




##########퀴즈#############
# buildings = []

# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))


# h1 = House("강남", "아파트", "매매", "10억", "2010년")
# h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# h3 = House("송파", "빌라", "월세", "500/50", "2000년")

# buildings.append(h1)
# buildings.append(h2)
# buildings.append(h3)

# print("총 {0}대의 매물이 있습니다.".format(len(buildings)))
# for sell_building in buildings:
#     sell_building.show_detail()




###########예외처리###########
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요")))
#     nums.append(int(input("두 번째 숫자를 입력하세요")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)



########에러 발생시키기########
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")



###########사용자 정의 예외처리, finally##########
# class BigNumberErr(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberErr("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberErr as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:  # err가 발생하든 말든 무조건 마지막에 적용
#     print("계산기를 이용해 주셔서 감사합니다.")




#########퀴즈##############
# chicken = 10
# waiting = 1

# class SoldoutError(Exception):
#     def __init__(self):
#         pass


# while(True):
#     try:
#         print("[남은 치킨] : {0}".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order < 1:
#             raise ValueError
#         # elif chicken == 0:   # elif로 chicken이 소진되었을 때 SoldoutError를 발생시키지 않는 이유는...? -> if문 시작에서 order를 기준으로 처리했기 때문. 독립적으로 다른 변수를 처리할 떄는 또다시 if를 쓴다.....!!!!!
#         #     raise SoldoutError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken == 0:
#             raise SoldoutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldoutError:
#         print("재고가 소진되어 더이상 주문을 받지 않습니다.")
#         break




############모듈##############
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(4)
# # price_soldier(5)

# from theater_module import price_soldier as price
# price(5)



##########패키지###########
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietamPackage()
# trip_to.detail()

# from travel import *   # 파일 중에서 어떤 모듈을 공개할건지 안할건지는 정해줘야함. 그래서 __init__모듈에서 모듈리스트 만드는것인듯
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


###########패키지, 모듈 위치###########
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))



##########패키지 설치###########
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


#########내장 함수##########
# print(dir())
# import random
# print(dir())
# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))


#########외장 함수##########
# import glob  # 경로 내의 폴더 / 파일 목록 조회
# print(glob.glob("*.py"))

# import os
# print(os.getcwd())  # 현재 디렉토리 

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는", datetime.date.today())

# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)


import byme
byme = byme.Byme()
byme.sign()