class Cachorro:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 100  # Energia inicial
        self.exaustao = 0   # Exaustão inicial

    def brincar(self):
        if self.energia > 0:
            print(f"{self.nome} está brincando!")
            self.energia -= 20  # Reduz energia ao brincar
            self.exaustao += 10  # Aumenta exaustão ao brincar
            self.verificar_estado()
        else:
            print(f"{self.nome} está muito cansado para brincar!")

    def descansar(self):
        print(f"{self.nome} está descansando...")
        self.energia += 30  # Recupera energia ao descansar
        self.exaustao -= 15  # Reduz exaustão ao descansar
        self.verificar_estado()

    def verificar_estado(self):
        # Garante que a energia e a exaustão não ultrapassem os limites
        if self.energia < 0:
            self.energia = 0
        if self.exaustao < 0:
            self.exaustao = 0
        if self.energia > 100:
            self.energia = 100
        if self.exaustao > 100:
            self.exaustao = 100

        print(f"Estado de {self.nome}: Energia = {self.energia}, Exaustão = {self.exaustao}")

# Exemplo de uso
cachorro1 = Cachorro("Rex", 3)

cachorro1.brincar()
cachorro1.brincar()
cachorro1.descansar()
cachorro1.brincar()
