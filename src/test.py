
# Function

def sum(value1, value2):
    result = value1 + value2
    print(result)


sum(1, 2)

# For loop

list = (1, 1, 1, 1, 1, 1)
sum = 0

for i in list:
    sum += i
    print('Volta', i, 'do loop. Soma:', sum)

print('Fora do loop', sum)


# Input
teste = int(input("Teste: "))

if teste >= 3:
    print('>= 3')
else:
    print('not >= 3')
