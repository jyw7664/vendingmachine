# Vendingmachine 클래스 생성
class Vendingmachine:
# self상태: 잔액을 0으로 초기화
    def __init__(self):
        self._change = 0

# run메서드(연산): self, 문자열에서 공백으로 토큰을 나누고 토큰의 첫번째는 cmd로,
# 두번째는 params로 정의
    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다"
        elif cmd == "동전":
            coin = params[0]
            if int(coin) not in [10, 50, 100, 500]:
                return "알 수 없는 동전입니다"
            else:
                self._change += int(coin)
                return coin + "원을 넣었습니다"
# 커피를 입력하고 잔액이 150원이상일 때 커피값을 빼고 "커피가 나왔습니다."
        elif cmd == "음료":
            known_beverage = "커피"
            price = 150

            beverage = params[0]
            if beverage != known_beverage:
                return "알 수 없는 음료입니다"
            if self._change < price:
                return "잔액이 부족합니다"
            self._change = self._change - price
            return beverage + "가 나왔습니다"

        else:
            return "알 수 없는 명령입니다"
