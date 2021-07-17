import unittest

def suite():   
    return unittest.TestLoader().discover("Produtos.tests", pattern="*.py")