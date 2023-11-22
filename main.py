import math
import random
import roman

metals_zarfiat = {
    1: ['H', 1, 1], 3: ['Li', 1, 1], 4: ['Be', 1, 2], 5: ['B', 1, 3], 11: ['Na', 1, 1], 12: ['Mg', 1, 2],
    13: ['Al', 1, 3], 19: ['K', 1, 1], 20: ['Ca', 1, 2], 24: ['Cr', 2, 2, 3], 25: ['Mn', 5, 2, 3, 4, 6, 7],
    26: ['Fe', 2, 2, 3], 27: ['Co', 2, 2, 3], 28: ['Ni', 2, 2, 3], 29: ['Cu', 2, 1, 2], 30: ['Zn', 1, 2],
    37: ['Rb', 1, 1], 38: ['Sr', 1, 2], 47: ['Ag', 1, 1], 48: ['Cd', 1, 2], 50: ['Sn', 2, 2, 4], 55: ['Cs', 1, 1],
    56: ['Ba', 1, 2], 80: ['Hg', 2, 1, 2], 82: ['Pb', 2, 2, 4], 714: ['NH4', 1, 1]}
nonmetals_zarfiat = {
    1: ['H', 1], 7: ['N', 3], 8: ['O', 2], 9: ['F', 1], 15: ['P', 3], 16: ['S', 2], 17: ['Cl', 1], 35: ['Br', 1],
    53: ['I', 1], 81: ['OH', 1], 683: ['CO3', 2], 782: ['NO2', 1], 783: ['NO3', 1], 1584: ['PO4', 3], 1683: ['SO3', 2],
    1684: ['SO4', 2]}
metals_name = {
    1: "هیدروژن", 3: "لیتیم", 4: "بریلیم", 5: "بور", 11: "سدیم", 12: "منیزیم", 13: "آلومینیم", 19: "پتاسیم", 20: "کلسیم", 
    24: "کروم", 25: "منگنز", 26: "آهن", 27: "کبالت", 28: "نیکل", 29: "مس", 30: "روی", 37: "روبیدیم", 38: "استرانسیم", 
    47: "نقره", 48: "کادمیم", 50: "قلع", 55: "سزیم", 56: "باریم", 80: "جیوه", 82: "سرب", 714: "آمونیوم"}
nonmetals_name = {
    1: "هیدرید", 7: "نیترید", 8: "اکسید", 9: "فلئورید", 15: "فسفید", 16: "سولفید", 17: "کلرید", 35: "برمید", 53: "یدید", 
    81: "هیدروکسید", 683: "کربنات", 782: "نیتریت", 783: "نیترات", 1584: "فسفات", 1683: "سولفیت", 1684: "سولفات"}

atomi1 = [1, 3, 4, 5, 11, 12, 13, 19, 20, 24, 25, 26, 27, 28, 29, 30, 37, 38, 47, 48, 50, 55, 56, 80, 82, 714]
x = random.randint(1, len(atomi1) - 1)
atomi2 = [1, 7, 8, 9, 15, 16, 17, 35, 53, 81, 683, 782, 783, 1584, 1683, 1684]
y = random.randint(1, len(atomi2) - 1)
felez = metals_zarfiat[atomi1[x]]
felez_name = metals_name[atomi1[x]]
nafelez = nonmetals_zarfiat[atomi2[y]]
nafelez_name = nonmetals_name[atomi2[y]]
i = random.randint((len(felez) - felez[1]), len(felez) - 1)
decided_type = int(input("Decide between 1 and 2: "))

if felez[1] == 1:
    answer = felez_name + " " + nafelez_name
else:
    answer = felez_name + '(' + str(roman.toRoman(felez[i])) + ')' + " " + nafelez_name

if atomi2[y] == 81 or atomi2[y] == 683 or atomi2[y] == 782 or atomi2[y] == 783 or atomi2[y] == 1584 or \
        atomi2[y] == 1683 or atomi2[y] == 1684:
    question = felez[0] + str(nafelez[1]) + '(' + nafelez[0] + ')' + str(felez[i])
else:
    question = felez[0] + str(nafelez[1]) + nafelez[0] + str(felez[i])
if nafelez[1] == felez[i]:
    question = felez[0] + nafelez[0]
elif nafelez[1] == 1:
    if atomi2[y] == 81 or atomi2[y] == 683 or atomi2[y] == 782 or atomi2[y] == 783 or atomi2[y] == 1584 or \
            atomi2[y] == 1683 or atomi2[y] == 1684:
        question = felez[0] + '(' + nafelez[0] + ')' + str(felez[i])
    else:
        question = felez[0] + nafelez[0] + str(felez[i])
elif felez[i] == 1:
    question = felez[0] + str(nafelez[1]) + nafelez[0]
elif (felez[i] / nafelez[1]) % 1 == 0:
    if atomi2[y] == 81 or atomi2[y] == 683 or atomi2[y] == 782 or atomi2[y] == 783 or atomi2[y] == 1584 or \
            atomi2[y] == 1683 or atomi2[y] == 1684:
        question = felez[0] + str(nafelez[1] // math.gcd(nafelez[1])) + '(' + nafelez[0] + ')' + \
                   str(felez[i] // math.gcd(nafelez[1], felez[i]))
        if nafelez[1] // math.gcd(nafelez[1], felez[i]) == 1:
            question = felez[0] + '(' + nafelez[0] + ')' + str(felez[i] // math.gcd(nafelez[1]))
    else:
        question = felez[0] + str(nafelez[1] // math.gcd(nafelez[1])) + nafelez[0] + str(
            felez[i] // math.gcd(nafelez[1], felez[i]))
        if nafelez[1] // math.gcd(nafelez[1], felez[i]) == 1:
            question = felez[0] + nafelez[0] + str(felez[i] // math.gcd(nafelez[1]))
elif (nafelez[1] / felez[i]) % 1 == 0:
    if atomi2[y] == 81 or atomi2[y] == 683 or atomi2[y] == 782 or atomi2[y] == 783 or atomi2[y] == 1584 or \
            atomi2[y] == 1683 or atomi2[y] == 1684:
        question = felez[0] + str(nafelez[1] // math.gcd(nafelez[1], felez[i])), '(' + nafelez[0] + ')' + \
                   str(felez[i] // math.gcd(nafelez[1], felez[i]))
        if felez[1] // math.gcd(nafelez[1], felez[1]) == 1:
            question = felez[0] + str(nafelez[1] // math.gcd(nafelez[1], felez[i])) + nafelez[0]
    else:
        question = felez[0] + str(nafelez[1] // math.gcd(nafelez[1], felez[i])), nafelez[0] + \
                   str(felez[i] // math.gcd(nafelez[1], felez[i]))
        if felez[1] // math.gcd(nafelez[1], felez[1]) == 1:
            question = felez[0] + str(nafelez[1] // math.gcd(nafelez[1], felez[i])) + nafelez[0]

if decided_type == 1:
    your_answer = input(question + ": ")
    if your_answer == answer:
        print("yes")
    else:
        print("no", answer)
if decided_type == 2:
    your_answer = input(answer + ": ")
    if your_answer == question or your_answer == felez_name + '(' + str(felez[i]) + ')' + " " + nafelez_name:
        print("yes")
    else:
        print("no", question)
