Algoritmo "ExercicioIntegrador"
Var
   nomesDigitados: vetor[1..100] de caractere
   nomesUnicos: vetor[1..100] de caractere
   entrada, continuar, aux: caractere
   totalDigitados, totalUnicos, i, j: inteiro
   repetido: logico

Inicio
   totalDigitados <- 0
   continuar <- "s"
   Enquanto (continuar = "s") e (totalDigitados < 100) Faca
      Escreva("Digite um nome: ")
      Leia(entrada)
      totalDigitados <- totalDigitados + 1
      nomesDigitados[totalDigitados] <- entrada
      Escreva("Deseja adicionar outro nome? (s/n): ")
      Leia(continuar)
   FimEnquanto
   totalUnicos <- 0
   Para i de 1 ate totalDigitados Faca
      repetido <- Falso
      Para j de 1 ate totalUnicos Faca
         Se nomesDigitados[i] = nomesUnicos[j] Entao
            repetido <- Verdadeiro
         FimSe
      FimPara
      Se Nao repetido Entao
         totalUnicos <- totalUnicos + 1
         nomesUnicos[totalUnicos] <- nomesDigitados[i]
      FimSe
   FimPara
   Para i de 1 ate totalUnicos - 1 Faca
      Para j de 1 ate totalUnicos - i Faca
         Se nomesUnicos[j] > nomesUnicos[j+1] Entao
            aux <- nomesUnicos[j]
            nomesUnicos[j] <- nomesUnicos[j+1]
            nomesUnicos[j+1] <- aux
         FimSe
      FimPara
   FimPara
   Escreval("")
   Escreval("--- RELATÓRIO FINAL ---")
   Escreval("Total de nomes digitados: ", totalDigitados)
   Escreval("Total de nomes únicos: ", totalUnicos)
   Escreval("Lista Ordenada:")
   Para i de 1 ate totalUnicos Faca
      Escreval(" - ", nomesUnicos[i])
   FimPara
   Se totalUnicos > 0 Entao
      Escreval("Tupla simulada (Primeiro, Último): (", nomesUnicos[1], ", ", nomesUnicos[totalUnicos], ")")
   FimSe
FimAlgoritmo
