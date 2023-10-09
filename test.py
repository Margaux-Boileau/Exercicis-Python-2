import csv
import consts
import json
import matplotlib.pyplot as plt

#FUNCIONS
def graph(list_x, list_y, label_x, label_y, title, file):
        plt.bar(list_x, list_y)
        plt.xlabel(label_x)
        plt.ylabel(label_y)
        plt.title(title)
        plt.savefig(file)

def cvs_to_json(list, output_file, indent):
    f_json= open(output_file, 'w')
    json.dump(list, f_json, indent=indent)
    f_json.close()

def cvs_to_list_of_dictionaries(cvs_file):
    header = []
    llista_diccionaris = []
    f = open(cvs_file)
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
    return llista_diccionaris

# EXERCICI 1
llista_diccionaris = cvs_to_list_of_dictionaries("basket_players.csv")

text = ["NOM", "EQUIP", "POSICIO", "ALTURA", "GRUIX", "EDAT"]
trad = {"Point Guard": "Base", "Shooting Guard": "Escorta", "Small Forward": "Aler", "Power Forward": "Ala-pivot", "Center": "Pivot"}

newF = open("jugadors_basket.csv", "w")
writer = csv.DictWriter(newF, fieldnames=text, delimiter="^", lineterminator="\n")
writer.writeheader()
writer.fieldnames = llista_diccionaris[0].keys()

for dct in llista_diccionaris:
    dct['Position'] = trad[dct['Position']]
    dct['Heigth'] = round(float(dct['Heigth']) * consts.inch_to_cm, 2)
    dct['Weigth'] = round(float(dct['Weigth']) * consts.lbs_to_kgs, 2)
    dct['Age'] = round(float(dct['Age']))
    writer.writerow(dct)
newF.close()

# EXERCICI 2
heaviest = llista_diccionaris[0]
shortest = llista_diccionaris[0]
num_posicions = {}
equips = {}
edats = {}

for dct in llista_diccionaris:
    # Pes mes alt i altura mes baixa
    if (dct["Weigth"] > heaviest["Weigth"]):
        heaviest = dct
    if (dct["Heigth"] < shortest["Heigth"]):
        shortest = dct

    # Membres, pes i alçada total per equip.
    try:
       equips[dct["Team"]]["count"] += 1
       equips[dct["Team"]]["pes"] += dct["Weigth"]
       equips[dct["Team"]]["alt"] += dct["Heigth"]
    except:
        equips[dct["Team"]] = {"count": 0, "pes": 0, "alt": 0}
    
    # Recompte de jugadors per posició.
    try:
        num_posicions[dct["Position"]] += 1
    except:
        num_posicions[dct["Position"]] = 1

    # Distribució de jugadors per edat.
    try:
        edats[dct["Age"]] += 1
    except:
        edats[dct["Age"]] = 1

# Mitjana pes i alçada per equip.
for equip in equips.keys():
    equips[equip]["pes"] = round(equips[equip]["pes"]/equips[equip]["count"], 2)
    equips[equip]["alt"] = round(equips[equip]["alt"]/equips[equip]["count"], 2)

# PRINTS
print("Heaviest:", heaviest["Name"])
print("\nShortest:", shortest["Name"])

print("\nMITJANA PES I ALÇADA PER EQUIP:")
for nom, info in equips.items():
    print(nom, ":")
    print("Pes:", info["pes"])
    print("Alçada:", info["alt"])

print("\nJUGADORS PER POSICIÓ:")
for pos, num in num_posicions.items():
    print(pos, ":", num)

print("\nJUGADORS PER EDAT:")
for edat, num in edats.items():
    print(num, "jugadors de", edat, "anys")

# EXERCICI 3
cvs_to_json(llista_diccionaris, 'jugadors_basket.json', 4)

# GRAFICA EDATS
graph(list(edats.keys()), list(edats.values()), "Edats", "Nombre de jugadors", "Nombre de jugadors per edat", "edats.png")

