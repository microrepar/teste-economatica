"""Modulo que implementa o conjunto de classes de investimentos que compoe
uma carteira de investimentos - Questao 2.

Raises:
    ValorMinimoInvalidoError: Lanca excecao de valores minimos nao atendidos
    QtdeMinimaInvalidaError: Lanca excecao para quantidades minimas nao atendidas
"""
import abc
import enum
from typing import Any, List
import datetime

# Criei uma enumeracao, pois eh uma forma mais consistente de classificar
@enum.unique
class TipoRendaFixa(enum.Enum):
    PREFIXADO = 1
    POSFIXADO = 2


# Crie uma classe base abstrata para definir um tipo de dado Investimento e
# com atributos e metodos comuns que sao utilizados pelas classes que herdam
# de Investimento, nela contem metodos abstratos que devem ser implementados
# por todas as classes que herdam a herdam
class Investimento(abc.ABC):
    """[summary]

    Args:
        abc ([ABC]): Classe Base Abstrata
    """

    def __init__(self, nome):
        # Decide adicionar o atributo nome, porque todas as classes concretas
        # que herdam de Investimento tem o atributo nome na especificacao.
        self._nome: str = nome
        self._valor: float

    # Exige a implementado do metodo pela classe que herda de Investimento.
    @abc.abstractclassmethod
    def adiciona_valor(self, valor: float):
        """Efetua a validacao do valor a ser adicionado no investimento"""

    # Exige a implementado do metodo pela classe que herda de Investimento.
    @abc.abstractclassmethod
    def descricao(self) -> str:
        """A descrição de um investimento de uma carteira depende de cada tipo
        e combina as informações adicionais sobre o investimento. Desta forma
        cada classe que herdar de Investimento devera implementar este metodo.
        """

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        # TODO: Implementar regras de consistencia do nome do Investimento
        self._nome = nome

    @property
    def valor(self) -> float:
        return self._valor

    # Gancho para retornar a descricao do Investimento. Funciona
    # semelhantemente ao metodo to_string() da linguagem java.
    def __str__(self):
        return self.descricao()


class Acao(Investimento):
    def __init__(self, nome: str):
        super().__init__(nome)
        self._quantidade: int

    def adiciona_valor(self, valor: float):
        # Local onde deve ser implementado as regras de valores
        # para o investimento em Acões
        if valor < 100.00:
            raise ValorMinimoInvalidoError(
                f"O valor minimo aceito eh de 100.00: e foi passado o valor de: {valor}"
            )
        self._valor = valor

    def descricao(self):
        return (
            f"Tipo de investimento:...Acões \n"
            f"Nome do investimento:...{self._nome}\n"
            f"Valor do investimento:..{self._valor}\n"
            f"Quantidade de ações:....{self._quantidade}\n"
        )

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, qtde: int):
        # Local onde deve ser implementado as regras da quantidade
        # de minima ou maxima de Acoes
        if qtde < 1:
            raise QtdeMinimaInvalidaError(
                f"A quantidade minima do investimento eh 1: e foi passado a quantidade e {qtde}"
            )
        self._quantidade = qtde


class Fundo(Investimento):
    def __init__(self, nome: str):
        super().__init__(nome)
        self._quantidade_cotas: int
        self._cnpj: str

    def adiciona_valor(self, valor: float):
        # Local onde deve ser implementado as regras de valores
        # para o investimento em Fundos
        if valor < 50.00:
            raise ValorMinimoInvalidoError(
                f"O valor minimo esperado era de 50.00: e foi passado o valor de: {valor}"
            )
        self._valor = valor

    def descricao(self):
        return (
            f"Tipo de investimento:..Fundos \n"
            f"Nome do investimento:..{self._nome}\n"
            f"CNPJ do investimento:..{self._cnpj}\n"
            f"Quantidade de cotas:...{self._quantidade_cotas}\n"
        )

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        if not self._cnpj_eh_valido(cnpj):
            raise Exception("O CNPJ informado eh invalido!")
        self._cnpj = cnpj

    def _cnpj_eh_valido(self, cnpj):
        """Efetua a validacao do CNPJ"""
        # TODO: Implementar o algoritmo de validacao do CNPJ
        pass

    @property
    def quantidade_cotas(self) -> int:
        return self._quantidade

    @quantidade_cotas.setter
    def quantidade(self, qtde: int):
        # Local onde deve ser implementado as regras da quantidade
        # de minima ou maxima de Fundos
        if qtde < 1:
            raise QtdeMinimaInvalidaError(
                f"A quantidade minima do investimento eh 1: e foi passado a quantidade de {qtde}"
            )
        self._quantidade_cotas = qtde


