def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    while True:
        print("\nEscolha a conversão desejada:")
        print("1. Celsius para Fahrenheit")
        print("2. Celsius para Kelvin")
        print("3. Fahrenheit para Celsius")
        print("4. Fahrenheit para Kelvin")
        print("5. Kelvin para Celsius")
        print("6. Kelvin para Fahrenheit")
        print("0. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '0':
            print("Saindo do programa.")
            break

        if escolha in ['1', '2', '3', '4', '5', '6']:
            temperatura = float(input("Digite a temperatura: "))
            if escolha == '1':
                resultado = celsius_to_fahrenheit(temperatura)
                print(f"{temperatura} °C é igual a {resultado:.2f} °F")
            elif escolha == '2':
                resultado = celsius_to_kelvin(temperatura)
                print(f"{temperatura} °C é igual a {resultado:.2f} K")
            elif escolha == '3':
                resultado = fahrenheit_to_celsius(temperatura)
                print(f"{temperatura} °F é igual a {resultado:.2f} °C")
            elif escolha == '4':
                resultado = fahrenheit_to_kelvin(temperatura)
                print(f"{temperatura} °F é igual a {resultado:.2f} K")
            elif escolha == '5':
                resultado = kelvin_to_celsius(temperatura)
                print(f"{temperatura} K é igual a {resultado:.2f} °C")
            elif escolha == '6':
                resultado = kelvin_to_fahrenheit(temperatura)
                print(f"{temperatura} K é igual a {resultado:.2f} °F")
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
