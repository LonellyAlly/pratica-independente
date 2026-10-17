algoritmo "ListaSegura"

var
   lista_original, nova_lista: vetor[1..3] de caractere
   i: inteiro

inicio
   // Inicializando a lista original com 2 itens (e um espaço vazio no índice 3)
   lista_original[1] <- "Maçã"
   lista_original[2] <- "Banana"
   lista_original[3] <- ""

   // Copiando os itens para a nova lista de forma "segura"
   para i de 1 ate 2 faca
      nova_lista[i] <- lista_original[i]
   fimpara
   
   // Adicionando o novo item apenas na nova lista copiada
   nova_lista[3] <- "Uva"

   escreval("Lista Original (intacta):")
   para i de 1 ate 3 faca
      se lista_original[i] <> "" entao
         escreval("- ", lista_original[i])
      fimse
   fimpara

   escreval("")
   escreval("Nova Lista (modificada):")
   para i de 1 ate 3 faca
      escreval("- ", nova_lista[i])
   fimpara
fimalgoritmo
