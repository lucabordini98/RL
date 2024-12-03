import mtgsdk

sets = mtgsdk.Set.all()
def testMtgSdk():# Ottieni una lista di tutti i set di carte
    # Stampa il nome di ogni set
    for s in sets:
        print(s.name)

if __name__ == '__main__':
    testMtgSdk()
