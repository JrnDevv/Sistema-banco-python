import mysql.connector
from time import sleep
import config

def conectar():
    return mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )

# Teste inicial de conexão
try:
    conexao = conectar()
    print("Conexão com MySQL feita com sucesso!")
    conexao.close()
except mysql.connector.Error as err:
    print(f"Erro na conexão {err}")

def inserir_contato(nome, telefone, email):
    # Validações
    if not nome.strip():
        print("Nome não pode estar vazio.")
        return
    if '@' not in email or '.' not in email:
        print("E-mail inválido.")
        return
    if not telefone.isdigit():
        print("Telefone deve conter apenas números.")
        return
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)"
        valores = (nome, telefone, email)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print(f"Contato {nome} inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir contato: {e}")

def listar_contatos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM contatos")
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()

        if resultados:
            print("\nLista de Contatos:")
            for contato in resultados:
                print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, E-mail: {contato[3]}")
        else:
            print("Nenhum contato encontrado.")
    except Exception as e:
        print(f"Erro ao listar contatos: {e}")

def buscar_contato(nome_busca):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT id, nome, telefone, email FROM contatos WHERE nome LIKE %s"
        parametro = f"%{nome_busca}%"
        cursor.execute(sql, (parametro,))
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        
        if resultados:
            print(f"\nResultados para '{nome_busca}':")
            for contato in resultados:
                print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, E-mail: {contato[3]}")
        else:
            print("Nenhum contato encontrado com esse nome.")
    except Exception as e:
        print(f"Erro ao buscar contato: {e}")

def atualizar_contato(id_contato, novo_nome, novo_telefone, novo_email):
    # Validações
    if not novo_nome.strip():
        print("Nome não pode estar vazio.")
        return
    if '@' not in novo_email or '.' not in novo_email:
        print("E-mail inválido.")
        return
    if not novo_telefone.isdigit():
        print("Telefone deve conter apenas números.")
        return
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """
        UPDATE contatos
        SET nome = %s, telefone = %s, email = %s
        WHERE id = %s
        """
        valores = (novo_nome, novo_telefone, novo_email, id_contato)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print(f"Contato {id_contato} atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar contato: {e}")

def deletar_contato(id_contato):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM contatos WHERE id = %s"
        cursor.execute(sql, (id_contato,))
        conexao.commit()
        cursor.close()
        conexao.close()
        print(f"Contato {id_contato} deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar contato: {e}")

def menu():
    while True:
        print("\n1. Inserir contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Atualizar contato")
        print("5. Deletar contato")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            inserir_contato(nome, telefone, email)
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            busca = input("Nome para buscar: ")
            buscar_contato(busca)
        elif opcao == '4':
            id_contato = int(input("ID do contato para atualizar: "))
            novo_nome = input("Nome novo: ")
            novo_telefone = input("Novo telefone: ")
            novo_email = input("Novo e-mail: ")
            atualizar_contato(id_contato, novo_nome, novo_telefone, novo_email)
        elif opcao == '5':
            id_contato = int(input("ID do contato para deletar: "))
            deletar_contato(id_contato)
        elif opcao == '6':
            print("Saindo...")
            sleep(2)
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
