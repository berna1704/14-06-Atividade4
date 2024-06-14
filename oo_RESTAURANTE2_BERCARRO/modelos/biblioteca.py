#Questao 5 

from atividade4 import Livro

#Questao 6
livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)

livro1.emprestar()
print("O livro está disponível:", livro1.disponivel)

ano_desejado = 1605
livros_disponiveis = Livro.verificar_disponibilidade(ano_desejado)
print(f"Os livros disponíveis publicados em {ano_desejado} são: {livros_disponiveis}")
