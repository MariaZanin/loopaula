palavras_sem_vogais = ""

usuario_palavra = input(('Entre com uma palavra: '))
usuario_palavra = usuario_palavra.upper()

for letra in usuario_palavra:
    if letra == 'A':
        continue
    if letra == 'E':
        continue
    if letra == 'I':
        continue
    if letra == 'O':
        continue
    if letra == 'U':
        continue
    else:
        palavras_sem_vogais += letra
        
print (palavras_sem_vogais)