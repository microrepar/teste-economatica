# Economatica

Teste
-----

O objetivo deste teste é avaliar seu conhecimento em programação básica, estrutura de dados e programação orientada a objeto.

As duas questões do teste são totalmente independentes.

Se tiver dúvida de algo, escreva a dúvida claramente, tome uma decisão, escreva qual foi sua decisão e prossiga baseado na sua decisão.

Você pode continuar usando uma linguagem de algoritmo genérico (como está abaixo) ou também pode usar uma linguagem real à sua escolha. O importante não é o código executar, o importante é estar correto e mostrar sua linha de raciocínio.


Questão 1
=========
>Abaixo temos uma estrutura de dados "Pessoa" e uma classe "Pessoas".
>
>Implemente os métodos da classe Pessoas de forma que seja possível executar os exemplos de uso abaixo,
>não precisa implementar nada nos exemplos de uso.
>
>Você pode criar variáveis, estrutura e métodos que achar necessário para completar a tarefa.
>
>O método "LerUmaPessoa" não precisa ser implementado, ele deve ser usado como auxiliar para carregar a
>lista de pessoas, se a função retornar "nulo" significa que não temos mais pessoas para serem carregadas.
>
>Implementar rotinas de ordenação e busca que achar necessárias para o funcionamento dos demais
>métodos da classe.
>
>Se utilizar uma linguagem de programação real, por favor, utilize apenas tipos de dados simples, arrays e
>estruturas simples. Não utilizar classes/bibliotecas que resolveriam o problema diretamente.
>
>Leve em consideração na sua implementação que esta lista pode ter milhões de pessoas.

- Exemplo de uso 1
```
        print "Lista de pessoas em ordem alfabética"
        lista = Pessoas.Criar()
        para i=0 ate Pessoas.Count-1 faça
                print Pessoas.PessoaEmOrdemAlfabetica[i].Nome
        fim
```

- Exemplo de uso 2
```
        nome = read "Digite seu nome"
        lista = Pessoas.Criar()
        index = Pessoas.IndiceDoNome(nome)
        se index=-1 então
                print "Seu nome não está na lista"
        senão
                print "Seu id é:"+Pessoas.PessoaEmOrdemAlfabetica[index].Id
```

- Exemplo de uso 3
```
        nomes = []
        lista = Pessoas.Criar()
        enquanto PegarIdPessoa(out IdPessoa) faça
                index = Pessoas.IndiceDoId(IdPessoa)
                nomes.add(Pessoas.PessoaEmOrdemAlfabetica[index].Nome)
        fim
        ...
```

Código
------
```
Pessoa = estrutura
    Id: Inteiro
    Nome: String
fim

Pessoas = classe
    privado
        Lista: array de Pessoa

        funcao LerUmaPessoa(): Pessoa // não precisa implementar
        procedimento CarregarPessoas()
    público
        construtor Criar()

        funcao IndiceDoId(Id: Inteiro): Inteiro
        funcao IndiceDoNome(Nome: string): Inteiro

        propriedade Count: Inteiro
        propriedade PessoaEmOrdemAlbetica[Indice: Inteiro]: Pessoa
fim
```


Questão 2
=========

> Modele as informações abaixo seguindo boas práticas de orientação a objetos, não precisa fazer diagramas, apresente apenas as classes. Faça a implementação apenas do que achar necessário para o entendimento do que está descrito abaixo:
> 1. Uma carteira de investimentos é formada por um conjunto de investimentos de tipos variados numa certa data.
> 2. Cada investimento de uma carteira possui no mínimo a informação de descrição e o valor investido.
> 3. A descrição de um investimento de uma carteira depende de cada tipo e combina as informações adicionais sobre o investimento.
> 4. Um investimento do tipo ações, possui adicionalmente o nome da ação e a quantidade de ações.
> 5. Um investimento do tipo fundos, possui adicionalmente o nome do fundo, CNPJ do fundo e a quantidade de cotas.
> 6. Um investimento do tipo título de renda fixa, possui adicionalmente o nome do título, se é pré ou pós fixado e, se for pré fixado possui o valor da taxa de juros, se for pós fixado possui um texto adicional.


Implementação Questao 1
=======================

Principais pontos
-----------------

Foi criado o módulo pessoas.py, que implementa a estrutura de dados Pessoa, a classe Pessoas e todo os códigos necessários para a Questão 1.

Para implementacão dos métodos de classe, resolvi utilizar o padrão de estilo snake case, que é o padrão convencionado pela linguagem de programação python, mas nao é obrigatorio.

Utilizei uma namedtuple para representar a estrutura Pessoa em python, pois é um tipo de dado imutável e indexado, o qual permite acessar os indíces pelo nome, funcionando semelhantemente a um struct.

Criei a classe Pessoas responsável pela manipulação da lista de estrutura do tipo tupla que representa uma Pessoa.

Nos casos de uso apresentados na questão 1, aparentemente o método "Pessoas.Criar( )" efetua a crição de uma instância da classe Pessoas, atribuindo a referência do objeto criado para uma variável de nome **lista**, mas o que aparentemente ocorre é que a própria classe Pessoas carrega a referência do objeto criado, porque todas as chamadas de método de instância passam a ser executadas pela própria classe, e neste ponto surgiram algumas dúvidas. Primeiro, o objeto criado seria referenciado pela variável **lista**, o que não ocorre nos exemplos de uso, pois a variável **lista** não é utilizada em momento algum após a chamada do método "Pessoa.Criar( )". Segundo, se a atribuição da instância foi realizada para a variável **lista**, entao os métodos somente poderiam ser acessados a partir da variável **lista** e nao da classe Pessoa, como ocorre em todos os exemplos de uso.

Na especificação do código informa que o método criar é um construtor, o que também gerou outra dúvida, pois métodos contrutores geralmente não retornam valores, a não ser a referência do objeto construido. Em python, instânciar um objeto é semelhante a efetuar uma chamada de uma função, atribuindo para uma variável que armazena a referência do objeto criado, conforme exemplo a seguir:
```
>>> pessoas = Pessoas()
```
Então, o código acima, os metódos ficam todos acessíveis a partir da variável pessoas, em que foi atribuido a referência do objeto criado.

Desta forma eu decide por não implementar o método "criar", pois o método contrutor da linguagem python é o ```__new__```, que por baixo dos panos ele chama o método inicializador ```__init__```, sendo assim a especifição do codigo é plenamente atendida com a implementação do metodo ```__init__```.
    
Foi implementado a ordenação da lista de pessoas utilizando o algoritmo bubble sort. Não é o algoritmo mais performaticatico para listas muito grandes totalmente desordenadas, porém na maioria das linguagens existem funções e métodos embutidos que implementam ordenações otimizadas.




