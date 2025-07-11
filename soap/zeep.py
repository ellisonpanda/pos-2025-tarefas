# zeep.py
from zeep import Client

def main():
    # Exemplo de WSDL: serviço de conversão de temperatura
    wsdl = 'https://www.w3schools.com/xml/tempconvert.asmx?WSDL'
    client = Client(wsdl=wsdl)

    # Converter Celsius para Fahrenheit
    celsius = '36'
    fahrenheit = client.service.CelsiusToFahrenheit(celsius)
    print(f"{celsius}°C → {fahrenheit}°F")

    # Converter Fahrenheit para Celsius
    fahrenheit2 = '98.6'
    celsius2 = client.service.FahrenheitToCelsius(fahrenheit2)
    print(f"{fahrenheit2}°F → {celsius2}°C")

if __name__ == '__main__':
    main()
