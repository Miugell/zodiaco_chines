def zodiaco(ano):
     signo = ['Rato', 'Búfalo', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Cabra', 'Macaco', 'Cão', 
              'Galo', 'Javali']
     ano_base = 1900
     diferenca = ano - ano_base
     animal = diferenca % 12
     
     zodiaco = signo[animal]
     return zodiaco


ano = int(input("Digite o ano que você nasceu: "))
resultado = zodiaco(ano)
print(f"O seu ano de nascimento corresponde ao signo {resultado}" )