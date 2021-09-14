"""
    Tässä sovelluksessa kysytään kaksi kokonaislukua
    ja tulostetaan niiden suurin yhteinen tekijä.
    Sovellus antaa virheilmoituksen, jos ei syötetä
    kahta syötettä samalta rivitä tai syötteet eivät
    ole kokonaislukuja.
    Sovellus lopetetaan, kun syötteeksi annetaan enter-painallus.
"""

def main():
    """Pääohjelmafunktio main()

        Pääohjelmafunktio sisältää pääohjelmasilmukan,
        jossa kysytään kaksi kokonaislukua ja
        lasketaan niiden suurin yhteinen tekijä
        käyttäen syt-funktiota.
        Pääohjelmafunktiossa tarkastetaan myös
        syötteiden oikeellisuus.
        
        Kutsuparametrit
        ---------------
        Ei kutsuparametreja
        
        Paluuparametrit
        ---------------
        Ei paluuparametreja
        
        Poikkeukset
        -----------
        ValueError - generoituu, kun int-muunnoksessa oleva arvo ei ole kokonaisluku
    """
    
    # pääohjelmasilmukka pythonilla
    while True:
        rivi = input("Anna kaksi kokonaislukua: ")
        
        # silmukan lopetus tyhjällä rivillä
        if len(rivi) == 0:
            break
        
        # jäsennellään syöterivilta erilliset syötteet
        # ja käsitellään virheelliset syötteet
        try:
            # syöterivin jäsentely
            luvut = rivi.split()
            
            # lasketaan ja tulostetaan syt, jos syötteet ovat oikein
            if len(luvut) == 2:
                print(syt(int(luvut[0]), int(luvut[1])))
                
            #tulostetaan virheilmoitus, jos syötteitä ei ole kaksi
            else:
                print("Lukuja ei ole kaksi!")
                
        # tulostetaan virheilmoitus, jos syötteistä jompi kumpi
        # tai molemmat eivät ole kokonaislukuja
        except ValueError:
            print("Luvut eivät ole kokonaislukuja!")
        except:
            print("Tulikin tuntematon virhe")
    
    # tulostetaan lopuksi ohjelman lopetusteksti
    print("Lopetetaan")
    
def syt(a: int, b: int) -> int:
    """Suurimman yhteisen tekijän laskentafunktio syt(a, b)

        Funktio laskee sille välitettyjen kahden luvun
        suurimman yhteisen tekijän käyttäen Eukleideen algoritmia.
        Laskenta tehdään iteroiden while-silmukassa.
        
        Kutsuparametrit
        ---------------
        a: int - ensimmäinen kokonaisluku
        b: int - toinen kokonaisluku
        
        Paluuparametrit
        ---------------
        syt: int - laskettu suurin yhteinen tekijä
        
        Poikkeukset
        -----------
        Ei käsiteltyjä poikkeuksia
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
            
    return a + b

if __name__ == "__main__":
    main()
