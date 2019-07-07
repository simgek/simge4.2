def decorator_metot(metot):
    def sarmal_metot():
        print("sarmal metodu {}'dan önce tetiklendi".format(metot.__name__))
        return metot()
    return sarmal_metot

@decorator_metot
def print_metot():
    print("print_metot çalıştı")

print_metot()
