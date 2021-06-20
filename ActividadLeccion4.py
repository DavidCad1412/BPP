lista=[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

for i in lista:
    maxi = max(i)
    print('Valor Maximo:', maxi)
    mini = min(i)
    print('Valor Minimo:', mini)
    
    
"""
################################################################
################################################################
################################################################
"""
def es_primo(n):
    es_primo = True
    if(n % 2 ==0):
            es_primo = False
    return es_primo
    
lista2 =  [3, 4, 8, 5, 5, 22, 13]
   

prim = list(filter(es_primo, lista2))
print (prim)
              
