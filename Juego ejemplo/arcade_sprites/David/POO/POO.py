#Programación Orientada a objetos
class enemigo:
    def __init__(self,x,y,vida,danno):
        self.x = x
        self.y = y
        self.vida = vida
        self.danno = danno
    def recibirDanno(self,danno):
        self.vida -= danno
        return


def main():
    orco = enemigo(100,100,20,4)
    orco.x += 20
    orco.recibirDanno(7)
    print(orco.vida)

    return
main()