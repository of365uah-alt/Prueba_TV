class Enemigos:
    def __init__(self):
        self.vida = 0
        self.danno = 0
        self.dinero = 0
        self.exp = 0

    def set_vida(self,vida):
        self.vida = vida

    def set_dinero(self,dinero):
        self.dinero = dinero

    def set_exp(self,exp):
        self.exp = exp

    def set_danno(self,danno):
        self.danno = danno

    def info(self):
        return self.vida, self.dinero, self.exp, self.danno

    def recibir_danno(self,danno):
        self.vida -= danno
        if self.vida <= 0:
            self.vida = 0
            return True
        else:
            return False
