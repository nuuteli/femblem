from math import trunc
# lv, hp, st, sk, sp, lu, de, re, mo, co
stat = [2, 23, 7, 5, 7, 3, 7, 00, 7, 10]
grow = [0, 90, 30, 30, 30, 50, 50, 30, 0, 0]
bonus = [0, 2, 1, 1, 1, 0, 2, 1, 1, 2]
cap = [0, 60, 20, 20, 20, 30, 20, 20, 0, 0]
pcap = [0, 0, 5, 6, 4, 30, 5, 5, 0, 0]
preclass = "Cavalier"
promoclass = "Paladin"
lv = 0
promolv = "-"

while True:
    prepromolv = int(input(f"Lowen's pre-promoted level ({stat[0]}-20): "))
    if prepromolv >= 2 and prepromolv <= 20 and prepromolv != None:
        break

lv += prepromolv - stat[0]

if prepromolv >= 10:
    while True:    
        promolv = int(input("Lowen's promoted level (0-20): "))
        if promolv >= 0 and promolv <= 20 and promolv != None:
            break

    lv += promolv
    if promolv > 0:
        lv -= 1
        stat[1] += bonus[1]
        stat[2] += bonus[2]
        stat[3] += bonus[3]
        stat[4] += bonus[4]
        stat[6] += bonus[6]
        stat[7] += bonus[7]
        stat[8] += bonus[8]
        stat[9] += bonus[9]
        cap[2] += pcap[2]
        cap[3] += pcap[3]
        cap[4] += pcap[4]
        cap[6] += pcap[6]
        cap[7] += pcap[7]
else:
    promolv == 0

stat[1] += (grow[1] / 100) * lv
stat[2] += (grow[2] / 100) * lv
stat[3] += (grow[3] / 100) * lv
stat[4] += (grow[4] / 100) * lv
stat[5] += (grow[5] / 100) * lv
stat[6] += (grow[6] / 100) * lv
stat[7] += (grow[7] / 100) * lv

if promolv == 0:
    print(f"Lowen (Lv {prepromolv} {preclass}):")
else:
        print(f"Lowen (Lv {prepromolv}/{promolv} {promoclass}):")
print(f"HP : {trunc(stat[1])} (/{cap[1]}, {grow[1]}%)")
print(f"Str: {trunc(stat[2])} (/{cap[2]}, {grow[2]}%)")
print(f"Skl: {trunc(stat[3])} (/{cap[3]}, {grow[3]}%)")
print(f"Spd: {trunc(stat[4])} (/{cap[4]}, {grow[4]}%)")
print(f"Lck: {trunc(stat[5])} (/{cap[5]}, {grow[5]}%)")
print(f"Def: {trunc(stat[6])} (/{cap[6]}, {grow[6]}%)")
print(f"Res: {trunc(stat[7])} (/{cap[7]}, {grow[7]}%)")
print(f"Mov: {stat[8]}")
print(f"Con: {stat[9]}")
