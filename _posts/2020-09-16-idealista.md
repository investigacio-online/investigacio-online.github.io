---
title: Extractor Informació Idealista
author: investigacio-online
date: 2020-09-16
categories: [Eines,Pròpies]
tags: [fase3,adquisició,Linux,idealista]
---

Eina que permet extreure informació dels habitatges o locals que estan a la venda o per llogar a [Idealista](https://www.idealista.com) i les agències que els gestionen.

# Informació
* **Dificultat d'instal·lació**: mitjana
* **Dificultat d'ús**: fàcil
* **Utilitat en investigació**: útil en la fase d'adquisició
* **Coneixements previs**: saber utilitzar una terminal

# Característiques
* Crea un CSV amb tots els habitatges d'una zona determinada.
* Crea un CSV de totes les agències que gestionen els habitatges d'una zona determinada.
* El CSV es pot importar fàcilment a un Excel o similars.

# Instal·lació
## Programa
Pots descarregar-te el programa del Github de Projecte Nadki:
* Repositori: [enllaç](https://github.com/projectenadki/Extractor-Idealista)

També pots utilitzar la comanda "git" des d'una terminal:
```
git clone https://github.com/projectenadki/Extractor-Idealista.git
```

## Requisits
Primer de tot, has d'instal·lar Python3 si no el tens:
```
sudo apt install python3
```

Per a poder instal·lar tots els requisits fàcilment, pots utilitzar pip3:
```
sudo apt install python3-venv python3-pip
```

A continuació, has d'instal·lar tots els paquets específics per a poder executar el programa:
* BeautifulSoup4
* datetime
* argparse
* progress

Pots instal·lar cada requisit manualment executant:
```
pip3 install <NOM_PAQUET>
```

Si vols anar més de pressa, al repositori hi ha un fitxer anomenat "requisits.txt". Si el baixes i executes la següent comanda, s'instal·laran tots els requisits automàticament:
```
pip3 install -r requisits.txt
```

Finalment, només caldrà executar el programa:
```
python3 idealista.py
```

# Funcionament
## Idealista
Aquesta eina utilitza la informació que hi ha a [Idealista](https://www.idealista.com).

Específicament, l'apartat on apareixen els pisos una vegada has escollit la província, ciutat i zona:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-16-idealista/ideal1.png)

## Atributs
El programa té diversos atributs que pots utilitzar quan l'executes:
* **--url**: una vegada has buscat la zona, copia la URL i enganxa-la després d'aquest atribut.
* **-n** o **--nombre**: especifica el nom del fitxer que vols que tinguin els CSV. Si no especifiques l'atribut, generarà un nom automàticament combinant el nom de la zona i la data.
* **-a** o **--agencias**: indica si vols obtenir informació sobre les agències de la zona. Per una banda, generarà un altre CSV amb informació específica i per l'altra, actualitzarà les dades sobre les agències del CSV que conté el llistat d'habitatges.

## Execució
A continuació indiquem com executar el programa amb els diferents atributs. Perquè puguis veure les diferències, utilitzarem els habitatges de Devesa (Girona) com a exemple.

La manera més fàcil és indicar només l'URL:
```
python3 idealista.py --url URL
```

Posant com a URL [https://www.idealista.com/alquiler-viviendas/girona/devesa/](https://www.idealista.com/alquiler-viviendas/girona/devesa/), obtenim un fitxer, que es pot obrir amb l'Excel o similars, que conté un llistat de tots els habitatges que et mostra l'URL que has indicat:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-16-idealista/ideal3.png)

Com pots veure, la majoria dels camps d'agència (nom, carrer i codi postal) estan buits. Això és degut al fet que no s'ha pogut obtenir tota la informació necessària de primeres.

L'atribut **-a** o **--agencies** fa una segona recopilació (pot tardar una mica) per obtenir informació sobre les agències:
```
python3 idealista.py --url URL -a
```

Per una banda, completa els camps que estaven buits del document amb el llistat d'habitatges:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-16-idealista/ideal2.png)

I per l'altra, crea un nou document amb informació més detallada sobre les agències trobades:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-16-idealista/ideal4.png)

Per últim, amb l'atribut **-n** o **--nombre** pots especificar un nom en concret que tindran els fitxers creats. Per defecte, tenen el format "zona\_[listado o agencias]\_data":
* devesa_listado_16_09_2020.csv
* devesa_agencias_16_09_2020.csv

Si especifiques un nom, en lloc de posar la zona, posarà el nom:
* Nadki_listado_16_09_2020.csv
* Nadki_agencias_16_09_2020.csv

```
python3 idealista.py --url URL -n Nadki
```

## Errors
Si utilitzes el programa mentre estàs connectat a un Wi-Fi públic o al de casa teva, no hauries de tenir problemes. No obstant això, si et connectes a través d'una VPN, és possible que vegis el següent error:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-16-idealista/err1.png)

Això és degut al fet que Idealista bloqueja tot el tràfic provinent de Tor o de VPNs. Per a poder executar correctament el programa, hauràs d'obrir la pestanya incògnit d'un navegador i entrar a Idealista.

Veuràs que en lloc de sortir-te la pàgina web en si, et sortirà un missatge dient que no saben si ets un robot i et faran resoldre un CAPTCHA de Google:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-16-idealista/err2.png)

Una vegada resolt, ja podràs utilitzar el programa amb normalitat. Normalment t'obligaran a resoldre el CAPTCHA la primera vegada que et connectis i passat un temps.

# Conclusions
A [Idealista](https://www.idealista.com) pots trobar habitatges i locals que estan en venda i lloguer. Depenent de la zona que t'interessi, pots ser bastant feixuc haver d'anar passant pàgines i perdre la pista dels pisos que t'interessen.

Amb aquest programa podràs exportar tots els pisos a un Excel per a poder filtrar ràpidament per preu, habitacions o zona. Si algun t'interessa, és tan fàcil com copiar l'enllaç i enganxar-lo al navegador per veure els detalls a la web.

A més a més, amb els resultats que s'obtenen, tant de pisos com d'agències, es poden fer estudis en l'àmbit d'habitatge per saber la tendència dels preus o quines agències predominen a la zona.