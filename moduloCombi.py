

def variacionesNoRep(m, n):
    resu = 1

    for i in range(n):
        resu *= m - i
    # return resu
    print ("")
    print("Existen ",resu,"formas de crear grupos de",n,"elementos de un total de",m,"sin repetir elementos.")
    print ("")