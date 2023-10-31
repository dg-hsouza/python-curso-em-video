# Refaça o EX035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais / Isósceles: dois lados iguais / Escaleno: todos os lados diferentes

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if s1 == s2 and s1 == s3:
        print('Tipo do triângulo: EQUILÁTERO')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('Tipo do triângulo: ESCALENO')
    else:
        print('Tipo do triângulo: ISÓSCELES')
else :
    print('Os segmento acima NÃO PODEM FORMAR triângulo')

