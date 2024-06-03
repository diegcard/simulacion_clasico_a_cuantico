import cal_matrix_cpmx as cal
import unittest
import Lib
import numpy as np
"""
-------- Archivo de Testeo de pruebas de la libreria -------
"""

class TestLibVecSpace(unittest.TestCase):

    def test_marbles_1(self):
        """test 1: marbles1"""
        matrix = [[(9, 8, 5), (1, 2, 3), (4, 12, 1)], [(4, 12, 1), (6, 5, 6), (5, 1, 9)], [(4, 12, 1), (1, 3, 9), (6, 5, 6)]]
        vector = [(5, 6, 9), (4, 2, 4), (1, 9, 6)]
        clicks = 2
        sum_ver = [(-4801, 102), (-3936, 778), (-4123, -163)]
        sum_doc = Lib.marble(matrix,vector,clicks)
        self.assertEqual(sum_doc, sum_ver)

    def test_marbles_2(self):
        """test 1: marbles2"""
        matrix = [[(9, 8), (1, 3)], [(4, 12), (5, 9)]]
        vector = [ (4, 2), (1, 6)]
        clicks = 4
        sum_ver = [(-14541, -256383), (138324, -486520)]
        sum_doc = Lib.marble(matrix,vector,clicks)
        self.assertEqual(sum_doc, sum_ver)
        """------------------------------------------------------------------------------------"""
    def test_multiple_slits_1(self):
        """test 1: marbles2"""
        matrix = [[(9, 8), (1, 3)], [(4, 12), (5, 9)]]
        vector = [ (4, 2), (1, 6)]
        clicks = 2
        sum_ver = [921.31, 1850.85]
        sum_doc = Lib.multiple_slits(matrix,vector,clicks)
        self.assertEqual(sum_doc, sum_ver)

    def test_multiple_slits_2(self):
        """test 1: marbles2"""
        matrix = [[(9, 8, 5), (1, 2, 3), (4, 12, 1)], [(4, 12, 1), (6, 5, 6), (5, 1, 9)], [(4, 12, 1), (1, 3, 9), (6, 5, 6)]]
        vector = [(5, 6, 9), (4, 2, 4), (1, 9, 6)]
        clicks = 1
        sum_ver = [185.88, 167.36, 182.48]
        sum_doc = Lib.multiple_slits(matrix,vector,clicks)
        self.assertEqual(sum_doc, sum_ver)




if __name__ == '__main__':
    unittest.main()
