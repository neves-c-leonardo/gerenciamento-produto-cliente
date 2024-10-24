import http.client
import json

class EnderecoApiService:

    def consultarEnderecoIbge(self):

        # Conectar ao servidor de API da Via Cep
        apiViaCep = http.client.HTTPSConnection("viacep.com.br")
 
        while True:
            cep = input("Digite o e cep para consultar o endereço: ")

            # Enviar uma requisição GET
            apiViaCep.request("GET", f"/ws/{cep}/json/")

            # Obter a resposta
            response = apiViaCep.getresponse()

            if response.status == 200:
                data = response.read().decode("utf-8")
                endereco_json = json.loads(data)

                endereco_simples = {
                    "logradouro": endereco_json.get("logradouro"),
                    "bairro": endereco_json.get("bairro"),
                    "localidade": endereco_json.get("localidade"),
                    "uf": endereco_json.get("uf")
                }

                print("1 - Confirmar endereço! ")
                print("2 - Para tentar novamente ")
                print("9 - Para voltar o menu ")

                acao = input("Qual ação deseja realizar? ")

                if acao == "1":
                    numero = input("Digite o número da residencia: ")
                    complemento = input("Digite o complemento da residencia (Ou enter para ir vazio caso não exista) ")

                    endereco_simples["numero"] = numero
                    endereco_simples["complemento"] = complemento

                    self.endereco = endereco_simples
                
                    apiViaCep.close()
                    return self.endereco
                elif acao == 2:
                    continue
                else:
                    deveContinuar = input("Cep não existe! Digite '0' para finalizar ou enter para continuar: ")
                    if(deveContinuar == "0"):
                        break
                    continue
            else:
                print('Erro ao consultar o endereco:', response.status)

        
        
