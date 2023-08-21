# Usando loop com laço de repetição for;

for (let andar=20; andar>=1; andar--)  {
    if (andar === 13) continue;
	console.log(andar);
}

# Usando loop com a função range:

for numero in range(20, 0, -1):
    if numero == 13:
        continue
    print("Você está no", numero, "andar!")

# Usando loop com laço de repetição While;

numero = 21
while (numero >= 1):
    numero -= 1
    if numero == 13:
        continue
    print("Você está no", numero, "andar!")