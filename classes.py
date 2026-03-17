class animal():
    def __init__(self, nome, idade, som): # "self" se usa quando vai declarar a variavel propria da classe
        self.nome = nome
        self.idade = idade
        self.som = som

    def info(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")

    def fala(self):
        return f"{self.som}"

class mamifero(animal):
    def __init__(self, nome, idade, som, habitat):
        super().__init__(nome, idade, som) #em "super" se coloca as caracteristicas herdadas da principal
        self.habitat = habitat

class reptil(animal):
    def __init__(self, nome, idade, som, alimento):
        super().__init__(nome, idade, som) 
        self.alimento = alimento

class zoologico():
    def __init__(self):
        self.bichos = []

    def add_animais(self, animal):
        self.bichos.append(animal)


    def listar_animais(self):
        for i in self.bichos:
            print(i.nome)
            print(i.som)