from vm import VendingMachine


def test_초기_잔액은_0원():
    m = VendingMachine()
    assert "잔액은 0원입니다" == m.run("잔액")

def test_동전_넣고_잔액_검사():
    m = VendingMachine()
    assert "100원을 넣었습니다" == m.run("동전 100")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_잔액_누적():
    m = VendingMachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")

def test_음료_커피_뽑기():
    m = VendingMachine()
    m.run("동전 500")
    assert "커피가 나왔습니다" == m.run("음료 커피")
    assert "잔액은 350원입니다" == m.run("잔액")

def test_음료_우유_뽑기():
    m = VendingMachine()
    m.run("동전 500")
    assert "우유가 나왔습니다" == m.run("음료 우유")
    assert "잔액은 300원입니다" == m.run("잔액")

def test_음료_밀크커피_뽑기():
    m = VendingMachine()
    m.run("동전 500")
    assert "밀크커피가 나왔습니다" == m.run("음료 밀크커피")
    assert "잔액은 200원입니다" == m.run("잔액")

def test_모르는_음료_뽑기():
    m = VendingMachine()
    m.run("동전 500")
    assert "알 수 없는 음료입니다" == m.run("음료 맥주")
    assert "잔액은 500원입니다" == m.run("잔액")

def test_동전이_부족한_상황에서_음료_뽑기():
    m = VendingMachine()
    m.run("동전 100")
    assert "잔액이 부족합니다" == m.run("음료 커피")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_unknown_command():
    m = VendingMachine()
    assert "알 수 없는 명령입니다" == m.run("웅앵")

def test_valid_coin():
    m = VendingMachine()
    assert "알 수 없는 동전입니다" == m.run("동전 99")
