algoritmo "SistemaCadastros"
var
   comando_usuario, nome_pessoa, tipo_cadastro: caractere
   quantidade_lote, idade_pessoa, total_cadastros: inteiro
   qtd_aluno, qtd_professor, qtd_funcionario, iterador_lote, iterador_lista: inteiro
   nomes_cadastrados: vetor[1..100] de caractere

inicio
   total_cadastros <- 0
   qtd_aluno <- 0
   qtd_professor <- 0
   qtd_funcionario <- 0
   comando_usuario <- ""
   enquanto comando_usuario <> "sair" faca
      escreval("")
      escreva("Digite 'c' para continuar ou 'sair' para encerrar: ")
      leia(comando_usuario)
      se comando_usuario <> "sair" entao
         escreva("Quantos cadastros deseja realizar agora? ")
         leia(quantidade_lote)
         para iterador_lote de 1 ate quantidade_lote faca
            escreval("")
            escreva("Nome: ")
            leia(nome_pessoa)
            escreva("Idade: ")
            leia(idade_pessoa)
            se idade_pessoa < 0 entao
               escreval("Erro: Idade inválida.")
            senao
               se idade_pessoa < 18 entao
                  escreval("Erro: Cadastro negado. A idade mínima é 18 anos.")
               senao
                  escreva("Tipo (1 - Aluno, 2 - Professor, 3 - Funcionário): ")
                  leia(tipo_cadastro)
                  escolha tipo_cadastro
                     caso "1"
                        qtd_aluno <- qtd_aluno + 1
                        total_cadastros <- total_cadastros + 1
                        nomes_cadastrados[total_cadastros] <- nome_pessoa
                        escreval("Aluno(a) cadastrado(a) com sucesso!")
                     caso "2"
                        qtd_professor <- qtd_professor + 1
                        total_cadastros <- total_cadastros + 1
                        nomes_cadastrados[total_cadastros] <- nome_pessoa
                        escreval("Professor(a) cadastrado(a) com sucesso!")
                     caso "3"
                        qtd_funcionario <- qtd_funcionario + 1
                        total_cadastros <- total_cadastros + 1
                        nomes_cadastrados[total_cadastros] <- nome_pessoa
                        escreval("Funcionário(a) cadastrado(a) com sucesso!")
                     outrocaso
                        escreval("Erro: Tipo de cadastro inválido.")
                  fimescolha
               fimse
            fimse
         fimpara
      fimse
   fimenquanto

   escreval("")
   escreval("--- RESUMO DOS CADASTROS ---")
   escreval("Quantidade total de cadastros: ", total_cadastros)
   escreval("Alunos: ", qtd_aluno)
   escreval("Professores: ", qtd_professor)
   escreval("Funcionários: ", qtd_funcionario)
   escreval("")
   escreval("Lista dos nomes cadastrados:")
   para iterador_lista de 1 ate total_cadastros faca
      escreval("- ", nomes_cadastrados[iterador_lista])
   fimpara
fimalgoritmo
