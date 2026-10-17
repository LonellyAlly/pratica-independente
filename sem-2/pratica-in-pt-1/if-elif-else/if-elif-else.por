algoritmo "ClassificacaoCliente"
var
   idade_cliente: inteiro
   renda_cliente: real
   classificacao_cliente: caractere

inicio
   escreva("Insira a idade do cliente: ")
   leia(idade_cliente)
   escreva("Insira a renda do cliente: ")
   leia(renda_cliente)
   
   se idade_cliente < 18 entao
      classificacao_cliente <- "Bronze"
   senao
      se renda_cliente >= 10000 entao
         classificacao_cliente <- "Diamante"
      senao
         se renda_cliente >= 5000 entao
            classificacao_cliente <- "Ouro"
         senao
            se renda_cliente >= 2000 entao
               classificacao_cliente <- "Prata"
            senao
               classificacao_cliente <- "Bronze"
            fimse
         fimse
      fimse
   fimse
   
   escreval("Classificação do cliente: ", classificacao_cliente)
fimalgoritmo
