# Enunciado: Crie um programa em Python que pergunta a idade de um usuário e se ele é 
# estudante ou não. O programa deve dizer se a pessoa deve pagar meia entrada ou inteira.
# Para ter direito a meia entrada, a pessoa deve ter menos de 21 OU mais de 65 OU ser estudante. 
# usar While para seguir perguntando até o usuário querer parar

# definir o loop
continuar = 'S' 

# inputs , e tudo no while vai repetir.
while continuar == 'S':
    idade = int(input('\nOlá! Qual a sua idade? '))
    estudante = str(input('Você é um estudante? (S/N) ')).upper()

    # condições
    if idade < 21 or idade > 65:
        meia = True
    elif estudante == 'S':
        meia = True
    else:
        meia = False
        
    print('ANALISANDO.....\n')
    
    # retorno
    if meia:
        print('Você tem direito a meia entrada!')
    else:
        print('Você não tem direito a meia entrada!')

    # a pergunta de continuar
    continuar = str(input('\nVocê deseja continuar verificando? (S/N) ')).upper()

print('Programa encerrado. Obrigada!')