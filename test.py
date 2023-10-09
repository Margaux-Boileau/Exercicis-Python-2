import csv
import consts


# Name;Team;Position;Heigth;Weigth;Age

header = []
llista_diccionaris = []
f = open("basket_players.csv")
for i, fila in enumerate(f):
 if (i == 0):
    header = fila[0:-1].split(";")
 else:
    element = fila[0:-1].split(";")
    item = {}
    for x, zone in enumerate(header):
        item[zone] = element[x]
    llista_diccionaris.append(item)
f.close()

#ex 2
text= ["NOM","EQUIP","POSICIO","ALTURA","GRUIX","EDAT"]
trad = {"Point Guard":"Base", "Shooting Guard":"Escorta", "Small Forward":"Aler", "Power Forward":"Ala-pivot", "Center":"Pivot"}
newF = open("jugadors_basket.csv", "w")


writer = csv.DictWriter(newF, fieldnames=text, delimiter="^", lineterminator="\n")
writer.writeheader()
writer.fieldnames = header

for index, dct in enumerate(llista_diccionaris):
    dct['Position'] = trad[dct['Position']]
    dct['Heigth'] = round(float(dct['Heigth'])* consts.inch_to_cm, 2)
    dct['Weigth'] = round(float(dct['Weigth']) * consts.lbs_to_kgs, 2)
    dct['Age'] = int(float(dct['Age'])) #libertades artisticas
    writer.writerow(dct)
newF.close()

#ex3
heaviest = llista_diccionaris[0]
shortest = llista_diccionaris[0]
info_equip = {"nom":"", "count":0, "pes":0, "alt":0}
num_posicions = {}
equips = {}

for dct in llista_diccionaris:
    
    if (dct["Position"] not in num_posicions.keys()):
        num_posicions[dct["Position"]] = 1
    else:
       num_posicions[dct["Position"]] += 1

    if (dct["Team"] not in equips.keys()):
       equips[dct["Team"]] = {"count":0, "pes":0, "alt":0}
    equips[dct["Team"]]["count"] += 1
    equips[dct["Team"]]["pes"] += dct["Weigth"]
    equips[dct["Team"]]["alt"] += dct["Heigth"]

    if (dct["Weigth"] > heaviest["Weigth"]):
        heaviest = dct
    if (dct["Heigth"] < shortest["Heigth"]):
        shortest = dct
    

print(equips)