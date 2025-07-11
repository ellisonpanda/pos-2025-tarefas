# cliente.py
import requests

API_URL = 'http://127.0.0.1:5000/users'

def listar():
    r = requests.get(API_URL)
    print("=== Usuários ===")
    for u in r.json():
        print(f"{u['id']}: {u['nome']} – {u['email']}")

def criar(nome, email):
    r = requests.post(API_URL, json={"nome": nome, "email": email})
    print("Criado:", r.json())

def ver(id):
    r = requests.get(f"{API_URL}/{id}")
    print("Detalhes:", r.json() if r.status_code == 200 else "Não encontrado")

def atualizar(id, nome=None, email=None):
    data = {}
    if nome: data['nome'] = nome
    if email: data['email'] = email
    r = requests.put(f"{API_URL}/{id}", json=data)
    print("Atualizado:", r.json())

def deletar(id):
    r = requests.delete(f"{API_URL}/{id}")
    print("Deletado" if r.status_code == 204 else "Não encontrado")

if __name__ == '__main__':
    listar()
    criar("Carol", "carol@example.com")
    listar()
    ver(3)
    atualizar(3, nome="Carolina")
    ver(3)
    deletar(3)
    listar()