class TituloRendaFixa(Investimento):
    def __init__(
        self,
        nome: str,
        tipo_renda_fixa: TipoRendaFixa,
        taxa_juros: float,
        texto_adicional: str = None,
    ):

        super().__init__(nome)
        self._taxa_juros: float
        self._texto_adicional: str = texto_adicional
        if not isinstance(tipo_renda_fixa, TipoRendaFixa):
            raise Exception("O tipo informado nao eh um tipo de renda fixa")
        self._tipo_titulo: TipoRendaFixa = tipo_renda_fixa
        self._consiste_taxa_juros(taxa_juros)

    @property
    def tipo_titulo(self):
        return self._tipo_titulo

    def _consiste_taxa_juros(self, taxa_juros):
        if isinstance(taxa_juros, float):
            if taxa_juros > 0.0:
                self._taxa_juros = taxa_juros
            else:
                ValorMinimoInvalidoError(
                    (
                        f"O valor minimo da taxa de juros deve ser maior que 0:"
                        f" o valor informa foi de: {taxa_juros}"
                    )
                )
        else:
            Exception("O valor informado nao eh um valor numerico!")

    def adiciona_valor(self, valor: float):
        # Local onde deve ser implementado as regras de valores
        # para o investimento em Titulos de Renda Fixa
        if valor < 10.00:
            raise ValorMinimoInvalidoError(
                f"O valor minimo esperado era de 10.00: e foi passado o valor de: {valor}"
            )
        self._valor = valor

    def descricao(self):
        if self._tipo_titulo is TipoRendaFixa.PREFIXADO:
            return (
                f"Tipo de investimento:..Titulo de Renda Fixa \n"
                f"Nome do investimento:..{self._nome}\n"
                f"Tipo do titulo:........Pré fixado\n"
                f"Taxa de Juros:...{self._quantidade_cotas}\n"
            )
        elif self._tipo_titulo is TipoRendaFixa.POSFIXADO:
            return (
                f"Tipo de investimento:.....Titulo de Renda Fixa \n"
                f"Nome do investimento:.....{self._nome}\n"
                f"Tipo do titulo:...........Pós fixado\n"
                f"Taxa de Juros:............{self._quantidade_cotas}\n"
                f"Informações adicionais:...{self._texto_adicional}\n"
            )


class Carteira:
    def __init__(self, nome, data):
        self._nome = nome
        self._data = self.alterar_data(data)
        self._lista_investimentos: List[Investimento]

    def adiciona_investimento(self, investimento: Investimento):
        if isinstance(investimento, Investimento):
            self.lista_investimentos.append(investimento)

    def remover_investimento(self, nome):
        indice = self._indice_do_nome(nome)
        if indice is not None:
            return self._lista_investimentos.pop(indice)

    def _indice_do_nome(self, nome):
        for i, investimento in enumerate(self._lista_investimentos):
            if investimento.nome == nome:
                return i

    def _str_to_data(self, str_data: str):
        if str_data is None or str_data.strip() == '':
            return None
        try:
            data = datetime.datetime.strptime(str_data, '%d/%m/%Y')
        except Exception as e:
            str(e)
            return None
        else:
            return data

    def alterar_data(self, str_data: str):
        data = self._str_to_data(str_data)
        if data is None:
            self._data = data
        else:
            raise(f'A data informada não é valida: {data}')

    @property
    def data(self):
        return self._data.strftime('%d/%m/%Y')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        # TODO: Implementar regras de consistencia de nome para Carteira
        self._nome = nome

    @property
    def listar_investimentos(self):
        return self._lista_investimentos


class ValorMinimoInvalidoError(Exception):
    """A Exception sera lancada quando o valor minimo
    para o tipo de investimento nao for atendido.
    """


class QtdeMinimaInvalidaError(Exception):
    """A Exception sera lancada quando a quantidade minima
    para o tipo de investimento nao for atendida.
    """
