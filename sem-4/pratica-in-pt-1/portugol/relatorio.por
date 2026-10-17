algoritmo "ProcessamentoDeNomes"
var
   nomesDigitados: vetor[1..100] de caractere
   nomesUnicos: vetor[1..100] de caractere
   qtdDigitados, qtdUnicos: inteiro
   i, j: inteiro
   nomeAtual, aux: caractere
   repetido: logico

inicio
   qtdDigitados <- 0
   qtdUnicos <- 0

   escreval("Digite os nomes (digite FIM para encerrar):")
   repita
      escreva("Nome: ")
      leia(nomeAtual)
      se nomeAtual <> "FIM" entao
         qtdDigitados <- qtdDigitados + 1
         nomesDigitados[qtdDigitados] <- nomeAtual
         repetido <- falso
         para i de 1 ate qtdUnicos faca
            se nomesUnicos[i] = nomeAtual entao
               repetido <- verdadeiro
            fimse
         fimpara
         se repetido = falso entao
            qtdUnicos <- qtdUnicos + 1
            nomesUnicos[qtdUnicos] <- nomeAtual
         fimse
      fimse
   ate (nomeAtual = "FIM") ou (qtdDigitados = 100)

   se qtdUnicos > 0 entao
      para i de 1 ate qtdUnicos - 1 faca
         para j de 1 ate qtdUnicos - i faca
            se nomesUnicos[j] > nomesUnicos[j+1] entao
               aux <- nomesUnicos[j]
               nomesUnicos[j] <- nomesUnicos[j+1]
               nomesUnicos[j+1] <- aux
            fimse
         fimpara
      fimpara

      escreval("")
      escreval("--- Relatório Final ---")
      escreval("Total de nomes digitados: ", qtdDigitados)
      escreval("Total de nomes únicos: ", qtdUnicos)
      escreval("Lista ordenada:")
      para i de 1 ate qtdUnicos faca
         escreval("- ", nomesUnicos[i])
      fimpara
      escreval("Extremos (Primeiro, Último): (", nomesUnicos[1], ", ", nomesUnicos[qtdUnicos], ")")
   senao
      escreval("Nenhum nome foi registrado.")
   fimse
fimalgoritmo
