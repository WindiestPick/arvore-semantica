from Vaso import Vaso
from Regra import Regras

def testador(memoria, f, cache):
    regras.encheV1()
    if ([vaso1.getVolume(), vaso2.getVolume()] != memoria[f]):
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria[f].append(testador(memoria, f, cache))
            f += 1
            regras.esvaziaV1

    regras.esvaziaV1()
    if ([vaso1.getVolume(), vaso2.getVolume()] != memoria[f]):
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria[f].append(testador(memoria, f, cache))
            f += 1
            regras.esvaziaV1
        
    regras.encheV2()
    if ([vaso1.getVolume(), vaso2.getVolume()] != memoria[f]):
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria[f].append(testador(memoria, f, cache))
            f += 1
            regras.esvaziaV2

    regras.esvaziaV2()
    if ([vaso1.getVolume(), vaso2.getVolume()] != memoria[f]):
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria[f].append(testador(memoria, f, cache))
            f += 1
            regras.esvaziaV2
        
    regras.despejarV1noV2()
    if ([vaso1.getVolume(), vaso2.getVolume()] != memoria[f]):
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria[f].append(testador(memoria, f, cache))
            f += 1
            regras.esvaziaV2
            regras.esvaziaV1

    regras.despejarV2noV1()
    if ([vaso1.getVolume(), vaso2.getVolume()] != memoria[f]):
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria[f].append(testador(memoria, f))
            f += 1
            regras.esvaziaV1
            regras.esvaziaV2

    return memoria
        
    
def perList(list, x):
    for i in range(len(list) - 1):
        if (x == list[i]):
            return False
    return True


#______Cria o objeto vaso_________
vaso1 = Vaso()
vaso1.setLimite(3)
vaso1.setVolume(0)

vaso2 = Vaso()
vaso2.setLimite(4)
vaso2.setVolume(0)

#_______Cria as Regras_____________
regras = Regras()
regras.setVaso1(vaso1)
regras.setVaso2(vaso2)


#____________Execução______________
f = 0
cache = [[0,0]]
memoria = []
memoria.append([0,0])


result = testador(memoria, f, cache)

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[j])
    
