MONTHS = [31,28,31,30,31,30,31,31,30,31,30,31]
x,y = map(int, input().split())
res = (sum(MONTHS[:x-1]) + y)%7
if res == 0:
    print("SUN")
elif res == 1:
    print("MON")
elif res == 2:
    print("TUE")
elif res == 3:
    print("WED")
elif res == 4:
    print("THU")
elif res == 5:
    print("FRI")
elif res == 6:
    print("SAT")