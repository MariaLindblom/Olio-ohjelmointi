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
    """Lisää parametrinä annetun asiakkaan asiakkaat-listaan.
        nostaa ValeError:in, jos parametrin tottusarvo on false."""
    asiakkaat.append(Asiakas)
    if Asiakas == False:
      raise ValueError ("Anna asiakas.")
    
  def poista_asiakas(Asiakas):
    try:
      asiakkaat.remove(Asiakas)
    except ValueError:
      pass
    
    
  def tulosta_asiakkaat(self):
    for ihminen in asiakkaat:
      print(ihminen)
    

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
    """Lisää parametrinä annetun edun edut-listaan.
        nostaa ValeError:in, jos parametrin tottusarvo on false."""
    edut.append(etu)
    if etu == False:
      raise ValueError ("Anna etu.")
    
    
  def poista_etu(self):
    try:
      edut.remove(etu)
    except ValueError:
      pass
    
    
  def tulosta_edut(self):
    for asia in edut:
      print(asia)
  
  
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
    #self._asiakasnro = _luo_nro()
    
    
  def _luo_nro(self):
    """Arvoo numeron asiakkaalle."""
    numerot = []
    numerolista = (random.randint(0,9)* 3)
    numerot.append(numerolista)
    return numerot


  def get_nimi(self,nimi):
    """Palauttaa nimen suoraan."""
    return nimi


  def set_nimi(self,nimi):
    if nimi == False:
      raise ValueError("Anna nimi.")


  def get_ika(self,ika):
    """Palauttaa iän suoraan."""
    return ika


  def set_ika(self,ika):
    if ika == False:
      raise ValueError("Anna ikä.")


  def get_asiakasnumero(self,asiakasnro):
    return 


"""
  def set_asiakas(self):
    if nimi and ika == False:
      raise ValueError("Anna uusi nimi tai ikä.")
    if nimi and ika == True:
      pass"""
      
