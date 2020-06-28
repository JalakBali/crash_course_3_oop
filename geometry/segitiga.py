from geometry.bangun_ruang import BangunRuang


class SegiTiga(BangunRuang):
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Segitiga, dgn alas = {self.alas} , dan tinggi = {self.tinggi}'

    def luas(self):
        return f'Luas = {self.alas * self.tinggi / 2}'
