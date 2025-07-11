
from zeep import Client

def main():
    wsdl = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL'
    client = Client(wsdl=wsdl)

    num = 12345
    result = client.service.NumberToWords(ubiNum=num)
    print(f"Número {num} por extenso: {result}")


    val = 987.65
    money = client.service.NumberToDollars(dNum=val)
    print(f"{val} em dólares: {money}")

if __name__ == '__main__':
    main()
