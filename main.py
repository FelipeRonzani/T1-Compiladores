import re

reserved_words = {'int', 'double', 'char', 'float', 'if', 'while', 'for'}
identifier_pattern = r'\b[A-Z][A-Za-z]*\b'
number_pattern = r'\b\d+(?:,\d+)?\b'

def gerar_tabela_simbolos(texto):
    tabela_simbolos = []
    simbolos_adicionados = set() 

    for palavra in reserved_words:
        if re.search(rf'\b{palavra}\b', texto) and palavra not in simbolos_adicionados:
            tabela_simbolos.append((palavra, 'reservada'))
            simbolos_adicionados.add(palavra)

    identificadores = re.findall(identifier_pattern, texto)
    for identificador in identificadores:
        if identificador not in reserved_words and identificador not in simbolos_adicionados:
            tabela_simbolos.append((identificador, 'identificador'))
            simbolos_adicionados.add(identificador)

    numeros = re.findall(number_pattern, texto)
    for numero in numeros:
        if numero not in simbolos_adicionados:
            tabela_simbolos.append((numero, 'número'))
            simbolos_adicionados.add(numero)

    return tabela_simbolos

def ler_entrada():
    escolha = input("Você deseja digitar o código-fonte ou ler de um arquivo? (digitar/arquivo): ").strip().lower()

    if escolha == 'digitar':
        texto = input("Digite o código-fonte: ")
    elif escolha == 'arquivo':
        nome_arquivo = input("Digite o caminho do arquivo: ").strip()
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                texto = arquivo.read()
        except FileNotFoundError:
            print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
            return None
    else:
        print("Opção inválida. Escolha 'digitar' ou 'arquivo'.")
        return None

    return texto

def exibir_tabela_simbolos(tabela):
    print(f"{'Entrada':<15}{'Tipo':<15}")
    print("-" * 30)
    for i, (simbolo, tipo) in enumerate(tabela, start=1):
        print(f"{i:<5}{simbolo:<15}{tipo:<15}")

def main():
    texto = ler_entrada()

    if texto:
        tabela = gerar_tabela_simbolos(texto)
        exibir_tabela_simbolos(tabela)

if __name__ == "__main__":
    main()
