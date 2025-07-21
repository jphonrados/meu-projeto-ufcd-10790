class Pessoa:
    def __init__(self, nome: str, idade: int, nif: str):
        self.nome = nome
        self.idade = idade
        self.nif = nif
    # Método __str__() para mostrar os dados de cada objeto Pessoa (optei por não o usar na função main()):
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, NIF: {self.nif}"

class Medico(Pessoa):
    def __init__(self, nome: str, idade: int, nif: str, especialidade: str, numero_ordem: str):
        super().__init__(nome, idade, nif)
        self.especialidade = especialidade
        self.numero_ordem = numero_ordem
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Especialidade: {self.especialidade}, Número da Ordem: {self.numero_ordem}"
    
class Paciente(Pessoa):
    def __init__(self, nome, idade, nif, numero_utente: str, historico_medico: list):
        super().__init__(nome, idade, nif)
        self.numero_utente = numero_utente
        self.historico_medico = historico_medico
    def adicionar_entrada_historico(self, descricao: str):
            self.historico_medico.append(f" {descricao}")                   
    def listar_historico(self):
            return ",".join(self.historico_medico)

class Consulta:
    def __init__(self, data: str, medico: Medico, paciente: Paciente, descricao: str):
        self.data = data
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
    def __str__(self):
        return f"Data: {self.data}, Médico: {self.medico.nome}, Paciente: {self.paciente.nome}, Descrição: {self.descricao}"