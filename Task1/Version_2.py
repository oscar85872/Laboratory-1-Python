for fg,bg in [(47, 37), (41, 31)]:
    for i in range(8):
        print(f"\u001b[{fg}m\u001b[{bg}m" + " " * 60 + "\u001b[0m")