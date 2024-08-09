cod_fonte = "position = initial+rate*60"
lexema = ""
for i in range(0, len(cod_fonte)):
    if cod_fonte[i].isalpha():
        lexema += cod_fonte[i]
        if cod_fonte[i+1] in ("=","+","*"):
            print("<ID, "+lexema+">")
            lexema = ""
            print("<OP, "+cod_fonte[i+1]+">")
    if cod_fonte[i].isdigit():
        lexema += cod_fonte[i]
print("<NUM, "+lexema+">")    