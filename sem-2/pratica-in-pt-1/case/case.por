algoritmo "MenuOperacoes"
var
   opcao_escolhida: caractere
   primeiro_numero, segundo_numero, resultado_operacao: real

inicio
   escreval("Menu de Operações:")
   escreval("1 - Adição")
   escreval("2 - Subtração")
   escreval("3 - Multiplicação")
   escreval("4 - Divisão")
   
   escreva("Escolha uma operação (1-4): ")
   leia(opcao_escolhida)
   
   escreva("Insira o primeiro número: ")
   leia(primeiro_numero)
   escreva("Insira o segundo número: ")
   leia(segundo_numero)
   
   escolha opcao_escolhida
      caso "1"
         resultado_operacao <- primeiro_numero + segundo_numero
         escreval("Resultado da adição: ", resultado_operacao)
      caso "2"
         resultado_operacao <- primeiro_numero - segundo_numero
         escreval("Resultado da subtração: ", resultado_operacao)
      caso "3"
         resultado_operacao <- primeiro_numero * segundo_numero
         escreval("Resultado da multiplicação: ", resultado_operacao)
      caso "4"
         se segundo_numero = 0 entao
            escreval("Erro: Não é possível dividir por zero.")
         senao
            resultado_operacao <- primeiro_numero / segundo_numero
            escreval("Resultado da divisão: ", resultado_operacao)
         fimse
      outrocaso
         escreval("Opção inválida.")
   fimescolha
fimalgoritmo
