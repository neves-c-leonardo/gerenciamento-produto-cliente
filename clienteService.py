clientes = [
  {"id": 1, "nome": "Leonardo"},
  {"id": 2, "nome": "Brenda"},
  {"id": 3, "nome": "Catarina"}
]



class Cliente:
  TODOS = "TODOS"
  SAIR = "SAIR"

  def adicionarCliente(self):
    nome = input("Qual o nome do cliente que deseja adicionar? ")
    proximoId = len(clientes)+1
    while next((cliente for cliente in clientes if cliente["id"] == proximoId), None) is not None:
      proximoId += 1
    clientes.append({"id": proximoId, "nome": nome})

    print(f"{nome} foi adicionado a lista de Clientes")


  def editarCliente(self):
    while True:
      id = input("Digite o código do cliente que deseja editar ou digite 'Sair' para voltar ao menu: ")

      if(id.upper() == self.SAIR):
        break

      cliente_encontrado = cliente_encontrado = self.consultarClientePorId(id)

      if cliente_encontrado is None:
          print("ID não encontrado. Veja a lista de clientes:")
          self.consultarCliente(self.TODOS)
          continue
      
      print(f"Dados atuais do cliente: {cliente_encontrado['id']} - {cliente_encontrado['nome']}")

      novo_nome = input("Digite o novo nome do cliente: ")

      cliente_encontrado['nome'] = novo_nome

      print(f"Cliente atualizado: {cliente_encontrado['id']} - {cliente_encontrado['nome']}")
      break

  def removerCliente(self):
    while True:

      id = input("Digite o código do cliente que deseja removerou digite 'Sair' para voltar ao menu: ")

      if(id.upper() == self.SAIR):
        break

      cliente_encontrado = self.consultarClientePorId(id)

      if cliente_encontrado is None:
        print("ID não encontrado. Veja a lista de clientes:")
        self.consultarCliente(self.TODOS)
        return
      
      clientes.remove(cliente_encontrado)

      print(f"Cliente {cliente_encontrado['nome']} removido com sucesso!")
      break

  def consultarCliente(self):

    id = input("Digite o id do cliente que deseja buscar! (Digite 'todos' para retornar todos os clientes cadastrados) ")
    
    if isinstance(id, str) and id.upper() == "TODOS":
      for cliente in clientes:  
        print(f"{cliente['id']} - {cliente['nome']}")
    else:  
      cliente = self.consultarClientePorId(id)
      print(f"Dados do cliente: {cliente['id']} - {cliente['nome']}")
    
  def consultarClientePorId(self, id):
    try:
        id = int(id)
    except ValueError:
      print("Não foi digitado um número inteiro!")
      return

    cliente_encontrado = None

    for cliente in clientes:
        if cliente["id"] == id:
            cliente_encontrado = cliente
            break
      
    return cliente_encontrado