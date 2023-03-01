#Ex. 05
palavra = str(input('Digite uma palavra: '))
palavra_separar = palavra.split()
palavra_juntar = ''.join(palavra_separar)
palavra_inverso = ''

for letra in range(len(palavra_juntar) -1, -1, -1):
    palavra_inverso += palavra_juntar[letra]
print(f' O inverso de {palavra} é {palavra_inverso}')

#Ex. 02
qtd_termos = int(input('Quantos termos você quer mostrar? '))
termo_1 = 0
termo_2 = 1
contador = 3
seq_fibonacci = [termo_1, termo_2]

while contador <= qtd_termos:
    termo_3 = termo_1 + termo_2
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
    seq_fibonacci.append(termo_3)

num = int(input('Informe um número que deseja saber se está ou não na sequência de Fibonacci: '))

if num in seq_fibonacci:
    print(f'O {num} está na sequência de Fibonacci!')
    print(seq_fibonacci)
else:
    print(f'O {num} não está na sequência de Fibonacci.')

#Ex. 04
faturamento_mensal_total = 67836.43 + 36678.66 + 29229.88 + 27165.48 + 19849.53
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

percentual_de_representacao = {}
for estado, faturamento in faturamento_por_estado.items():
    percentual_de_representacao[estado] = faturamento / faturamento_mensal_total * 100
    
for estado, percentual in percentual_de_representacao.items():
    print(f'{estado}: {percentual:.2f}% do valor total mensal.')

#Ex. 03    
import json

with open('dados.json', 'r') as f:
    faturamento_diario = json.load(f)

faturamento_valido = [f for f in faturamento_diario if f > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

superior_a_media = len([f for f in faturamento_valido if f > media_mensal])

print(f'Menor faturamento: R$ {menor_faturamento:.2f}')
print(f'Maior faturamento: R$ {maior_faturamento:.2f}')
print(f'Número de dias com faturamento acima da média: {superior_a_media}')
