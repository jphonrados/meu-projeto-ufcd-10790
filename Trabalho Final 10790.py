# Trabalho Final de Projeto de Programação (UFCD 10790): Publicar Projeto no GitHub

# Objetivo: 
# - Aprender a publicar um projeto local no GitHub;
# - Configurar um repositório remoto;
# - Sincronizar alterações entre local e remoto.

# Tarefas:

# 1. Preparar o Projeto Local:

# Comecei por criar uma pasta github10790 com um mini-projeto funcional, 
# conforme solicitado, que corresponde a um mini-programa
# que implementa algumas classes em Python com o objetivo de simular uma clínica médica.
# O programa permite registar e listar médicos, pacientes e consultas.
# Está dividido em dois ficheiros: um classes_medic com as classes 
# e outro (este) com a função main() que implementa uma interface com o utilizador.

# De seguida, criei um repositório local com o comando 'git init' (no terminal do VSC) 
# e adicionei os ficheiros ao repositório com 'git add .'.
# Configurei também username e e-mail.

# 2. Criar o Repositório Remoto no GitHub

# 3. Ligar o Repositório Local ao GitHub:

# Commando: git remote add origin https://github.com/jphonrados/meu-projeto-ufcd-10790.git
# Primeiro push: git push -u origin main
# Não funcionou porque ainda não tinha feito o commit inicial corretamente. Verifiquei com 'git log'.

# 4. Verificar no GitHub:

# Depois de feito o commit inicial seguido do primeiro push, verifiquei 
# no GitHub que o repositório estava corretamente publicado!

# 5. Alterar localmente e sincronizar com o GitHub:

# Fiz algumas alterações (adicionei estes comentários do ponto 5.) e atualizei no GitHub com os comandos:
# git add .
# git commit -m "Atualização do projeto com alguns comentários (relativos ao ponto 5.)."
# git push -u origin main
# De seguida, verifiquei que estas atualizações constavam do repositório respetivo no GitHub!

# Acrecentei um README.md com alguma info pessoal (nome e curso). Comando:
# echo "# meu-projeto-ufcd-10790" > README.md
# Verifiquei que foi criado com o comando ls
# git add README.md
# git commit -m "Adiciona README.md"
# E, de seguida, um push.
# echo "Nome: João Silva. Curso: LP Python Ação 2" >> README.md
# Por fim, um add (do README.md), um commit e um push para o GitHub.

#############################################################################################

from classes_medic import Medico, Paciente, Consulta

# Função principal para interagir com o utilizador:

def main():

    def interface():
        print("1. Adicionar Médico")
        print("2. Listar Médicos")
        print("3. Adicionar Paciente")
        print("4. Listar Pacientes")
        print("5. Agendar Consulta")
        print("6. Listar Consultas")
        print("0. Sair")
    
    lista_medicos = []
    lista_pacientes = []
    lista_consultas = []
    # As listas vazias têm de ficar fora do loop while para não serem reinicializadas a cada iteração! 
    # Isto para a informação não se perder a cada interação.

    # Loop principal de interface com o utilizador:

    while True:

        interface()
        opcao = int(input("Escolha uma opção (0 para sair): "))

        if opcao == 0:
            break

        elif opcao == 1:
            nome = input("Nome do médico: ")
            idade = int(input("Idade do médico: "))
            nif = input("NIF do médico: ")
            especialidade = input("Especialidade do médico: ")
            numero_ordem = input("Número de ordem do médico: ")
            medico = Medico(nome, idade, nif, especialidade, numero_ordem)
            lista_medicos.append(medico)
            print(f"Médico {medico.nome} adicionado com sucesso!")

        elif opcao == 2:
            print("\nLista de médicos disponíveis: ")
            if lista_medicos == []:
                print("Nenhum médico registado como disponível.")
            else:
                for medico in lista_medicos:
                    print(f"\n{medico}")
            print("\n")  # Linha vazia para melhor legibilidade

        elif opcao == 3:
            nome = input("Nome do paciente: ")
            idade = int(input("Idade do paciente: "))
            nif = input("NIF do paciente: ")
            numero_utente = input("Número de utente do paciente: ")
            historico_medico = input("Histórico médico do paciente (separado por vírgulas): ").split(",")
            paciente = Paciente(nome, idade, nif, numero_utente, historico_medico)
            lista_pacientes.append(paciente)
            entrada_historico = input("Adicionar entrada ao histórico médico: ")
            paciente.adicionar_entrada_historico(entrada_historico)
            print(f"Paciente {paciente.nome} adicionado com sucesso!")

        elif opcao == 4:
            print("\nLista de pacientes: ")
            if lista_pacientes == []:
                print("Nenhum paciente registado.")
            else:
                for paciente in lista_pacientes:
                    print(f"\n{paciente}")
                    print("Histórico médico:")
                    print(paciente.listar_historico())
            print("\n")

        elif opcao == 5:
           data = input("Data da consulta (AAAA-MM-DD): ")
           nome_medico = input("Nome do médico: ")
           nome_paciente = input("Nome do paciente: ")
           descricao = input("Motivo/descrição da consulta: ")
           # Procurar o médico e o paciente com recurso a next(), que retorna o primeiro elemento que satisfaz uma dada condição 
           # ou None se não encontrar nenhum. As expressões dentro do next() são geradores que percorrem as listas:
           medico = next((m for m in lista_medicos if m.nome == nome_medico), None)
           paciente = next((p for p in lista_pacientes if p.nome == nome_paciente), None)
           if medico and paciente:
           # Se ambos os objetos existem, a condição é avaliada como True e o bloco if é executado:
               consulta = Consulta(data, medico, paciente, descricao)
               lista_consultas.append(consulta)
               print("Consulta agendada com sucesso!")
           else:
               print("Médico ou paciente não encontrado. Verifique se foram registados.")

        elif opcao == 6:
            print("\nLista de consultas agendadas: ")
            if lista_consultas == []:
                print("Nenhuma consulta agendada.")
            else:
                for consulta in lista_consultas:
                    print(f"\n{consulta}")
            print("\n")  
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
