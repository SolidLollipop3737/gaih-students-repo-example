
students={}

for i in range(1,6):
    print("Öğrenci",i,"Bilgileri")
    print("*******************")
    adsoyad = str(input("Öğrencinin Adı Soyadı: "))
    asinav = int(input("Öğrencinin Ara Sınavı: "))
    pnotu = int(input("Öğrencinin Proje Notu: "))
    fnotu = int(input("Öğrencinin Final Notu: "))
    gnotu = (asinav * (0.3)) + (pnotu * (0.3)) + (fnotu * (0.4))
    students[i] = {"Ad Soyad": adsoyad, "Ara Sınav": str(asinav),"Proje Notu":str(pnotu),"Final Notu":str(fnotu),"Geçme Notu":str(gnotu)}
sirali_students = sorted(students.items(), key=lambda x: float(x[1]["Geçme Notu"]),reverse=True)
print(sirali_students)
