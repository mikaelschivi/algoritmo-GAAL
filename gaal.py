#!/usr/bin/env python3

mat = input('insira seu numero de matricula: ')
smat = [int(c) for c in mat]
smat = sum(smat)

def calculo(s1, n) -> int:
        if s1%31 == 0:
                s1 = s1/31
        return int( (s1*n)%31 )

print(f'\nNumero de matricula: {mat}')
for i in range(1,5):
        print(f'Questao {i}: {calculo(smat,i)}')