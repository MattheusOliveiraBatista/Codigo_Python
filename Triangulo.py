import os
import time
os.system("cls")
time.sleep(1)

descrição = "DESCRIÇÃO ABAIXO DO ALGORITMO:"

print("\033[1;34m=\033[m"*80)
print(f'\033[1;39m {descrição :>50}\033[m')
print("\033[1;34m=\033[m"*80)

print('''- \033[1;39mInput de 3 Segmentos para formar um Triângulo.\033[m
    - \033[1;39mSe for possível formar um triângulo, classificar em:\033[m
        - \033[1;32mAcutângulo, Retângulo e Obtusângulo\033[m.
        - \033[1;32mEquilátero, Escaleno, Isósceles\033[m.
    - \033[1;39mCaso não seja possível formar um triângulo, enviar a seguinte mensagem:\033[m
        - \033[1;31mOs três segmentos não formam um triângulo\033[m.''')
print("\033[1;34m=\033[m"*80)


def TipoDeTriangulo(a,b,c):
    """
    :param a: Primeiro Segmento
    :param b: Segundo Segmento
    :param c: Terceiro Segmento
    :return:  Retorna a classificação dos tipos  de Triângulo: Retângulo, Acutângulo e Obtusângulo.
    """
    if a*a < b*b + c*c:
        print('\033[1;39mTriângulo\033[m \033[1;31mAcutângulo\033[m e', end= '')
    elif a*a == b*b + c*c:
        print('\033[1;39mTriângulo\033[m \033[1;34mRetângulo\033[m e', end = '')
    elif a*a > b*b + c*c:
        print('\033[1;39mTriângulo\033[m \033[1;33mObtusângulo\033[m e', end = '')


def Escaleno_Equilatero_Isosceles(c, d, e):

    if c == d and d == e:
        print(' \033[1;36mEquilátero\033[m.')

    elif c != d != e != c:
        print('\033[1;36m Isósceles\033[m.')
    else:
        print('\033[1;36m Escaleno\033[m.')


def ConfereTriangulo(a, b, c):
    """
    :param a: Primeiro Segmento
    :param b: Segundo Segmento
    :param c: Terceiro Segmento
    :return: Casos os três parâmetros possa formar um triângulo chama as duas funções, caso não possa, informa
    apenas uma mensagem.
    """
    print(f'\n\033[1;39mOs valores recebidos foram respectivamente:\033[m  \033[1;33m{PrimeiroSegmento}\033[m, \033[1;33m{SegundoSegmento}\033[m, \033[1;33m{TerceiroSegmento}\033[m.')
    if a < b + c and b < c + a and c < b+a:
        print('\033[1;39mOs segmentos informados podem formar um\033[m \033[1;32mTriângulo\033[m!')
        TipoDeTriangulo(PrimeiroSegmento,SegundoSegmento, TerceiroSegmento)
        Escaleno_Equilatero_Isosceles(PrimeiroSegmento,SegundoSegmento, TerceiroSegmento)
    else:
        print('\033[1;39mNão foi possível formar um\033[m \033[1;31mTriângulo\033[m \033[1;39mcom os segmentos informados.\033[m ')



print()
print("\033[1;34m=\033[m"*43)
PrimeiroSegmento = int(input('\033[1;39mDigite o valor para o primeiro segmento:\033[m '))
SegundoSegmento = int(input('\033[1;39mDigite o valor para o segundo segmento:\033[m '))
TerceiroSegmento = int(input('\033[1;39mDigite o valor para o terceiro segmento:\033[m '))
print("\033[1;34m=\033[m"*43)
ConfereTriangulo(PrimeiroSegmento, SegundoSegmento,TerceiroSegmento)
print("\n\033[1;39m============\033[m \033[1;34mPrograma Finalizado\033[m \033[1;39m============\033[m")
print("\033[1;39m=====\033[m \033[1;34mDev. Matheus Batista de Oliveira\033[m \033[1;39m======\033[m")
time.sleep(40)
os.system("cls")


