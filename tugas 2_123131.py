# menghitung volume dan luas tabung

pi = 22/7
r = int(input("masukkan r tabung:"))
tinggi = int(input("masukkan tinggi tabung:"))

volumetabung = pi*r*r*tinggi
luastabung = 2*pi*r*(r+tinggi)

print("volume tabung tersebut adalah:", volumetabung)
print("luas tabung tersebut adalah:", luastabung)
