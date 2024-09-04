
palavra_secreta = 'flamengo'
letras_salvas = ''


i_palavra_secreta = len(palavra_secreta)
i_letra_secreta = len(letras_salvas)

i = 0
if i_letra_secreta < i_palavra_secreta:
    while True:
        letra_digitada = input('digite uma letra para adivinhar a palavra: ')
        # letra_atual = palavra_secreta[i]
        if len(letra_digitada) > 1:
            print('digite apenas uma letra.')
            continue

        if letra_digitada in letras_salvas:
            print('voce já digitou essa letra.')
            continue
        if letra_digitada in palavra_secreta:
            letras_salvas += letra_digitada

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_salvas:
                print(letra_secreta)
            else:
                print('*') 
        if letras_salvas == palavra_secreta:
            print('parabens, voce acertou')
            break

    
