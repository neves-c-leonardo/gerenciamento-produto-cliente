import requests

# URL da API do json-server
url = 'http://localhost:3000/clientes'

class ClientesApiService:
    
    # Fazendo a requisição GET
    def buscarClientes(self):
        response = requests.get(url)

        if response.status_code == 200:
            clientes = response.json()
            return clientes
        else:
            print('Erro ao acssar a API:', response.status_code)

    # GET com parametro
    def buscarCliente(self, id=None, nome=None):
        if id is not None and nome is not None:
            response = requests.get(f"{url}?id={id}&nome={nome}")
        elif id is not None:
            response = requests.get(f"{url}/{id}")
        elif nome is not None:
            response = requests.get(f"{url}?nome={nome}")
        else:
            return self.buscarClientes()

        if response.status_code == 200:
            cliente = response.json()
            return cliente
        else:
            print('Erro ao acssar a API:', response.status_code)

    # Post sendo enviado o body JSON
    def adicionarCliente(self, nome, cpf, endereco):
        novo_cliente = {"nome": nome, "cpf": cpf, "endereco": endereco}
        response = requests.post(url, json=novo_cliente)

        if response.status_code == 201:
            print(f"{nome} foi adicionado a lista de clientes")
        else:
            print('Erro ao adicionar o cliente:', response.status_code)

    # Put sendo enviado o body JSON
    def alterarCliente(self, id, nome, cpf=None):
        cliente_atualizado = {"nome": nome}
        
        if cpf is not None:
            cliente_atualizado["cpf"] = cpf
        
        response = requests.put(f"{url}/{id}", json=cliente_atualizado)

        if response.status_code == 200:
            print(f"{nome} foi atualizado na lista de clientes")
        else:
            print('Erro ao atualizar o cliente:', response.status_code)

    # Delete via parametro ID
    def removerCliente(self, id):
        response = requests.delete(f"{url}/{id}")

        if response.status_code == 200:
            print(f"Cliente de código {id} foi removido da lista de clientes")
        else:
            print('Erro ao remover o cliente:', response.status_code)

    # Put sendo enviado com body JSON
    def inserirEnderecoCliente(self, id, endereco):
        cliente_atualizado = { "endereco": endereco }

        response = requests.put(f"{url}/{id}", json=cliente_atualizado )

        if response.status_code == 200:
            print(f"Endereço do cliente inserido com sucesso!")
        else:
            print('Erro ao inserir endereço cliente:', response.status_code)