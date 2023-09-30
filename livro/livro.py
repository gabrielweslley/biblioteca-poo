class Livro:
    def __init__(self, id, autor, titulo, ano_publi):
        self.__livro_id = id
        self.__autor = autor
        self.__titulo = titulo
        self.__ano_publi = ano_publi
        self.__disponivel = True

    def estaDisponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print("Livro emprestador com sucesso")
        else:
            print("Livro indisponivel")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print("Livro devolvido a estante")
        else:
            print("O livro ja esta devolvido!")


    @property
    def ano_publi(self):
        return self.__ano_publi

    @ano_publi.setter
    def ano_publi(self, value):
        self.__ano_publi = value

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        self.__autor = value

    @property
    def livro_id(self):
        return self.__livro_id

    @livro_id.setter
    def livro_id(self, value):
        self.__livro_id = value

