# 미니 프로젝트 구현
# 난이도 상 - 음료 자판기 프로그램
# 210825 vending_machine.py

#import random

menus = ['콜라', '사이다', '생수', '커피', '주스']
prices = [1200, 1200, 600, 300, 800]

print('----메뉴----')

for i, (menu, price) in enumerate(zip(menus, prices)):
    print(i + 1, menu, price)

money = int(input('돈을 투입하세요 : '))
choice = int(input('메뉴를 선택하세요 : '))

menu = menus[choice - 1]
price = prices[choice - 1]

if price <= money:
    print('선택 메뉴 : ', menu)
    print('메뉴 가격 : ', price)
    print('거스름 돈 : ', money - price)
else:
    print('잔액이 부족합니다')


