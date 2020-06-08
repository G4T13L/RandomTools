import unittest

class Caesar():
    abc= "abcdefghijklmnñopqrstuvwxyz"
    abc_op = abc
    def __init__(self, abc="abcdefghijklmnñopqrstuvwxyz"):
        self.abc = abc
        self.abc_op = abc+'\n'+'\t'+' '
        
    def encrypt(self, entrada,rot,opcional=False):
        salida = ""
        if (opcional and (self.abc.find ("\n") or self.abc.find ("\t"))):
            abc = self.abc_op
        else:
            abc = self.abc
        for i in range(len(entrada)):
            if(abc.find (entrada[i])!=-1):
                tmp = abc[(abc.find (entrada[i])+rot)%len(abc)]
                salida+=tmp
                #print (tmp, end="")
            else:
                #print (entrada[i],end="")
                salida+=entrada[i]
        return salida

    def decrypt(self,entrada,rot,opcional=False):
        salida = ""
        if (opcional and (self.abc.find ("\n") or self.abc.find ("\t"))):
            abc = self.abc_op
        else:
            abc = self.abc
        for i in range(len(entrada)):
            if(abc.find (entrada[i])!=-1):
                tmp = abc[(abc.find (entrada[i])-rot)%len(abc)]
                salida+=tmp
                #print (tmp, end="")
            else:
                #print (entrada[i],end="")
                salida+=entrada[i]
        return salida
    
    def encrptydecrypt (self, entrada, rot):
        salida = self.encrypt(entrada,rot)
        return self.decrypt(salida,rot)

abc = "abcdefghijklmnñopqrstuvwxyz"
class my_tests(unittest.TestCase):
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    test = Caesar(abc)

    def test_0(self):
        n = 0
        self.assertEqual(self.texto,self.test.encrptydecrypt(self.texto,n),"esta mal")

    def test_1(self):
        n = 10
        self.assertEqual(self.texto,self.test.encrptydecrypt(self.texto,n),"esta mal")

    def test_4(self):
        n = 13
        self.assertEqual(self.texto,self.test.encrptydecrypt(self.texto,n),"esta mal")

    def test_001(self):
        n = 20
        self.assertEqual(self.texto,self.test.encrptydecrypt(self.texto,n),"esta mal")

    def test_nega(self):
        n = 50
        self.assertEqual(self.texto,self.test.encrptydecrypt(self.texto,n),"esta mal")

if __name__ == '__main__':
    unittest.main()
