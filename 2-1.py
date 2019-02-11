print("string")
print("sample", end = "  ")
print("test")
print("I'm haha")
print('I\'m haha')

name = "yuji"
age = 27
phone = "010-3228-9311"
print("내 이름은 " + name + "입니다.", end = " ")
print("나는 ", age, "살 입니다.")
print("내 연락처는 " + phone + "입니다!")

print("안녕하세요, %s씨. %d 새해 복 많이 받으세요." %("유지", 2019))
print("안녕하세요, {name}씨. 오늘은 {day}입니다.".format(name="유지", day="일요일"))


name = input("이름을 입력하세요. ")
age = input("나이를 입력하세요. ")
phone = input("휴대폰 번호를 입력하세요. ")

print("내 이름은 ", name, "입니다.", end = " ")
print("내 이름은 ", len(name), "글자입니다.")
print("나는 ", age, "살 입니다.")
print("내 연락처는", phone, "입니다.")
