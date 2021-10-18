def isPrime(x):
    '''
    functia verifica daca un numar dat este prim sau nu
    :param x: numar intreg
    :return: True daca nr este prim, sau False in caz contrar
    '''

    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

def testisPrime():
    assert isPrime(3) is True
    assert isPrime(5) is True
    assert isPrime(6) is False

def eliminaNrPrime(l):
    '''
    functia elimina din lista nr care sunt prime
    :param l: lista de nr intregi
    :return: afiseaza lista cu nr care nu sunt prime din lista
    '''
    rezultat=[]
    for x in l:
        if isPrime(x)==False:
            rezultat.append(x)
    return rezultat

def testeliminaNrPrime():

    assert eliminaNrPrime([3,4,5])==[4]
    assert eliminaNrPrime([3,5,6,8])==[6,8]
    assert eliminaNrPrime([3,7,8])==[8]

def mediaAritmetica(l,n):
    '''
    functia verifica daca media aritmetica a nr din lista este mai mare decat un nr dat n
    :param l: lista de nr intregi
    :param n: numar intreg
    :return: DA, daca media aritmetica a nr din lista este mai mare decat n, sau NU, in caz contrar
    '''
    suma=0
    for i in range(0,len(l)):
        suma=suma+l[i]
    media=suma//(len(l))
    if media > n:
        return True
    else:
        return False

def testmediaAritmetica():

    assert mediaAritmetica([3,4,5],3) is True
    assert mediaAritmetica([4,6],4) is True
    assert mediaAritmetica([3,4,5],5) is False

def AdaugaNrDivProprii(l):
    '''
    adauga nr de divizori proprii ai unui nr dupa acesta
    :param l: lista de nr intregi
    :return: lista cu nr de divizori adaugat dupa fiecare element
    '''

    rezultat=[]
    for x in l:
        rezultat.append(x)
        nr=0
        for i in range(2,x//2+1):
            if x%i==0:
                nr=nr+1
        rezultat.append(nr)
    return rezultat

def testAdaugaNrDivProprii():

    assert AdaugaNrDivProprii([3,7])==[3,0,7,0]
    assert AdaugaNrDivProprii([19,5])==[19,0,5,0]

def tupluNr(l):
    '''
    functia returneaza lista obtinuta din lista inițială în care numerele sunt înlocuite cu un tuplu în care pe
    prima poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia
    poziție apare numărul de apariții a numărului.
    :param l: lista de nr intregi
    :return: lista modificata
    '''

    rezultat=[]
    i=-1
    for x in l:
        nr=0
        i=i+1
        for j in l:
            if x==j:
                nr=nr+1
        tuplu=(x,i,nr)
        rezultat.append(tuplu)
    return rezultat

def testtupluNr():

    assert tupluNr([25, 13, 26, 13])==[(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]


def printMenu():
    print("1.Citire.")
    print("2. Elimina nr prime din lista.")
    print("3. Verifica daca media aritmetica este mai mare decat un nr dat.")
    print("4. Adauga dupa fiecare element nr de divizori proprii ai acestuia ")
    print("5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu.")
    print("6.Iesire")

def citireListe():
    l=[]
    n=int(input("Dati numarul de elemente din lista: "))
    for i in range(n):
        l.append(int(input("l["+ str(i) + "]=")))
    return l

def main():
    testisPrime()
    testeliminaNrPrime()
    testmediaAritmetica()
    testAdaugaNrDivProprii()
    testtupluNr()
    l=[]
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l=citireListe()
            printMenu()
            optiune=input("Alegeti optiunea: ")
            if optiune == "2":
              print(eliminaNrPrime(l))
            elif optiune == "3":
              n=int(input("Dati un nr: "))
              print(mediaAritmetica(l,n))
            elif optiune=="4":
                print(AdaugaNrDivProprii(l))
            elif optiune=="5":
                print (tupluNr(l))
            elif optiune == "6":
                break
        else:
            print("Optiune gresita! Reincercati!")

main()