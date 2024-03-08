from math import trunc
# lv, hp, st, sk, sp, lu, de, re, mo, co
stat = [5, 24, 8, 13, 14, 7, 5, 2, 5, 8]
grow = [0, 80, 30, 55, 55, 30, 20, 20, 0, 0]
bonus1 = [0, 5, 2, 0, 0, 0, 2, 1, 1, 1]
bonus2 = [0, 3, 1, 0, 0, 0, 2, 2, 1, 0]
cap = [0, 60, 20, 20, 20, 30, 20, 20, 0, 0]
cap1 = [0, 0, 4, 9, 10, 0, 2, 3, 0, 0]
cap2 = [0, 0, 0, 10, 10, 0, 0, 0, 0, 0]

lv = 0
skill = "None"
promolv = "0"
promoclass = "0"

while True:
    prepromolv = int(input(f"Joshua's pre-promoted level ({stat[0]}-20): "))
    if prepromolv >= 5 and prepromolv <= 20 and prepromolv != "":
        break 

lv += prepromolv - stat[0]

if prepromolv >= 10:
    while True:
        promoclass = int(input("Swordmaster (1), Assassin (2) or unpromoted (0):"))
        
        if promoclass == 1:
            while True:
                promolv = int(input("Joshua's promoted level (1-20): "))
                if promolv >= 1 and promolv <= 20 and promolv != "":
                    break
            lv += promolv
            stat[1] += bonus1[1]
            stat[2] += bonus1[2]
            stat[3] += bonus1[3]
            stat[4] += bonus1[4]
            stat[6] += bonus1[6]
            stat[7] += bonus1[7]
            stat[8] += bonus1[8]
            stat[9] += bonus1[9]
            cap[2] += cap1[2]
            cap[3] += cap1[3]
            cap[4] += cap1[4]
            cap[6] += cap1[6]
            cap[7] += cap1[7]
        
        if promoclass == 2:
            while True:
                promolv = int(input("Joshua's promoted level (1-20)"))
                if promolv >= 1 and promolv <= 20 and promolv != "":
                    break
            lv += promolv
            stat[1] += bonus2[1]
            stat[2] += bonus2[2]
            stat[3] += bonus2[3]
            stat[4] += bonus2[4]
            stat[6] += bonus2[6]
            stat[7] += bonus2[7]
            stat[8] += bonus2[8]
            stat[9] += bonus2[9]
            cap[2] += cap2[2]
            cap[3] += cap2[3]
            cap[4] += cap2[4]
            cap[6] += cap2[6]
            cap[7] += cap2[7]

        if promoclass == 0:
            break
        break

stat[1] += (grow[1] / 100) * lv
stat[2] += (grow[2] / 100) * lv
stat[3] += (grow[3] / 100) * lv
stat[4] += (grow[4] / 100) * lv
stat[5] += (grow[5] / 100) * lv
stat[6] += (grow[6] / 100) * lv
stat[7] += (grow[7] / 100) * lv


if promoclass == 1:
    print(f"Joshua (Lv {prepromolv}/{promolv} Swordmaster)")
    print("Critical +15")
if promoclass == 2:
    print(f"Joshua (Lv {prepromolv}/{promolv} Assassin)")
    print("Silencer")
if promoclass == 0 or promolv == "0":
    print(f"Joshua (Lv {prepromolv} Myrmidon)")

print(f"HP : {trunc(stat[1])} (/{cap[1]}, {grow[1]}%)")
if trunc(stat[2]) < 10:
    print(f"Str: 0{trunc(stat[2])} (/{cap[2]}, {grow[2]}%)")
else:
    print(f"Str: {trunc(stat[2])} (/{cap[2]}, {grow[2]}%)")
print(f"Skl: {trunc(stat[3])} (/{cap[3]}, {grow[3]}%)")
print(f"Spd: {trunc(stat[4])} (/{cap[4]}, {grow[4]}%)")
if trunc(stat[5]) < 10:
    print(f"Lck: 0{trunc(stat[5])} (/{cap[5]}, {grow[5]}%)")
else:
    print(f"Lck: {trunc(stat[5])} (/{cap[5]}, {grow[5]}%)")
if trunc(stat[6]) < 10:
    print(f"Def: 0{trunc(stat[6])} (/{cap[6]}, {grow[6]}%)")
else:
    print(f"Def: {trunc(stat[6])} (/{cap[6]}, {grow[6]}%)")
if trunc(stat[7]) < 10:
    print(f"Res: 0{trunc(stat[7])} (/{cap[7]}, {grow[7]}%)")
else:
    print(f"Res: {trunc(stat[7])} (/{cap[7]}, {grow[7]}%)")
print(f"Mov: 0{stat[8]}")
print(f"Con: 0{stat[9]}")
