for i in range(1000, 10000):
    si = str(i)
    co1 = int(si[0]) + int(si[1])
    co2 = int(si[1]) + int(si[2])
    co3 = int(si[2]) + int(si[3])
    list_co = sorted([co1, co2, co3])
    if str(list_co[1]) + str(list_co[2]) == '1418':
        print(i)
        break
