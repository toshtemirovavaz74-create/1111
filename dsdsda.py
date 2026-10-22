yil = int(input("Yilni kiriting: "))

if yil % 400 == 0:
    print(yil, "- kabisa yili.")
elif yil % 100 == 0:
    print(yil, "- kabisa yili emas.")
elif yil % 4 == 0:
    print(yil, "- kabisa yili.")
else:
    print(yil, "- kabisa yili emas.")
    
    
    
    
    summa = float(input("Xarid summasini kiriting: "))
vip = input("VIP mijozmisiz? (ha/yo'q): ").lower()

if summa < 0:
    print("Summa manfiy bo'lishi mumkin emas.")
else:
    if summa <= 100000:
        chegirma = 0
    elif summa <= 500000:
        chegirma = 5
    else:
        chegirma = 10

    if vip == "ha":
        chegirma += 5

    tolov = summa - (summa * chegirma / 100)

    print("Chegirma:", chegirma, "%")
    print("To'lanadigan summa:", tolov, "so'm")
    
