from connect import conectar, criar_banco, criar_tabela


def exibir_aluno(aluno):
    return (
        f"ID: {aluno[0]}\n"
        f"Nome: {aluno[1]}\n"
        f"Idade: {aluno[2]} anos\n"
        f"Nota: {aluno[3]:.1f}"
    )


def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, idade, nota FROM alunos ORDER BY id")
    registros = cursor.fetchall()
    conexao.close()

    if len(registros) == 0:
        print("Nenhum aluno foi cadastrado.")
        return

    print("------------------Lista de Alunos------------------")
    for aluno in registros:
        print(exibir_aluno(aluno))
        print("---------------------------------------------------")


def ler_nome():
    while True:
        nome = input("Digite o nome do aluno: ").strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")


def ler_idade():
    while True:
        texto = input("Digite a idade do aluno: ").strip()

        try:
            idade = int(texto)
        except ValueError:
            print("A idade deve ser um número inteiro.")
            continue

        if 0 < idade <= 150:
            return idade
        print("A idade deve estar entre 1 e 150.")


def ler_nota():
    while True:
        texto = input("Digite a nota do aluno: ").strip().replace(",", ".")
        try:
            nota = float(texto)
        except ValueError:
            print("A nota deve ser um número.")
            continue
        if 0 <= nota <= 10:
            return nota
        print("A nota deve estar entre 0 e 10.")


def adicionar_aluno():
    nome = ler_nome()
    idade = ler_idade()
    nota = ler_nota()

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO alunos (nome, idade, nota) VALUES (%s, %s, %s)",
        (nome, idade, nota)
    )

    conexao.commit()
    conexao.close()

    print("Aluno cadastrado com sucesso!")


def buscar_aluno():
    nome = input("Digite o nome do aluno que deseja buscar: ").strip()

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, idade, nota FROM alunos WHERE nome ILIKE %s  ORDER BY id", (f"%{nome}%",),
                   )

    registros = cursor.fetchall()
    conexao.close()

    if len(registros) == 0:
        print("Aluno não encontrado.")
        return

    print("\nAluno(s) encontrado(s):")
    for aluno in registros:
        print(exibir_aluno(aluno))
        print("---------------------------------------------------")


def ler_id(mensagem):
    while True:
        texto = input(mensagem).strip()
        try:
            return int(texto)
        except ValueError:
            print("O ID deve ser um numero inteiro.")


def atualizar_aluno():
    id_aluno = ler_id("Digite o ID do aluno que deseja atualizar: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, nome, idade, nota FROM alunos WHERE id = %s",
        (id_aluno,),
    )

    aluno = cursor.fetchone()

    if aluno is None:
        print("Aluno não encontrado.")
        conexao.close()
        return

    print("Dados atuais:")
    print(exibir_aluno(aluno))
    print("\nDigite os novos dados:")

    nome = ler_nome()
    idade = ler_idade()
    nota = ler_nota()

    cursor.execute(
        "UPDATE alunos SET nome = %s, idade = %s, nota = %s WHERE id = %s",
        (nome, idade, nota, id_aluno,)
    )

    conexao.commit()
    conexao.close()
    print("Aluno atualizado com sucesso!")


def remover_aluno():
    id_aluno = ler_id("Digite o ID do aluno que deseja remover: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id FROM alunos WHERE id = %s",
        (id_aluno,)
    )

    if cursor.fetchone() is None:
        print("Aluno não encontrado.")
        conexao.close()
        return

    cursor.execute(
        "DELETE FROM alunos WHERE id = %s",
        (id_aluno,)
    )

    conexao.commit()
    conexao.close()

    print("Aluno removido com sucesso!")


def mostrar_media():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT AVG(nota) FROM alunos"
    )

    media = cursor.fetchone()[0]
    conexao.close()

    if media is None:
        print("Nenhum aluno cadastrado.")
        return

    print(f"A média geral é {media:.2f}")


def exibir_menu():
    print("-----------SISTEMA DE CADASTRO DE ALUNOS-----------")
    print("1. Cadastrar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno pelo nome")
    print("4. Atualizar dados de um aluno")
    print("5. Remover aluno")
    print("6. Mostrar média geral das notas")
    print("7. Sair")
    print("---------------------------------------------------")


def main():
    criar_banco()
    criar_tabela()

    while True:
        exibir_menu()
        opcao = input("Digite uma opção: ").strip()
        print("---------------------------------------------------")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            atualizar_aluno()
        elif opcao == "5":
            remover_aluno()
        elif opcao == "6":
            mostrar_media()
        elif opcao == "7":
            print("Saindo......")
            break
        else:
            print("Opção inválida. Digite uma opção de 1 a 7.")


if __name__ == "__main__":
    main()
