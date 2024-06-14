#Questao 1
class Livro:
    livros=[]
    def __init__(self,titulo,autor,ano_publicacao):
        self._titulo=titulo
        self._autor=autor
        self._ano_publicacao=ano_publicacao
        self._disponivel=True
        Livro.livros.append(self)
    #Questao 2
    def __str__(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Ano de Publicação: {self._ano_publicacao}"
    
   #Questao 3
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Livro emprestado com sucesso!")
        else:
            print("Este livro já está emprestado.")
# Questao 4
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        return livros_disponiveis

