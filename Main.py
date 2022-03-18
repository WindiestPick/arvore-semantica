from Vaso import Vaso
from Regra import Regras

#FUNÇÃO RECURSIVA RESPONSAVEL POR TENTAR TODAS AS POSSIBILIDADES
#ATÉ NÃO TER MAIS NENHUMA POSSIBILIDADE NOVA POSSIVEL
def testador(memoria, f, cache):
    if (f == 0):
        print("\n\n---------------INICIO---------------- \n\n")

    else:
        vaso1.setVolume(cache[f-1][0])
        vaso2.setVolume(cache[f-1][1])
        memoria = []
        print("Estado Atual :",[vaso1.getVolume(), vaso2.getVolume()])
        print("Resultados Possives : ", end="")
        regras.encheV1()

        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria.append([vaso1.getVolume(), vaso2.getVolume()])
    
        print([vaso1.getVolume(), vaso2.getVolume()], end="")     
        vaso1.setVolume(cache[f-1][0])

        regras.esvaziaV1()
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria.append([vaso1.getVolume(), vaso2.getVolume()])
    
        print([vaso1.getVolume(), vaso2.getVolume()], end="")
        vaso1.setVolume(cache[f-1][0])
        
        regras.encheV2()
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria.append([vaso1.getVolume(), vaso2.getVolume()])
    
        print([vaso1.getVolume(), vaso2.getVolume()], end="")
        vaso2.setVolume(cache[f-1][1])

        regras.esvaziaV2()
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria.append([vaso1.getVolume(), vaso2.getVolume()])
    
        print([vaso1.getVolume(), vaso2.getVolume()], end="")
        vaso2.setVolume(cache[f-1][1])

        regras.despejarV1noV2()
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria.append([vaso1.getVolume(), vaso2.getVolume()])
    
        print([vaso1.getVolume(), vaso2.getVolume()], end="")
        vaso1.setVolume(cache[f-1][0])
        vaso2.setVolume(cache[f-1][1])

        regras.despejarV2noV1()
        if perList(cache, [vaso1.getVolume(), vaso2.getVolume()]):
            cache.append([vaso1.getVolume(), vaso2.getVolume()])
            memoria.append([vaso1.getVolume(), vaso2.getVolume()])
        
        print([vaso1.getVolume(), vaso2.getVolume()], end="")
        vaso1.setVolume(cache[f-1][0])
        vaso2.setVolume(cache[f-1][1])

            
    
        print("\nNovos Resultados : ", end="")
        if memoria == []:
            print("Nenhum novo resultado")
        else:
            print(memoria)
        print('\n-----------------------------------')

    f += 1
    if (len(cache) < f):
        return 0

    return(testador(memoria, f, cache))

    
        
# funão responsavel por percorrer a "cache" e 
#retornar se a possibilidade ja foi encontrada antes
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
memoria = [[0,0]]


testador(memoria, f, cache)


    
