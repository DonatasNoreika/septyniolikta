# Sukurkite ir išsibandykite funkcijas, kurios:

# 1. Gražinti trijų paduotų skaičių sumą.

def skaiciu_suma(sk1, sk2, sk3):
    return sk1 + sk2 + sk3

# 2. Gražintų paduoto sąrašo iš skaičių, sumą.

def saraso_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius
    return suma

# 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).

# def didziausias_skaicius(*args):
#     didziausias = args[0]
#     for sk in args:
#         if sk > didziausias:
#             didziausias = sk
#     return didziausias

# arba

def didziausias_skaicius(*args):
    return max(args)


# 4. Gražintų paduotą stringą atbulai.

def stringas_atbulai(stringas):
    return stringas[::-1]


# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.

def info_apie_sakini(stringas):
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios += 1
        if simbolis.islower():
            mazosios += 1
        if simbolis.isnumeric():
            skaiciai += 1
    return (f"Žodžių: {len(stringas.split())}, didžiosios: {didziosios}, mažosios: {mazosios}, skaičiai: {skaiciai}")


# 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.

def unikalus_sarasas(sarasas):
    naujas_sarasas = []
    for skaicius in sarasas:
        if skaicius not in naujas_sarasas:
            naujas_sarasas.append(skaicius)
    return naujas_sarasas


def unique_only(*args):
    return list(set(args))


# 7. Gražintų, ar paduotas skaičius yra pirminis.

def ar_pirminis(skaicius):
    if skaicius > 1:
        for num in range(2, skaicius):
            if skaicius % num == 0:
                return False
        return True
    return False


# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

def isrikiuoti_nuo_galo(sakinys):
    zodziai = sakinys.split()[::-1]
    return " ".join(zodziai)

# 9. Gražina, ar paduoti metai yra keliamieji, ar ne.

import calendar


def ar_keliamieji(metai):
    return calendar.isleap(metai)

# 10. Gražina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.

import datetime


def patikrinti_data(sukaktis, now=datetime.datetime.now()):
    ivesta_data = datetime.datetime.strptime(sukaktis, "%Y-%m-%d %X")
    skirtumas = now - ivesta_data

    metai = skirtumas.days // 365
    menesiai = skirtumas.days // 365 * 12
    savaites = skirtumas.days // 7
    dienos = skirtumas.days
    valandos = skirtumas.total_seconds() // 3600
    minutes = skirtumas.total_seconds() // 60
    sekundes = round(skirtumas.total_seconds())
    return metai, menesiai, savaites, dienos, valandos, minutes, sekundes

