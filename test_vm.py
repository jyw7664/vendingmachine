from vm import Vendingmachine


def test_initial_chang_should_be_zero():
   m = Vendingmachine()
   assert "잔액은 0원입니다" == m.run("잔액")


def test_initial_chang_should_be_zero():
   m = Vendingmachine()
    assert "잔액은 0원입니다" == m.run("잔액")

def test_insert_coin_and_check():
   m = Vendingmachine()
    assert "100원을 넣었습니다" == m.run("동전 100")
    assert "잔액은 100원 입니다" == m.run("잔액")

def test_insert_coin_and_check():
   m = Vendingmachine()
    run("동전 100")
    run("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")

def test_error():
   m = Vendingmachine()
   assert "알 수 없는 명령입니다" == m.run("몰라")
