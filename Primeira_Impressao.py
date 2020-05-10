from unittest import TestCase, main
from abvr import Eh_Par, soma, sub


class Teste(TestCase):
    def teste_Soma(self):
        self.assertEqual(soma(5,5),10)

    def Teste_Eh_Par(self):
        self.assertEqual(Eh_Par(3), True)

    #def Teste_Eh_Da_String(self):
    #    self.assertEqual(Eh_Par("string"),False)
    
    def teste_Sub(self):
        self.assertEqual(sub(10,10),0)


    #def teste_Soma_Errada(self):
    #    self.assertEqual(soma(5,5),11)
    


if __name__ == "__main__":
    Eh_Par(3)
    main()
    pass