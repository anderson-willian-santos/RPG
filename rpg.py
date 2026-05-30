class Personagem:

    def __init__(self, nome, vida, ataque, defesa):

        self.nome = nome.upper()
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def status(self):
        print('- FICHA DE PERSONAGEM -')
        print(f'Nome: {self.nome}\nVida: {self.vida}\nAtaque: {self.ataque}\nDefesa: {self.defesa}')
        print('-' * 20)

    def acao(self):
        print(f"Turno de {self.nome}")
        print("1 - Atacar   2 - Pular   3 - Fichas")


    def atacar(self, inimigo):
        print(f'{self.nome} atacou {inimigo.nome} com {self.ataque} de ataque!')
        inimigo.receber_dano(self.ataque)
    
    def receber_dano(self, dano):
        dano -= self.defesa
        print(f'DEFESA absorveu parte do dano')
        self.vida = self.vida - dano
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nome} recebeu {dano} de dano. Vida atual de {self.nome}: {self.vida}')
    
    def vivo(self):
        return self.vida > 0

p1 = Personagem('Elf', 100, 20, 15)
p2 = Personagem('Joel', 90, 35, 10)

while p1.vivo() and p2.vivo():
    p1.acao()
    escolha = int(input("Sua escolha: "))
    print()
    if escolha == 1:
        p1.atacar(p2)
        print()
    elif escolha == 3:
        p1.status()

    p2.acao()
    escolha = int(input("Sua escolha: "))
    print()
    if escolha == 1:
        p2.atacar(p1)
        print()
    elif escolha == 3:
        p2.status()

print()

if p1.vivo():
    print(f'{p1.nome} ganhou a batalha!')
else:
    print(f'{p2.nome} ganhou a batalha!')
