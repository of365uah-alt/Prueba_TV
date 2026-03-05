#Programación Orientada a objetos
class enemigo:
    def __init__(self,x,y,vida,danno):
        self.x = x
        self.y = y
        self.vida = vida
        self.danno = danno
    def recibir_danno(self,danno):
        self.vida -= danno
        if self.vida <= 0:
            return False
        return True
    def __len__(self):
        return 4


def main():
    orco = enemigo(100,100,20,4)
    orco.x += 20
    orco.recibir_danno(7)
    print(orco.vida)
    print(len(orco))

    return
main()