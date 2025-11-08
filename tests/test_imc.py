import unittest

from main import resultat, nom
from utils import valider_entree
from utils import interpretation_resultat
class Test(unittest.TestCase):
    def test_valider_entree(self):
        self.assertEqual(valider_entree(10,300),True)

    def test_interpretation_resultat(self):
        self.assertEqual(interpretation_resultat(resultat))
