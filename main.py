#!/usr/bin/python3

import recopila as rec
import random as rd
import colorama as C


def verify(wort, the):
    '''
    retorna un boolea si esta correcto o mal
    '''
    if wort == (the +" "+ wort[4:]):
        print(C.Fore.GREEN + ">>>" + C.Fore.RESET)
        return True

    else:
        if wort[1].upper() == "I":
            print(C.Fore.RED + f"!!! --{wort}" + C.Fore.RESET)
            return False
            
        elif wort[1].upper() == "E":
            print(C.Fore.CYAN + f"!!! --{wort}" + C.Fore.RESET)
            return False

        elif wort[1].upper() == "A":
            print(C.Fore.GREEN + f"!!! --{wort}" + C.Fore.RESET)
            return False

def menu(dic):
    print("aprende Aleman")
    print("1. DIE, DER, DAS")
    print("2. Traducir SP -ALE")
    print("3. Traducir ALE -sP")
    option = int(input("escoge: "))


    if option == 1:
        op1(dic)
    elif option ==2:
        op2(dic)
    elif option ==3:
        op3(dic)

    else:
        print("numero incorrecto")
        menu(dic)

def op2(dic):#sp a aleman  {"ap":"aleman"}
    i,corect,fail,flow = varis()
    value_l = dic_l(dic)
    while flow:
        tupl = rd.choice(value_l)
        word_ale = tupl[1]
        word_ep = tupl[0]
        antwort = input(f"{word_ep}:").upper()
        if traductor_ale(word_ep,word_ale,antwort):
            corect += 1
        else:
            fail += 1

        i, flow = qsalir(i)
    printer(corect,fail)


def op3(dic):
    i,corect,fail,flow = varis()
    value_l = dic_l(dic)
    while flow:
        tupl = rd.choice(value_l)
        word_ale = tupl[1]
        word_ep = tupl[0]
        antwort = input(f"{word_ale}:").upper()
        if traductor_sp(word_ep,word_ale,antwort):
            corect += 1
        else:
            fail += 1

        i, flow = qsalir(i)
    printer(corect,fail)

def traductor_ale(sp,ale, rep):
    if rep == ale.upper():
        print(f">>>")
        return True
    else:
        print(f"!!!---{sp} : {ale}")
        return False

def traductor_sp(sp,ale, rep):
    if rep == sp.upper():
        print(f">>>")
        return True
    else:
        print(f"!!!---{ale} : {sp}")
        return False

def dic_l(dic):
    value_l = list(dic.items())  #[(espanol,aleman),(b,2)]
    return value_l

def varis():
    ite = 0
    corrt = 0
    fallo = 0
    seguir = True
    return ite,corrt,fallo, seguir

def op1(dic):
    print("di si es DAS, DER, DIE")
    #rd.randint(0,len(dic))
    #tem = dic.items()
    #for key, value in dic.items():
    #key = rd.choice(dic)  #key Espanol
    l_error = []
    i,corect,fail,flow = varis()
    value_l = dic_l(dic)
    while flow:
        tupl = rd.choice(value_l)
        word_ale = tupl[1]
        word_ep = tupl[0]
        #f"{word_ep} :  ___ {word_ale[4:-1]} :"
        art = str(input(f"___ {word_ale[4:]}:{word_ep}:")).upper()
        if verify(word_ale,art):
            corect += 1
        else:
            fail += 1
        i += 1
        i, flow = qsalir(i,corect,fail)
    printer(corect,fail)     

def printer(corr, fail):
    print("---")
    print(f"--correctos >>>>{corr}")
    print(f"inccorrectos !!!{fail}")

    print(f"has respondido un :{(100*corr/(corr + fail))}%  bien")


def qsalir(iter,ok,fail ):
    if iter == 10:
            printer(ok, fail)
            option = str(input("queires seguir:(y-/n) ")).upper()
             
            if (option == "") or (option[0] == "Y"):
                return 0,True
            return iter,False

    return iter, True


def main(doc):
    dic = rec.reader(doc)
    menu(dic)

#run menu
temas = ["T1.txt", "T2.txt","T3.txt" ]
n =  int(input("Tema? "))
if (n == 1):
    main(temas[n-1],)
if (n == 2):  
    main(temas[n-1])
if (n == 3):
    main(temas[n-1])
