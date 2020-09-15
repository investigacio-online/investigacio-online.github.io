---
title: Cronograma Botlletins Oficials
author: investigacio-online
date: 2020-09-14
categories: [Eines,Pròpies]
tags: [fase3,adquisició,Linux,cronograma,BORME,BOE,BOPI]
---

Analitza els anuncis dels butlletins oficials BORME, BOE, BOPI, publicats a Empresia i en crea un cronograma.

# Informació
* **Dificultat d'instal·lació**: mitjana
* **Dificultat d'ús**: fàcil
* **Utilitat en investigació**: útil en la fase d'adquisició
* **Coneixements previs**: saber utilitzar una terminal

# Característiques
* Permet crear cronogrames
* Permet personalitzar els intervals de temps dels cronogrames
* Permet abreujar alguns dels anuncis

# Instal·lació
## Programa
Pots descarregar-te el programa del Github de Projecte Nadki:
* Repositori: [enllaç](https://github.com/projectenadki/Cronograma-Butlletins-Oficials)

També pots utiltizar la comanda "git" des d'una terminal:
```
git clone https://github.com/projectenadki/Cronograma-Butlletins-Oficials.git
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
* selenium
* matplotlib
* numpy
* datetime
* argparse

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
python3 cronologia.py
```

# Funcionament
## Empresia
Aquesta eina utilitza la informació que recopila la pàgina [Empresia](https://www.empresia.es/) sobre les empreses.

Específicament, l'apartat d'anuncis dels butlletins oficials:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-14-cronograma/crono1.png)

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-14-cronograma/crono2.png)

## Atributs
El programa té diversos atributs que pots utilitzar tant per executar-lo com per personalitzar el cronograma:
* **--url**: una vegada has buscat l'empresa a Empresia, copia la URL i enganxa-la després d'aquest atribut.
* **-x** o **--ejex**: permet especificar l'interval de l'eix X, en mesos. Si no especifiques res, posarà la data de cada anunci.
* **--año**: per defecte agafa tots els anuncis publicats. Pots utilitzar aquest atribut per especificar un any o període en concret.
* **-n** o **--nombre**: especifica el nom del fitxer que vols que tingui el cronograma. Si no poses l'atribut, generarà un nom automàticament combinant el nom de l'empresa i el període.
* **-a** o **--abreviatura**: si hi ha molts anuncis al cronograma, potser es veu molt atapeït. Si ho executes amb aquest atribut, alguns dels títols sortiran més curts:
	* Nombramientos: N
	* Revocaciones: R
	* Ceses/Dimisiones: C/D
	* Anuncio de reducción de capita: Reducción capita

## Execució
A continuació indiquem com executar el programa amb els diferents atributs. Per a què puguem veure les diferències, utilitzarem l'empresa "GRIFOLS SA" com a exemple.

La manera més fàcil és indicar només l'URL:
```
python3 cronograma.py --url URL
```

Com pots veure, el cronograma està molt ple, ja que hi ha anuncis des del 2005:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-14-cronograma/crono3.png)

Afegint l'atribut **-x** pots fer que l'eix X sigui llegible:
```
python3 cronograma.py --url URL -x INTERVAL_MESOS
```

Per exemple, posant **-x 6** l'eix X només mostrarà la data cada 6 mesos:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-14-cronograma/crono4.png)

Amb l'atribut **-a** aconseguiràs abreujar alguns dels títols i serà tot més llegible:
```
python3 cronograma.py --url URL -x INTERVAL_MESOS -a
```

No obstant això, encara hi ha informació no llegible:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-14-cronograma/crono5.png)

Per a poder fer un estudi més minuciós, pots crear diversos cronogrames, un per cada any per exemple, amb l'atribut **--año**:
```
python3 cronograma.py --url URL --año ANY
```

Si poses només l'any 2019, el cronograma ja és llegible:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-14-cronograma/crono6.png)

A més a més, pots indicar un període en lloc d'un any en concret:
```
python3 cronograma.py --url URL --año ANY1-ANY2
```

Posant **--año 2018-2020**, et mostrarà els anuncis compresos entre el període 2018 i 2020, ambdós inclosos:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-09-14-cronograma/crono7.png)

## Fitxer de text
Juntament amb el cronograma, s'emmagatzema un fitxer de text on podràs trobar tota la informació detallada de cada un dels anuncis que apareixen al cronograma.

# Conclusions
Informació sobre els anuncis publicats la pots trobar a moltes pàgines web, com per exemple a [Empresia](https://www.empresia.es/) o [LibreBOR](https://librebor.me/).

L'eina et permet veure la data on un anunci va ser publicat gràficament. Així pots analitzar, des d'un punt de vista més genèric, el context de l'empresa que estàs investigant.

A més a més, pots fer un seguiment dels canvis de noms que ha fet l'empresa buscant els anuncis que tenen com a títol "Cambio de denominación social" i mirar al fitxer de text el nom exacte.