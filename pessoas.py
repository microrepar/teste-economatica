"""Modulo que implementa a estrutura de dados Pessoa e a classe Pessoas - Questao 1.
Para implementacao dos metodos resolvi utilizar o padrao de estilo snake case,
que é o padrao convensinado pela comunidade python, mas nao eh obrigatorio.
"""
import contextlib
import copy
from collections import namedtuple
from typing import List

# Uma das formas de representar uma struct em python é utilizando tupla,
# pois é um tipo de estrutura imutável e indexada, então utilizei o
# namedtuple, que é uma uma variante dela, que permite acessar os indíces
# pelo nome funcionando semelhantemente a uma struct.
Pessoa = namedtuple("Pessoa", ["id", "nome"])


class Pessoas:
    """Classe para manipular lista de estrutura do tipo tupla que representa uma Pessoa

    Nos casos de uso apresentados na questão 1, aparentemente o método "Pessoas.Criar()" 
    efetua a crição de uma instância da classe Pessoas, atribuindo a referência do objeto
    criado para uma variável de nome **lista**, mas o que ocorre é que a própria classe 
    Pessoas carrega a referência do objeto criado, porque todas as chamadas de método de 
    instância passam a ser executadas pela própria classe, e neste ponto surgiram algumas 
    dúvidas. Primeiro, aparentemente o objeto criado seria referenciado pela variável 
    **lista**, o que não ocorre nos exemplos, pois a variável **lista** não é utilizada 
    em momento algum após a chamada do método "Criar()". Segundo, se a atribuição da instância
    foi realizada para a variável **lista**, entao os métodos somente poderiam ser acessado
    a partir da variável **lista** e nao do nome da classe Pessoa, como ocorre em todos os 
    exemplos de uso.
    Na especificação do código informa que o método criar é um construtor, o que também gerou
    outra dúvida, pois métodos contrutores geralmente não retornam valores, a não ser a 
    referência do objeto construido. Em python, instânciar um objeto é semelhante a efetuar 
    uma chamada de uma função, atribuindo para uma variável que armazena a referência do objeto 
    criado, conforme exemplo a seguir: ">>> pessoas = Pessoas()". Então os metódos ficam todos 
    acessíveis a partir da variável pessoas.
    Desta forma eu decide por não implementar o método "criar", pois o método contrutor da 
    linguagem python é o ```__new__```, que por baixo dos panos ele chama o método 
    ```__init__```, sendo assim a especifição do codigo é plenamente atendida com a implementação
     do metodo ```__init__```.
    """
    def __init__(self):
        self._lista_pessoas: List[Pessoa]
        self._carregar_pessoas()

    def _ler_uma_pessoa(self, id: int = None, nome: str = None) -> Pessoa:
        """auxiliar para carregar a lista de pessoas, se a função retornar 
        "nulo" significa que não temos mais pessoas para serem carregadas.
        """
        # TODO: O método "LerUmaPessoa" não precisa ser implementado

    def _carregar_pessoas(self):
        pessoas = []
        while True:
            pessoa = self._ler_uma_pessoa()
            if pessoa is None:
                break
            pessoas.append(pessoa)

        self._lista_pessoas = pessoas


    def indice_do_id(self, id: int) -> int:
        for i, pessoa in enumerate(self.pessoa_em_ordem_alfabetica):
            if pessoa.id == id:
                return i
        return -1

    def indice_do_nome(self, nome: str) -> int:
        # Aqui podera ocorrer um efeito colateral, pois se houver nomes
        # duplicados na lista o metodo retornará o indice da primeira
        # pessoa cuja o nome foi encontrado na lista.
        for i, pessoa in enumerate(self.pessoa_em_ordem_alfabetica):
            if pessoa.nome == nome:
                return i
        return -1

    @property  # Funcao decoradora que transforma o metodo em propriedade
    def count(self):
        # Retorna o tamanho da lista de pessoas
        return len(self._lista_pessoas)

    @property  # Funcao decoradora que transforma o metodo em propriedade
    def pessoa_em_ordem_alfabetica(self) -> List[Pessoa]:
        return [pessoa for pessoa in ordem_alfabetica(self._lista_pessoas)]


def ordem_alfabetica(pessoas: List[Pessoa]) -> List[Pessoa]:
    """Efetua a ordenacao da lista de pessoas utilizando o algoritmo bubble sort.
    Nao eh o algoritmo mais performatica para lista desordenadas muito grandes, 
    porem nas a maioria das linguagens tem funcoes e metodos embutidos que 
    implementam ordenacoes otimizadas.

    Args:
        pessoas (List[Pessoa]): Lista de tuplas Pessoas

    Returns:
        [List[Pessoa]]: Lista de tuplas Pessoa ordenada pelo nome
    """
    # Efetua uma copia da lista de pessoas para nao alterar implace a lista
    # original, pois as listas sao mutaveis e podem causar efeitos colaterais
    lista_pessoas_ordenada = copy.copy(pessoas)
    flag_mudou = True
    while flag_mudou:
        flag_mudou = False
        for i, pessoa in enumerate(lista_pessoas_ordenada):
            # Aqui foi utilizado o operador de contexto "with", pois não fazia
            # sentido utilizar o "try: except:", porque não utilizo a excessao
            # capiturada para nenhum tipo de tratamento, então eu apenas suprimo
            # a excessao levantada.
            with contextlib.suppress(IndexError):
                if pessoa.nome > lista_pessoas_ordenada[i + 1].nome:
                    flag_mudou = True
                    lista_pessoas_ordenada[i], lista_pessoas_ordenada[i + 1] = (
                        lista_pessoas_ordenada[i + 1],
                        lista_pessoas_ordenada[i],
                    )
    return lista_pessoas_ordenada
