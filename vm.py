def run(raw):
    tokens = raw.split(" ")
    cmd = toens[0]

    if cmd == "잔액":
        return "잔액은 100원입니다"
    else:
        coin = tokens[1]
        return coin + "원을 넣었습니다"
