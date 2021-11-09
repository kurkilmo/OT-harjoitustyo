import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 0.25")

    def test_saldo_vahenee_oikein_kun_saldo_riittaa(self):
        self.maksukortti.ota_rahaa(4)
        self.assertEqual(str(self.maksukortti), "saldo: 0.06")

    def test_ei_muutu_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_palautus_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def test_palautus_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)
