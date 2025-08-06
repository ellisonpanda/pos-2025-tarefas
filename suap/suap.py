import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"
authentication_url = f"{api_url}v2/autenticacao/token/"

user = input("Usuário: ")
password = getpass()

data = {"username": user, "password": password}
response = requests.post(authentication_url, json=data)

token = response.json()['access']
headers = {"Authorization": f'Bearer {token}'}

# Exemplo de requisição autenticada
res = requests.get(f"{api_url}minhas-informacoes/meus-dados/", headers=headers)
print(res.json())
