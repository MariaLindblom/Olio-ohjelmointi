import random

class Palvelu:
  """Luokka, joka kuvaa palvelua.
        :ivar tuotenimi: tuotteen nimi
        :type tuotenimi: str
        :ivar asiakkaat: lista asiakkaista 
        :type asiakkaat: list

        Julkiset metodit
            lisaa_asiakas(Asiakas)
            poista_asiakas(Asiakas)
            tulosta_asiakkaat

        Suojatut metodit
            luo_asiakasrivi(Asiakas)
        """  
  
  def __init__(self,tuotenimi):
    """Konstruktori"""
    self.tuotenimi = tuotenimi
    self.__asiakkaat = asiakkaat = []
    
    
  def _luo_asiakasrivi(self,asiakas):
    """Luo asiakasrivin getterreitten saamilla tiedoilla."""
    f'{asiakas.get_nimi()} ({get_asiakasnro}) on {get_ika}-vuotias.'
    
    
  def lisaa_asiakas(self,asiakas):
    """Lisää parametrinä annetun asiakkaan asiakkaat-listaan.
        nostaa ValeError:in, jos parametrin totuusarvo on false."""
    asiakkaat.append(asiakas)
    if asiakas == False:
      raise ValueError ("Anna asiakas.")
    
    
  def poista_asiakas(self,asiakas):
    """Poistaa parametrinä annetun asiakkaan,
        jos asiakasta ei ole asiakkaat-listassa ohitetaan ValueError."""
    try:
      asiakkaat.remove(asiakas)
    except ValueError:
      pass
    
    
  def tulosta_asiakkaat(self):
    """Tulostaa asiakas-listan jokaisen asiakkaan käyttämällä
        luo_asiakasrivi metodia."""
    for ihminen in asiakkaat:
      print(self._luo_asikasrivi(asiakas))
    

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
    self.__edut = edut =[]
    
    
  def lisaa_etu(self):
    """Lisää parametrinä annetun edun edut-listaan.
        nostaa ValeError:in, jos parametrin totuusarvo on false."""
    edut.append(etu)
    if etu == False:
      raise ValueError ("Anna etu.")
    
    
  def poista_etu(self):
    """Poistaa parametrinä annetun edun,
        jos etua ei ole edut-listassa ohitetaan ValueError."""
    try:
      edut.remove(etu)
    except ValueError:
      pass
    
    
  def tulosta_edut(self):
    """Käy läpi ja palauttaa edut-listan jokaisen edun."""
    for asia in edut:
      print(asia)
  
  
class Asiakas:
  """Luokka, joka kuvaa asiakasta.
        :ivar nimi: asiakkaan nimi
        :type nimi: str
        :ivar asiakasnro: asiakkaan numero
        :type asiakasnro: int,list
        :ivar ika: asiakkaan ikä
        :type ika: int

        Yksityiset metodit
        luo_nro()
    """
  
  def __init__(self, nimi, ika):
    """Konstruktori."""
    self._nimi = nimi
    self.__ika = ika
    self.__asiakasnro = self.__luo_nro()
    
    
  def __luo_nro(self):
    """Arvoo kahdeksan numeora sisältävät listan asiakkaalle."""
    numerot = []
    numero = 0
    while numero < 8:
      numerot.append(random.randint(0,9))
      numero += 1
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


  def get_asiakasnro(self,asiakasnro):
    return 
    
