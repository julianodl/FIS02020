#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Funções
# - Funçoes retornam um único objeto.
# - sintaxe:
# def <nome_da_função>(arq1, arq2,...):
#     <corpo_da_função>

# Exemplo 1:
def sayHello():
    '''diz Hello!'''
    print("Hello!!")

r = sayHello()
print(f'r = {r}')

# Exemplo 2:
def quadrado(x):
    '''retorna o quadrado de x'''
    return x**2
x2 = 5
y2 = quadrado(x2)
print(f'O quadrado de {x2} é {y2}.')

# Exemplo 3:

def soma(a, b, c):
    '''soma 3 números'''
    s = a + b + c
    return s

A = 10
B = 15
C = 17
y3 = soma(A, B, C)
print(f'{A} + {B} + {C} = {y3}')

#%% Argumentos posicionais
def soma(a, b, c):
    '''soma 3 números'''
    s = a + b + c
    return s

y1 = soma(10,20, 30)
print(y1)

y2 = soma(30, 10, 20)
print(y2)

#%% Argumentos com palavras-chave
# (keyword)
def p(a, b, c):
    '''retorna a + b**2 + c**3'''
    return a + b**2 + c**3

print()
y1 = p(10, 20, 30)
print(y1)

y2 = p(30, 10, 20)
print(y2)

y3 = p(c=30, a=10, b=20)
print(y3)

#%% Argumentos posicionais + 
#   argumentos com palavras-chave

print()
print( p(30, 10, c=30))
#print( p(a=30, 10, 20)) #erro
#print( p(30, b=10, 30)) #erro

#%% Paramentros com valores
#   padrões (default)(defeito)

def potencia(x, n=2):
    '''retorna x**n'''
    return x**n
print()
print(potencia(2, 3))
print(potencia(2))

#%% Forçando o uso de palavras-chave

def q(a, *, b=0, c=0):
    '''retorna a + b**2 + c**3'''
    return a + b**2 + c**3

print()
#print(q(10, 20, 30))
print(q(10,b=20, c=30))
print(q(10,c=30, b=20))
print(q(a=10,c=30, b=20))

print(q(10))

#%% Passando uma lista como argumento

# Exemplo 1:
def lsitar_elementos(lista):
    '''lista os elementos da
    lista "lista" '''
    for elemento in lista:
        print(elemento)

Lista = ['alpha', 'beta', 'gamma', 'delta']

lsitar_elementos(Lista)


#%% Exemplo 2:
def p(a, b, c):
    '''retorna a + b**2 + c**3'''
    return a + b**2 + c**3

lista = [10, 20, 30]
print(lista)
print(*lista) # *: op. de desempacotamento

#print( p(lista)) #erro
print( p(*lista))

#%% Passando um dicionário como argumento
#  de uma função

def p(a, b, c):
    '''retorna a + b**2 + c**3'''
    return a + b**2 + c**3

args = dict(a=10, b=20, c=30)
#args = ('a':10, 'b':20, 'c':30) #alternativa

print()
print(args)
print(*args)

print(p(**args))

#%% Passando um número arbitrário
#   de argumentos para uma função

def media3(a, b, c):
    '''retorna a média de a, b, c'''
    return (a + b + c)/3

def media(*valores):
    '''retorna a média de n valores'''
    #soma = 0
    #for x in valores:
    #    soma += x
    soma = sum(valores)
    n = len(valores)
    med = soma / n
    return med

print()
print(media3(10, 22, 25))
print(media(10, 20, 30, 40))

#%% Variáveis locais e globais

v = 123
G = 777
T = 222

def foo():
    global G
    v = 500
    G = 111
    print(f'foo(): {v} {G} {T}')
    
print()    
print(f"valor de v, G ANTES: {v} {G}")
foo()
print(f"valor de v, G DEPOIS: {v} {G}")