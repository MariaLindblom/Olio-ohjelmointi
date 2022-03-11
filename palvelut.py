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
    """Lisää parametrinä annetun asiakkaan asiakkaat-listaan."""
    asiakkaat.append(asiakas)
    
  def poista_asiakas(Asiakas):
      pass
    
    
  def tulosta_asiakkaat(self):
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
    
  def lisaa_etu(self):
      pass
    
    
  def poista_etu(self):
      pass
    
    
  def tulosta_edut(self):
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
    
    
  def _luo_nro(self):
    """Arvoo numeron asiakkaalle."""
    numerot = []
    numerot.append(random.randint(0,9))
    return numerot


  def get_asiakas(self):
    return (nimi,ika)


  def set_asiakas(self):
    if nimi and ika == False:
      raise ValueError("Anna uusi nimi tai ikä.")
    if nimi and ika == True:
      return nimi, ika
      
