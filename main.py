
names = ['Tural', 'Cavid', 'Mehriban', 'Rufet']
ages = [1992, 1997, 1998, 1999]


names.append("Tehmine")


names.insert(0, "Zaur")


names.remove("Mehriban")


rufet_index = names.index("Rufet")
print("Rufet-in indeksi:", rufet_index)


print("Oktay listdə var mı?", "Oktay" in names)


names.reverse()
print("Tərs çevrilmiş names:", names)


names.sort()
print("Əlifba sırası ilə names:", names)


ages.sort()
print("Sıralanmış ages:", ages)


s = "IPhone X,IPhone XR"
phones = s.split(",")
print("Telefon listi:", phones)


print("Ən böyük:", max(ages))
print("Ən kiçik:", min(ages))


print("1998-lərin sayı:", ages.count(1998))

ages.clear()
print("Ages təmizləndi:", ages)

brands = []
for i in range(3):
    marka = input("Marka daxil et: ")
    brands.append(marka)
print("Markalar:", brands)

