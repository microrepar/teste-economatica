# Economatica

Teste
-----

O objetivo deste teste é avaliar seu conhecimento em programação básica, estrutura de dados e
programação orientada a objeto.

As duas questões do teste são totalmente independentes.

Se tiver dúvida de algo, escreva a dúvida claramente, tome uma decisão, escreva qual foi sua decisão e
prossiga baseado na sua decisão.

Você pode continuar usando uma linguagem de algoritmo genérico (como está abaixo) ou também pode
usar uma linguagem real à sua escolha. O importante não é o código executar, o importante é estar correto e
mostrar sua linha de raciocínio.


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

> Modele as informações abaixo seguindo boas práticas de orientação a objetos, não precisa fazer diagramas,
> apresente apenas as classes. Faça a implementação apenas do que achar necessário para o entendimento
> do que está descrito abaixo:
> 1. Uma carteira de investimentos é formada por um conjunto de investimentos de tipos variados numa
> certa data.
> 2. Cada investimento de uma carteira possui no mínimo a informação de descrição e o valor investido.
> 3. A descrição de um investimento de uma carteira depende de cada tipo e combina as informações
> adicionais sobre o investimento.
> 4. Um investimento do tipo ações, possui adicionalmente o nome da ação e a quantidade de ações.
> 5. Um investimento do tipo fundos, possui adicionalmente o nome do fundo, CNPJ do fundo e a
> quantidade de cotas.
> 6. Um investimento do tipo título de renda fixa, possui adicionalmente o nome do título, se é pré ou pós
> fixado e, se for pré fixado possui o valor da taxa de juros, se for pós fixado possui um texto adicional.



