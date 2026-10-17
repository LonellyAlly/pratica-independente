algoritmo "UtilidadesIndependentes"

funcao dobrar(valor: real): real
inicio
   retorne valor * 2
fimfuncao

funcao eh_par(numero: inteiro): logico
inicio
   se numero % 2 = 0 entao
      retorne verdadeiro
   senao
      retorne falso
   fimse
fimfuncao

procedimento saudacao(nome: caractere)
inicio
   escreval("Olá, ", nome, "! Bem-vindo(a).")
fimprocedimento

var
   resultado_dobro: real
   numero_teste: inteiro
inicio
   saudacao("Carlos")
   
   resultado_dobro <- dobrar(15)
   escreval("O dobro de 15 é: ", resultado_dobro)
   
   numero_teste <- 10
   se eh_par(numero_teste) entao
      escreval("O número ", numero_teste, " é par.")
   senao
      escreval("O número ", numero_teste, " não é par.")
   fimse
fimalgoritmo
