from math import trunc
lv = 2
plv = 0
hp = 23
st = 7
sk = 5
sp = 7 
lu = 3 
de = 7
re = 0
mo = 7
co = 10
hpg = 0.9
stg = 0.3
skg = 0.3
spg = 0.3
lug = 0.5
deg = 0.5
reg = 0.3
promolv = "-"

while True:
    prepromolv = int(input("What is Lowen's pre-promoted level?"))
    if prepromolv >= 2 and prepromolv <= 20:
        break

lv += prepromolv
lv -= 2

if prepromolv >= 10:
    while True:    
        promolv = int(input("What is Lowen's promoted level?"))
        if promolv >= 1 and promolv <= 20:
            break

    lv += promolv
    lv -= 1
    if promolv >= 1:
        hp += 2
        st += 1
        sk += 1
        sp += 1
        de += 2
        re += 1
        mo += 1
        co += 2
else:
    promolv == 0

hp += hpg * lv
st += stg * lv
sk += skg * lv
sp += spg * lv
lu += lug * lv
de += deg * lv
re += reg * lv

print(f"Lowen's average stats (Lv {prepromolv}/{promolv}):")
print(f"HP: {trunc(hp)}")
print(f"Strength: {trunc(st)}")
print(f"Skill: {trunc(sk)}")
print(f"Speed: {trunc(sp)}")
print(f"Luck: {trunc(lu)}")
print(f"Defence: {trunc(de)}")
print(f"Resistance: {trunc(re)}")
print(f"Movement: {mo}")
print(f"Constitution: {co}")