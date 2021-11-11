import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_luotu_kassapaate_rahat_oikein(self):
        self.assertEqual(self.kassapaate.kassassarahaa(), 100000)

    def test_luotu_kassapaate_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat_maara(), 0)

    def test_luotu_kassapaate_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset_maara(), 0)

    def test_kateinen_kassa_kasvaa_oikein_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassarahaa(), 100240)

    def test_kateinen_kassa_kasvaa_oikein_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassarahaa(), 100400)

    def test_kateinen_vaihtoraha_oikein_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_kateinen_vaihtoraha_oikein_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(600), 200)

    def test_kateinen_edulliset_kasvavat(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset_maara(), 1)
    
    def test_kateinen_maukkaat_kasvavat(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat_maara(), 1)
    
    def test_kateinen_ei_riita_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassarahaa(), 100000)
        self.assertEqual(self.kassapaate.edulliset_maara(), 0)

    def test_kateinen_ei_riita_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassarahaa(), 100000)
        self.assertEqual(self.kassapaate.maukkaat_maara(), 0)

    def test_kortilta_veloitetaan_edullinen(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(onnistui, True)
        self.assertEqual(str(self.maksukortti), "saldo: 2.6")

    def test_kortilta_veloitetaan_maukas(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(onnistui, True)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_edullisten_maara_kasvaa_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset_maara(), 1)

    def test_maukkaiden_maara_kasvaa_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat_maara(), 1)

    def test_kortilla_ei_rahaa_edullinen(self):
        maksukortti = Maksukortti(100)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(onnistui, False)
        self.assertEqual(str(maksukortti), "saldo: 1.0")
        self.assertEqual(self.kassapaate.edulliset_maara(), 0)

    def test_kortilla_ei_rahaa_maukas(self):
        maksukortti = Maksukortti(300)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(onnistui, False)
        self.assertEqual(str(maksukortti), "saldo: 3.0")
        self.assertEqual(self.kassapaate.maukkaat_maara(), 0)

    def test_kortilla_kassan_rahamaara_ei_muutu(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassarahaa(), 100000)

    def test_kortin_saldo_muuttuu_kassan_rahat_kasvavat(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 300)
        self.assertEqual(self.kassapaate.kassassarahaa(), 100300)
        self.assertEqual(str(self.maksukortti), "saldo: 8.0")

    def test_kortin_saldo_ei_muutu_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassarahaa(), 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
        

    
        