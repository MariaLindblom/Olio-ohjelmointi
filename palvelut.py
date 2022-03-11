import random

class Palvelu:
  """Luokka, joka kuvaa palvelua.
        :ivar tuotenimi: tuotteen nimi
        :type tuotenimi: str
        :ivar asiakkaat: lista asiakkaista 
        :type asiakkaat: list

        Julkiset metodit
            lisaa_asiakas(asiakas)
            poista_asiakas(asiakas)
            tulosta_asiakkaat(asiakas)

        Salatut metodit
            luo_asiakasrivi(asiakas)
        """  
  
  def __init__(self,tuotenimi):
    """Konstruktori"""
    self.tuotenimi = tuotenimi
    self._asiakkaat = asiakkaat = []
    
  def __luo_asiakasrivi(Asiakas):
      pass
    
    
  def lisaa_asiakas(Asiakas):
    """Lisää parametsrinä annetun asiakkaan asiakkaat-listaan."""
    asiakkaat += asiakas
    
  def poista_asiakas(Asiakas):
      pass
    
    
  def tulosta_asiakkaat():
      pass
    

class ParempiPalvelu(Palvelu):
  """Luokka, joka kuvaa parempaa palvelua.
        :ivar edut: paremman palvelun edut
        :type edut: str

    Julkiset palvelut
    lisaa_etu
    poista_etu
    tulosta_edut
"""
  
  def __init__(self, tuotenimi):
    """Konstruktori."""
    super().__init__(tuotenimi)
    self._edut = edut =[]
    
  def lisaa_etu():
      pass
    
    
  def poista_etu():
      pass
    
    
  def tulosta_edut():
      pass
  
  
class Asiakas:
  """Luokka, joka kuvaa asiakasta.
        :ivar nimi: asiakkaan nimi
        :type nimi: str
        :ivar asiakasnro: asiakkaan numero
        :type asiakasnro: int[]
        :ivar ika: asiakkaan ikä
        :type ika: int

        Yksityiset metodit
        luo_nro()
    """
  
  def __init__(self, nimi, ika):
    """Konstruktori."""
    self._nimi = nimi
    self._ika = ika
    self._asiakasnro = luo_nro()
    
    
  def _luo_nro():
    """Arvoo numeron asiakkaalle."""
    numerot = []
    random.randint(0,9)
    
