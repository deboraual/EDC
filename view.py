from controller import *

def main():
    while True:

     escolha = (int(input('Selecione um exercicio entre 1 a 4 que desja ver primeiro:\n-->')))
     match escolha:
        case 1:
           print('Implemente uma função denominada implica: implica(p, q) ≡ p =⇒ q.')
           valor_p = input('Indique o valor de p (use extritamente v/f) qualquer valor diferente ira ser entendido como none\n')
           valor_q = input('Indique o valor de q (use extritamente v/f) qualquer valor diferente ira ser entendido como none\n')
           valor_p.lower()
           valor_q.lower()

           #-------Verificar valores logicos--------

           if valor_p == 'v':
              p = True
           elif valor_p == 'f':
              p = False
           else:
              print('Valor logico invalido')
              p = None

           if valor_q == 'v':
              q = True
           elif valor_q == 'f':
              q = False
           else:
              print('Valor logico invalido')
              q = None
            
           if p == None or q == None:
              print('Não é possivel realizar o exercicio com valores None')
           else:
              valor_implicacao = resolver_implicacao(p,q)
              if valor_implicacao == True:
                 print(f'o valor {valor_p} => {valor_q} = {valor_implicacao}') 
              else:
                 print(f'O valor {valor_p} => {valor_q} = {valor_implicacao}')
              
        case 2:
           print('Implemente um script que resolva o exercicio 9 g) da série de exercicios de lógica.')
           print('p → q e (p ^ ¬q) → F')
           
           valor_p = input('Indique o valor de p (use extritamente v/f) qualquer valor diferente ira ser entendido como none\n')
           valor_q = input('Indique o valor de q (use extritamente v/f) qualquer valor diferente ira ser entendido como none\n')
           valor_p.lower()
           valor_q.lower()

           #-------Verificar valores logicos--------

           if valor_p == 'v':
              p = True
           elif valor_p == 'f':
              p = False
           else:
              print('Valor logico invalido')
              p = None

           if valor_q == 'v':
              q = True
           elif valor_q == 'f':
              q = False
           else:
              print('Valor logico invalido')
              q = None

           if  p == None or q == None:
              print('Não é possivel realizar o exercicio com valores None')
           else:
              valor_implicacao = resolver_implicacao(p,q)
              exp = not (p and not q) or False
              if  exp == valor_implicacao:
                 print (f' p → q: {valor_implicacao} e (p ^ ¬q) → F: {exp}, como são iguais logo são equivalentes')
              else:
                 print (f' p → q: {valor_implicacao} e (p ^ ¬q) → F: {exp}, como são diferentes logo não são equivalentes')

        case 3:
           print('Implemente uma função que recebe um número inteiro positivo e devolve uma lista com os respetivos fatores primos')
           numero = int(input('Digite um numero:\n-->'))
           fatores = fatores_primo(numero)
           print(f'Os fatores primos de {numero} sao: {fatores}')

        case 4:
           print('Implemente uma função f(x, n) que devolve, caso exista, o inverso de x modulo n.')
           print('Considere que x e n são dois números inteiros positivos tais que x ≤ n.')
           print(' O inverso devolvido pela função deverá pertencer a Zn. Se não existir um tal inverso a função deve devolver uma string a informar disso mesmo.')
           x = int(input('\n Digite um número para x:\n-->'))
           n = int(input('Digite um número para n:\n-->'))
           lista = list(range(0,n))
           inverso = modulo(x,n,lista)

           print(f'O inverso de {x} modulo de {n} = {inverso}')
        case 5:
           print('Trabalho acabado obrigada pela atenção')
           break
        