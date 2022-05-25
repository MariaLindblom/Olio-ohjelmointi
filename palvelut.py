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
    
    
  def _luo_asiakasrivi(self,Asiakas):
    """Luo asiakasrivin getterreitten saamilla tiedoilla."""
    f'{Asiakas.get_nimi()} ({Asiakas.get_asiakasnro()}) on {Asiakas.get_ika()}-vuotias.'
    
    
  def lisaa_asiakas(self,Asiakas):
    """Lisää parametrinä annetun asiakkaan asiakkaat-listaan.
        nostaa ValeError:in, jos parametrin totuusarvo on false."""
    self.__asiakkaat.append(Asiakas)
    if Asiakas == False:
      raise ValueError ("Anna asiakas.")
    
    
  def poista_asiakas(self,Asiakas):
    """Poistaa parametrinä annetun asiakkaan,
        jos asiakasta ei ole asiakkaat-listassa ohitetaan ValueError."""
    try:
      self.__asiakkaat.remove(Asiakas)
    except ValueError:
      pass
    
    
  def tulosta_asiakkaat(self):
    """Tulostaa asiakas-listan jokaisen asiakkaan käyttämällä
        luo_asiakasrivi metodia."""
    for ihminen in self.__asiakkaat:
      print(ihminen)
      #(self._luo_asiakasrivi(Asiakas))
    

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
    self.__edut = edut = []
    
    
  def lisaa_etu(self, etu):
    """Lisää parametrinä annetun edun edut-listaan.
        nostaa ValeError:in, jos parametrin totuusarvo on false."""
    self.__edut.append(etu)
    if etu == False:
      raise ValueError ("Anna etu.")
    
    
  def poista_etu(self,etu):
    """Poistaa parametrinä annetun edun,
        jos etua ei ole edut-listassa ohitetaan ValueError."""
    try:
      self.__edut.remove(etu)
    except ValueError:
      pass
    
    
  def tulosta_edut(self):
    """Käy läpi ja palauttaa edut-listan jokaisen edun."""
    for asia in self.__edut:
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
    numerot = [random.randint(0,100) for i in range(3)]
    return numerot
  

  def set_nimi(self,nimi):
    if self._nimi == False:
      raise ValueError("Anna nimi.")
    else:
        asiakasnimi = self._nimi


  def get_nimi(self, asiakasnimi):
    """Palauttaa nimen suoraan."""
    return asiakasnimi
  

  def set_ika(self,asiakas_ika):
    if self.__ika == False:
      raise ValueError("Anna ikä.")
    else:
        asiakas_ika = self.__ika

    
  def get_ika(self,asiakas_ika):
    """Palauttaa iän suoraan."""
    return asiakas_ika

  
  def get_asiakasnro(self,asiakasnro):
    return f'{self.__luo_nro:08}' #ei toimi
