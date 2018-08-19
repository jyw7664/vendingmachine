from vm import Vendingmachine

# 잔액 테스트
def test_initial_chang_should_be_zero():
    m = Vendingmachine()
    assert "잔액은 0원입니다" == m.run("잔액")

# 동전을 넣고 잔액이 올라가는지 확인
def test_insert_coin_and_check():
    m = Vendingmachine()
    assert "100원을 넣었습니다" == m.run("동전 100")
    assert "잔액은 100원 입니다" == m.run("잔액")

# 동전을 두 번 넣고 잔액이 올라가는지 확인
def test_insert_coin_and_check():
    m = Vendingmachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")

# 정의되지 않은 명령(몰라)을 넣었을 때 "알 수 없는 명령입니다."
def test_error():
    m = Vendingmachine()
    assert "알 수 없는 명령입니다" == m.run("몰라")
