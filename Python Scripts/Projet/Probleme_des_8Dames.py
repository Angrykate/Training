def case_libre(list_dame):

    position = [(len(list_dame),i) for i in range(8)]
    position_valide = []
    for i in position:
        test = True
        for j in list_dame:
            if i[1] == j[1]:
                test = False
            elif abs((i[0]-j[0])/(i[1]-j[1])) == 1:
                test = False

        if test:
            position_valide.append(i)

    return position_valide
nombre = 0
def position_dames(list_dame=[]):


    global nombre
    for i in case_libre(list_dame):
        if len(list_dame) == 7:
            print(list_dame + [i])
            nombre+=1
        else:
            position_dames(list_dame + [i])


position_dames()
print("\nIl y a",nombre,"solutions possibles")