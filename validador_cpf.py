cpf = input('Digite seu CPF: ')
nove_digitos = cpf[:9]
cont1 = 10
res_digito1 = 0

for digito in nove_digitos:
    res_digito1 += int(digito) * cont1
    cont1 -= 1
digito_10 = (res_digito1 * 10) % 11
digito_10 = digito_10 if digito_10 <= 9 else 0

dez_digitos = nove_digitos + str(digito_10)
cont2 = 11
res_digito2 = 0

for digito in dez_digitos:
    res_digito2 += int(digito) * cont2
    cont2 -= 1
digito_11 = (res_digito2 * 10) % 11
digito_11 = digito_11 if digito_11 <= 9 else 0

cpf_final = f'{nove_digitos}{digito_10}{digito_11}'

if cpf == cpf_final:
    print(f'{cpf_final} é válido.')
else:
    print('CPF inválido')