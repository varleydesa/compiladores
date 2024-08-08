codigo_fonte = "position=initial+rate+alfa*beta*60+78"
variavel = ""
numero = ""
contador = 0
for i in range(len(codigo_fonte)):
    if codigo_fonte[i].isalpha():
        variavel += codigo_fonte[i]
    elif (codigo_fonte[i] in ("*" , "=" , "+")):
            if codigo_fonte[i-1].isalpha():
                contador += 1
                print ("<VAR, "+str(contador)+">")
                variavel =""
            print("<OP, "+codigo_fonte[i]+">")
    elif codigo_fonte[i].isdigit():
        numero += codigo_fonte[i]
print("<NUM, "+numero+">")