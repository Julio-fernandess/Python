# Função para coletar informações pessoais
def coletar_informacoes_pessoais():
    nome = input("Qual é o seu nome completo? ")
    idade = input("Qual sua idade? ")
    cidade = input("Em que cidade mora? ")
    profissao = input("Qual sua profissão? ")
    hobby = input("Você poderia descrever um hobby ou atividade que gosta de fazer? ")

    # Organizando as informações em um dicionário
    informacoes = {
        "Nome Completo": nome,
        "Idade": idade,
        "Cidade": cidade,
        "Profissão": profissao,
        "Hobby": hobby
    }

    return informacoes

# Função para coletar informações sobre o funcionário
def coletar_informacoes_funcionario():
    nome = input("Qual é o seu nome? ")
    cargo = input("Qual seu cargo na empresa? ")
    empresa = input("Qual é o nome da empresa onde trabalha? ")
    salario = input("Qual o seu salário atual? ")
    tempo_trabalho = input("Há quanto tempo você trabalha na empresa? ")

    # Organizando as informações em um dicionário
    informacoes = {
        "Nome": nome,
        "Cargo": cargo,
        "Empresa": empresa,
        "Salário": salario,
        "Tempo de Trabalho": tempo_trabalho
    }

    return informacoes

# Função para coletar informações sobre o produto
def coletar_informacoes_produto():
    nome_produto = input("Qual é o nome do produto? ")
    preco = input("Qual é o preço do produto? ")
    categoria = input("Qual é a categoria ou o tipo do produto? ")
    quantidade_estoque = input("Qual é a quantidade disponível em estoque? ")
    data_validade = input("Qual é a data de validade (caso aplicável)? ")

    # Organizando as informações em um dicionário
    informacoes = {
        "Nome do Produto": nome_produto,
        "Preço": preco,
        "Categoria": categoria,
        "Quantidade em Estoque": quantidade_estoque,
        "Data de Validade": data_validade
    }

    return informacoes

# Função para exibir as informações de forma organizada
def exibir_informacoes(informacoes):
    print("\nInformações Coletadas:")
    print("----------------------")
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

# Função principal
def main():
    print("Escolha o formulário que deseja preencher:")
    print("1 - Informações Pessoais")
    print("2 - Dados do Funcionário")
    print("3 - Dados do Produto")
    
    escolha = input("Digite 1, 2 ou 3: ")

    if escolha == '1':
        informacoes_usuario = coletar_informacoes_pessoais()
        exibir_informacoes(informacoes_usuario)
    elif escolha == '2':
        informacoes_funcionario = coletar_informacoes_funcionario()
        exibir_informacoes(informacoes_funcionario)
    elif escolha == '3':
        informacoes_produto = coletar_informacoes_produto()
        exibir_informacoes(informacoes_produto)
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

# Executando a função principal
if __name__ == "__main__":
    main()
