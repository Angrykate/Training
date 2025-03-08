def nuke(n):
    a = []
    for i in range(10):
        if n > 1:
            a.append(nuke(n - 1))
        else:
            a.append(i)
    return a

mini_Tsar = nuke(3)
Hiroshima = nuke(2)
atomic = nuke(1)

def compter_elements(liste):
    if isinstance(liste, list):
        return sum(compter_elements(elem) for elem in liste)
    else:
        return 1

print(compter_elements(mini_Tsar))
