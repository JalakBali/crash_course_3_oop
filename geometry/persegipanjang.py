from geometry.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self,p,l):
        #fungsi yg dipanggil pertama kali saat objek diciptakan
        self.p = p
        self.l = l


    def info(self):
        return f'Persegipanjang, dgn panjang = {self.p} , dan lebar  = {self.l}'


    def luas(self):
        return f'Luas = {self.p * self.l}'