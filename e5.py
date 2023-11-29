"""
Taranpreet Kaur
Trishan Mizhquiri
29/11/2023
ASIXc 1B UF1 PR4
Programa que realitza la multiplicació, de dos
nombres sencers,  mitjançant sumes.
"""
numero= int(input())
numerosuma=int(input())
for x in range(numerosuma):
    for j in range(numero):
        print(x,j,x+j)