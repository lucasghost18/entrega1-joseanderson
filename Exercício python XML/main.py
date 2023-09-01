import xml.etree.ElementTree as ET

class Passageiro:
    def __init__(self, nome, idade, numero_ticket, origem, destino):
        self.nome = nome
        self.idade = idade
        self.numero_ticket = numero_ticket
        self.origem = origem
        self.destino = destino

class ExtratorXML:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)  # Parse no XML e cria uma tree
        self.root = self.tree.getroot()  # pega o root da tree
    
    def extrair_dados(self):
        passageiros = []
        
        for passageiro_elem in self.root.findall('passageiro'):
            # pega os dados de cada elemento do XML
            nome = passageiro_elem.find('nome').text
            idade = int(passageiro_elem.find('idade').text)
            numero_ticket = passageiro_elem.find('numero_ticket').text
            origem = passageiro_elem.find('origem').text
            destino = passageiro_elem.find('destino').text
            
            # Cria um objeto Passageiro e add numa lista
            passageiro = Passageiro(nome, idade, numero_ticket, origem, destino)
            passageiros.append(passageiro)
        
        return passageiros

# if para rodar apenas o conteúdo desse arquivo com o que foi extraido em cima
if __name__ == '__main__':
    extrator = ExtratorXML('passageiros.xml')  # Cria uma instância do ExtratorXML com o arquivo XML
    dados_passageiros = extrator.extrair_dados()  # Chama o método para extrair os dados do XML
    
    print("Número de passageiros:", len(dados_passageiros))
    print("Origens e destinos:")
    for passageiro in dados_passageiros:
        print(f"Passageiro: {passageiro.nome} | Origem: {passageiro.origem} | Destino: {passageiro.destino}")
