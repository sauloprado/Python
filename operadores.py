num1 =  input("Dugute o primeiro numero: ")
operador = input("Digite o operador: ")
num2 = input("Digite o segundo numero: ")

if operador == "+":
	resultado = num1 + num2

elif operador == "-":
	resultado = num1 - num2

elif operador == "/":
	resultado = num1 / num2

elif operador == "*":
	resultado = num1 * num2

print (resultado)