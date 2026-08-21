s = "aa" 
p = "a"

model_automato = []

i = 0
indice = 0

while i < len(p):
    character = p[i]
    state = dict()

    if character == "*":
        print("False")
    else:
        indice += 1
        state.update({character: indice })

    model_automato.append(state)
    i += 1

state = 0
for char in s:
    if char in model_automato[state]:
        state = model_automato[state][char]
