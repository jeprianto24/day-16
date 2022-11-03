#day 16 ,ngoding cara mengetahui generasi berdasarkan tahun lahir

nama = input("masukkan nama : ")
tahun = int(input("masukan tahun kelahiran : "))

if tahun >= 1912 and tahun <=1950 :
    print("nama anda",nama)
    print("anda lahir pada tahun",tahun)
    print("anda lahir di generasi X(Old)")

elif tahun >= 1951 and tahun <= 1990 :
    print("nama anda",nama)
    print("anda lahir pada tahun",tahun)
    print("anda lahir di generrasi Y(Milenial)")

elif tahun >= 1991 :
    print("nama anda",nama)
    print("anda lahir pada tahun",tahun)
    print("anda lahir di generasi Z(Modern)")
else :
    print("nama anda",nama)
    print("anda lahir pada tahun",tahun)
    print("anda tidak terdaftar di generasi manapun")