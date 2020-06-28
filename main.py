from geometry.bangun_ruang import BangunRuang
from geometry.persegipanjang import PersegiPanjang
from geometry.segitiga import SegiTiga

print('menggunakan OOP')
p1 = PersegiPanjang(10,3)
print(p1.info())
print(p1.luas())

s1 = SegiTiga(4,2)
print(s1.info())
print(s1.luas())

print('\nmencoba membuat objek dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.luas())

#polymorphism : kemampuan object utk merespon berbeda, terhadap method pemanggilan yg sama

daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\npolymorphism : kemampuan object utk merespon berbeda, terhadap method pemanggilan yg sama')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())

