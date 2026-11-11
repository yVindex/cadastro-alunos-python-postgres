from connect import conectar, criar_banco, criar_tabela

def exibir_aluno(aluno):
    return(
        f"ID: {aluno[0]}\n"
        f"Nome: {aluno[1]}\n"
        f"Idade: {aluno[2]} anos\n"
        f"Nota: {aluno[3]:.1f}"
    )
    
def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor
    
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

        if idade > 0:
            return idade
        print("A idade deve ser maior que 0.")
        
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
