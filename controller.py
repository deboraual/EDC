def resolver_implicacao(p,q):

    exp = not p or q
    
    if exp == True:
        return True 
    
    if exp == False:
        return False

def fatores_primo(numero):
    fatores_primos = []
    n = 2 # começa com o menor número primo 

    while numero > 1: #continua ate que o numero seja completamente fatorado 
        if numero % n == 0: #verifica se 2 é um divisor 
            fatores_primos.append(n) #adiciona oa fator primo 
            numero //= n
        else:
            n += 1 #tenta com o procimo numero
    return fatores_primos    

def modulo(x,n,lista):
    for i in lista:
        if(x*i) % n == 0:
            i=+1
        if(x * i) % n == 1:
            return i
             
