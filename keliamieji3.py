from calendar import isleap


class Keliamieji:
    def tikrinti(self, metai):
        return isleap(metai)

    def diapazonas(self, nuo, iki):
        return list(metai for metai in range(nuo, iki) if isleap(metai))
