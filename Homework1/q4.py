def timeConverter(hr, mins, sec):
    sec = hr * 60 ** 2 + mins * 60 + sec
    print(sec)
    return sec

timeConverter(2,8,40)
