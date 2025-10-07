

...
lod a odvozene tridy pro vesmirni souboj
...

class lod:
    ...
    zakladni
    ...

    def __init__(self, jmeno, trup, utok, stit, kostka):
        self._jmeno = jmeno
        self._trup = trup
        self._max_trup = trup
        self._utok = utok
        self._stit = stit
        self._kostka = kostka
        self._zprava = ''

    def __str__(self):
        return str(self.jmeno)

    def utoc(self, souper)
        uder = self._utok + self._kostka.hod()
        zprava = f'{self.jmeno} pali kanoli za {uder} HP.'
        self.nastav_zpravu(zprava)
        souper.bran_se(uder)

    def bran_se(self, uder):    
        poskozeni = uder - (self._stit + self._kostka.hod())
        if poskozeni > 0:
            zprava = f'{self._jmeno} utrpela zasah o sile {poskozeni} HP.'
            self._trup -= poskozeni
            if self._trup < 0:
                self.trup = 0
                zprava = f'{zprava[:-1]} a byla znicena'
        else:


    def nastav_zpravu(self,zprava):
        self._zprava = zprava       

    def vypis zpravy(self):
        return self._zprava
