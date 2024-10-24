from api.clientesApiService import ClientesApiService
from api.enderecoApiService import EnderecoApiService

class Cliente:
  TODOS = "TODOS"
  SAIR = "SAIR"

  def __init__(self):
    self.clientesApi = ClientesApiService()
    self.enderecoApi = EnderecoApiService()
    
  def adicionarCliente(self):
    nome = input("Qual o nome do cliente? ")
    cpf = input("Qual o CPF do cliente? ")
    endereco = self.enderecoApi.consultarEnderecoIbge()
    self.clientesApi.adicionarCliente(nome, cpf, endereco)

  def editarCliente(self):
    while True:
      id = input("Digite o código do cliente que deseja editar ou digite 'Sair' para voltar ao menu: ")

      if(id.upper() == self.SAIR):
        break

      cliente_encontrado = self.clientesApi.buscarCliente(id)

      if cliente_encontrado is None:
          print("ID não encontrado. Veja a lista de clientes:")
          clientes = self.clientesApi.buscarClientes()
          print(clientes)
          continue
      
      print(f"Dados atuais do cliente: {cliente_encontrado['id']} - {cliente_encontrado['nome']}")

      novo_nome = input("Digite o novo nome do cliente: ")
      novo_cpf = input("Digite cpf do cliente: ")

      self.clientesApi.alterarCliente(id, novo_nome, novo_cpf)
      break

  def removerCliente(self):
    while True:

      id = input("Digite o código do cliente que deseja removerou digite 'Sair' para voltar ao menu: ")

      if(id.upper() == self.SAIR):
        break

      cliente_encontrado = self.clientesApi.buscarCliente(id)

      if cliente_encontrado is None:
        print("ID não encontrado. Veja a lista de clientes:")
        clientes = self.clientesApi.buscarClientes()
        print(clientes)
        continue
      
      self.clientesApi.removerCliente(id)
      break

  def consultarCliente(self):
    id = input("Digite o id do cliente que deseja buscar! (Digite 'todos' para retornar todos os clientes cadastrados) ")
    
    if isinstance(id, str) and id.upper() == "TODOS":
      for cliente in self.clientesApi.buscarClientes():  
        print(f"{cliente['id']} - {cliente['nome']}")
    else:  
      cliente = self.clientesApi.buscarCliente(id)
      print(f"Dados do cliente: {cliente['id']} - {cliente['nome']}")
    
  def consultarClientePorId(self, id):

    cliente = self.clientesApi.buscarCliente(id)

    if cliente is None:
      print("Usuário digitado não existe!")

    print(f"Dados do cliente: {cliente['id']} - {cliente['nome']}")
