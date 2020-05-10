from unittest import TestCase, main

def soma(x,y):
    return x + y
def subtracao(x, y):
    return x - y

class Teste(TestCase):
    def teste_Soma(self):
        self.assertEqual(soma(5,5),10)
    def teste_subtracao():
        self.assertEqual(sub(5,5),0)
    #def teste_Soma_Errada(self):
    #    self.assertEqual(soma(5,5),11)
    


if __name__ == "__main__":
    main()
    pass