s = "aa" 
p = "a"

automato = []

indice = 1
i = 0

#create automato
while i < len(p):
    character = p[i]
    automato.append([(character, indice)])
    indice += 1
    i += 1

automato.append([("/n", indice)])

apontador = 0

for character in s:
    for tupla in automato[apontador]:
        if character == tupla[0]:

