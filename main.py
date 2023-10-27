import re

def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Erreur : Division par zéro"
    return x / y

def main():
    while True:
        print("Options:")
        print("Entrez 'add' ou '+' pour additionner deux nombres")
        print("Entrez 'sub' ou '-' pour soustraire deux nombres")
        print("Entrez 'mul' ou '*' pour multiplier deux nombres")
        print("Entrez 'div' ou '/' pour diviser deux nombres")

        user_input = input("> ")

        if user_input not in ('add', 'sub', 'mul', 'div', '+', '-', '*', '/'):
            print("Option non valide!")
            continue

        num1 = input("Entrez le premier nombre: ")
        puissance_match = re.match(r'(\d+)²', num1)
        if puissance_match:
            base = float(puissance_match.group(1))
            num1 = base ** 2
        else:
            num1 = float(num1)

        num2 = input("Entrez le deuxième nombre: ")
        puissance_match = re.match(r'(\d+)²', num2)
        if puissance_match:
            base = float(puissance_match.group(1))
            num2 = base ** 2
        else:
            num2 = float(num2)

        if user_input == "add" or user_input == "+":
            print("Le résultat de l'addtion est", addition(num1, num2))
        elif user_input == "sub" or user_input == "-":
            print("Le résultat de la soustraction est", soustraction(num1, num2))
        elif user_input == "mul" or user_input == "*":
            print("Le résultat de la multiplication est", multiplication(num1, num2))
        elif user_input == "div" or user_input == "/":
            print("Le résultat est de la division", division(num1, num2))

        print("Voulez-vous effectuer une autre opération ? 'yes' ou 'no'")
        user_input = input("> ")

        if user_input == "no":
            break

main()
