salario = float(input('Digite seu salário:'))

if salario <= 1903.98:
    print(f'Isento de IRFF')
    print(f'Seu salário: {salario}')

elif salario <= 2826.66:
    print(f'Desconto de R$ 142,80')
    print(f'Seu salário com desconto é: {salario - 142.80}')

elif salario <= 3751.06:
    print(f'Desconto de R$ 354,80')
    print(f'Seu salário com desconto é: {salario - 354.80}')

elif salario <= 4664.68:
    print(f'Desconto de R$ 636,13')
    print(f'Seu salário com desconto é: {salario - 636.13}')

else:
    print(f'Desconto de R$ 869,36')
    print(f'Seu salário com desconto é: {salario - 869.36}')
