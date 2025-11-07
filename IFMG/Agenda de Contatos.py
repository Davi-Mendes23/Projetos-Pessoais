import csv
from os.path import isfile


# Escreve uma linha na tela para organização visual
def linha():
    """Imprime uma linha de separação no console."""
    print('-' * 50)


class Contato:
    """Representa um contato na agenda, com nome, telefone e aniversário."""
    # Campos padrão para cada contato
    campos = ['Nome', 'Telefone', 'Aniversário']

    def __init__(self, valores):
        """
        Inicializa um objeto Contato.
        'valores' deve ser uma lista de strings com nome, telefone e aniversário.
        """
        # Inicializa um dicionário para armazenar os dados do contato
        self._dic = {}
        # Percorre a lista de campos padrão
        for cont, camp in enumerate(self.campos):
            # CORREÇÃO: A variável no loop era 'camp', mas estava sendo usado 'campo'.
            # O correto é usar a variável definida no loop ('camp').
            self._dic[camp] = valores[cont]

    def alterar(self):
        """Permite ao usuário alterar os dados de um contato existente."""
        linha()
        print('Alteração de contato')
        linha()
        # Percorre os campos e valores do contato
        for campo, valor in self._dic.items():
            # Mostra o campo com seu valor atual
            print(f'{campo} ({valor})')
            # Pede ao usuário o novo valor
            novo_valor = input('Novo valor (deixe em branco para manter o atual): ').strip()
            # Verifica se um novo valor foi inserido
            if novo_valor:
                # Atribui o novo valor ao campo
                self._dic[campo] = novo_valor

    @property
    def valores(self):
        """Retorna uma lista com os valores dos campos do contato."""
        lista_valores = []
        for campo in self.campos:
            # CORREÇÃO: Havia um erro de digitação ('self.di').
            # O correto é self._dic[campo] para acessar o valor no dicionário.
            lista_valores.append(self._dic[campo])
        return lista_valores

    def __str__(self):
        """Retorna uma representação em string do contato."""
        # Cria uma lista de "Campo: Valor"
        lista_cv = [f'{campo}: {valor}' for campo, valor in self._dic.items()]
        return '\n'.join(lista_cv)

    def __lt__(self, other):
        """
        Define a comparação '<' para ordenar contatos pelo nome.
        Essencial para o método sort().
        """
        return self.valores[0].lower() < other.valores[0].lower()

    @classmethod
    def novo(cls):
        """
        Método de classe para criar um novo contato a partir da entrada do usuário.
        """
        linha()
        print('Novo contato')
        linha()
        lista_valores = []
        # Pede ao usuário para inserir os dados para cada campo
        for campo in cls.campos:
            valor = input(f'{campo}: ').strip()
            lista_valores.append(valor)

        # Validação: o nome é obrigatório
        if not lista_valores[0]:
            print('Contato inválido, o nome é um campo obrigatório.')
            return None
        else:
            # Cria e retorna a nova instância de Contato
            return Contato(lista_valores)


class Arquivo:
    """Gerencia a leitura e escrita dos contatos em um arquivo CSV."""

    def __init__(self, nome_arquivo):
        """
        Inicializa o gerenciador de arquivo e carrega os contatos existentes.
        """
        self._nome_arquivo = nome_arquivo
        self._lista_contatos = []
        # Verifica se o arquivo de contatos já existe
        if isfile(self._nome_arquivo):
            # MELHORIA: Especificar encoding 'utf-8' e newline='' é uma boa prática
            # para evitar problemas com caracteres especiais e linhas em branco no CSV.
            with open(self._nome_arquivo, 'r', newline='', encoding='utf-8') as arq:
                leitor = csv.reader(arq)
                try:
                    # Ignora a linha do cabeçalho
                    next(leitor)
                    # Percorre as linhas do arquivo
                    for linha_csv in leitor:
                        # CORREÇÃO: Deve-se instanciar a classe Contato.
                        # O código original tentava chamar uma variável local 'contato'.
                        contato = Contato(linha_csv)
                        self._lista_contatos.append(contato)
                except StopIteration:
                    # O arquivo existe, mas está vazio (só tinha cabeçalho ou nada)
                    pass

    def listar(self):
        """Exibe todos os contatos cadastrados, ordenados por nome."""
        if not self._lista_contatos:
            print('Nenhum contato cadastrado!')
        else:
            # Ordena a lista de contatos (usa o método __lt__ da classe Contato)
            self._lista_contatos.sort()
            # Percorre a lista e exibe cada contato com seu código
            for i, contato in enumerate(self._lista_contatos):
                linha()
                print(f'Código: {i}')
                print(str(contato))
        linha()

    def buscar(self, codigo):
        """Busca um contato na lista pelo seu código (índice)."""
        if 0 <= codigo < len(self._lista_contatos):
            return self._lista_contatos[codigo]
        return None

    def incluir(self):
        """Adiciona um novo contato à lista."""
        contato = Contato.novo()
        if contato is not None:
            self._lista_contatos.append(contato)
            print('Contato incluído com sucesso!')

    def excluir(self, codigo):
        """Remove um contato da lista pelo seu código."""
        if 0 <= codigo < len(self._lista_contatos):
            self._lista_contatos.pop(codigo)
            print('Contato excluído com sucesso!')
        else:
            print('Código de contato inválido!')

    def salvar(self):
        """Salva a lista de contatos atual no arquivo CSV."""
        with open(self._nome_arquivo, 'w', newline='', encoding='utf-8') as arq:
            escritor = csv.writer(arq)
            # Escreve o cabeçalho no arquivo
            escritor.writerow(Contato.campos)
            # Escreve os dados de cada contato
            for contato in self._lista_contatos:
                escritor.writerow(contato.valores)
        print('Contatos salvos com sucesso no arquivo!')


class Agenda:
    """Controla o fluxo principal do programa e a interação com o usuário."""

    def __init__(self, nome_arquivo='contatos.csv'):
        """Inicializa a agenda, criando o objeto de arquivo."""
        self._arq = Arquivo(nome_arquivo)

    def menu(self):
        """Exibe o menu de opções e retorna a escolha do usuário."""
        print("Agenda de Contatos")
        linha()
        self._arq.listar()
        print('(I)ncluir | (E)xcluir | (A)lterar | (S)alvar | Sai(R)')
        return input('Informe a opção desejada: ').strip().lower()

    def executar(self):
        """Inicia o loop principal da agenda."""
        while True:
            opcao = self.menu()
            if opcao == 'i':
                self._arq.incluir()
            elif opcao in ('e', 'a'):
                # MELHORIA: Adicionado tratamento de erro para entrada não numérica.
                # Isso evita que o programa quebre se o usuário digitar um texto.
                try:
                    codigo = int(input(f'Código do contato a ser {"excluído" if opcao == "e" else "alterado"}: '))
                    if opcao == 'e':
                        self._arq.excluir(codigo)
                    else:  # opcao == 'a'
                        contato = self._arq.buscar(codigo)
                        if contato:
                            contato.alterar()
                            print('Contato alterado com sucesso!')
                        else:
                            print('Código de contato inválido!')
                except ValueError:
                    print('Erro: Por favor, digite um número válido para o código.')
            elif opcao == 's':
                self._arq.salvar()
            elif opcao == 'r':
                print('Saindo da agenda...')
                break
            else:
                print('Opção inválida! Tente novamente.')


if __name__ == '__main__':
    # Cria a instância da agenda e inicia a execução
    agenda = Agenda()
    agenda.executar()
