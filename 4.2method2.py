# metot(ad, soyad, telefon, görev)
# metot(*parametreler):

def metot(ad, soyad, telefon, görev):
    print(ad,soyad,telefon,görev)


def metot1(*params):
    for i in params:
        print(i)
metot("simge","karademir","1234567","ögrenci")
metot1("simge","karademir","1234567","ögrenci")



def metotvol1(**params):
    print(params["ad"])

metotvol1(ad = "simge", soyad = "karademir",telefon = "1234567",görev = "ögrenci")