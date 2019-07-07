def kayıtlar(**params):
    print("-"*25)
    for key,value in params.items():
        print("{0:<8}:{1}".format(key,value))
    print("-"*25)

kayıtlar(ad = "simge", soyad = "karademir",telefon = "1234567",görev = "ögrenci")