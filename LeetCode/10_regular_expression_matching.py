# s = "aa"
# p = "a"

s = "aa" 
p = "a*"

model_automato = []

i = 0
indice = 0

while i < len(p):
    character = p[i]
    state = dict()

    if character == "*":
        state.update({p[i - 1]: indice})
    else:
        state.update({character: indice })
        indice += 1

    model_automato.append(state)
    i += 1

model_automato[len(model_automato) - 1].update({"\n" : True})

state = 0

print(model_automato)

for char in s:
    if char in model_automato[state] and state < len(model_automato):
        state = model_automato[state][char]
    else:
        print(False)



