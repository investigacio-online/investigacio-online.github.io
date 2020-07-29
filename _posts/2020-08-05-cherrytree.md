---
title: CherryTree
author: investigacio-online
date: 2020-08-05
categories: [Eines,Notes]
tags: [notes,fase3,adquisició,fase4,processament,fase5,anàlisis,Windows,Linux,MacOS]
---

CherryTree és un organitzador que utilitza un esquema jeràrquic que permet escriure text, afegir imatges, taules i enllaços. A més a més, permet exportar totes les notes en format PDF.

# Informació
* **Dificultat d'instal·lació**: fàcil
* **Dificultat d'ús**: fàcil
* **Utilitat en investigació**: útil en totes les fases
* **Coneixements previs**: ofimàtica bàsica

# Característiques
Algunes de les característiques que té són les següents:
* Programari lliure i gratuït
* Permet utilitzar text enriquit (negreta, subratllat, cursiva, colors...)
* Permet afegir sintaxi per ressaltar diversos llenguatges de programació
* Emmagatzemar les notes en format sqlite o xml.
* Permet afegir contrasenya per guardar les notes xifrades
* Disponible en molts idiomes
* Interfície d'usuari personalitzable
* Funcionalitat de cerca global en totes les notes
* Permet importar i exportar notes. Es poden exportar en HTML o PDF

# Aplicació a les investigacions
CherryTree és una eina molt útil per centralitzar i a l'hora organitzar tota la informació que vagis trobant.

Té una barra superior, molt similar a la del Word, on pots escollir el format del text, el color, inserir enllaços, imatges, taules, etc. El panell de l'esquerre és on hi haurà tots els nodes distribuïts en arbre. I al mig, és on pots apuntar tot el que vulguis:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-08-05-cherrytree/cherry4.png)

Pots crear nodes per apuntar qualsevol cosa. Per exemple, un anomenat "Investigació X" per escriure tot el que fa referència amb els requisits inicials i estat de la investigació:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-08-05-cherrytree/cherry5.png)

Al panell de l'esquerra pots afegir tants nodes com vulguis. Cada node serà una nota diferent. A més a més, com que està distribuït en arbre, pots crear nodes que formen part d'altres nodes i mantenir tota la informació organitzada:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-08-05-cherrytree/cherry6.png)

Pots guardar el document en dos formats diferents: SQLite i XML. A no ser que vulguis processar el document amb una eina automàtica, t'hauria de ser indiferent quin format escollir. El que sí que hauries de decidir és si vols posar-li contrasenya:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-08-05-cherrytree/cherry7.png)

Per últim, si t'interessés pots exportar un node o tot l'arbre en PDF:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-08-05-cherrytree/cherry8.png)

I també en HTML. Si ho fessis així, hauràs de crear una carpeta nova on es guardaran tots els fitxers necessaris per crear l'HTML. Finalment, només hauràs d'executar el fitxer anomenat *index.html* i se t'obrirà al navegador:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-08-05-cherrytree/cherry9.png)

# Instal·lació
CherryTree és multiplataforma. Està disponible en Windows, Linux i Mac OS. En Linux hi ha diversos mètodes d'instal·lació que pots utilitzar.

## Windows
Pots obtenir l'arxiu d'instal·lació a la pàgina de descàrrega que t'indiquem a les referències.

Té una versió portable per si només vols executar el programa sense instal·lar-lo:

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-08-05-cherrytree/cherry1.png)

És tan fàcil com descarregar l'arxiu i instal·lar el programa:
1. Descarrega't l'executable (extensió .exe)
2. Executa'l
3. Selecciona el llenguatge
4. Accepta la llicència
5. Selecciona el directori on vols que s'instal·li el programa
6. Indica si vols crear un accés directe a l'escriptori
7. Revisa el resum i assegura't que tot estigui bé
8. Completa la instal·lació

## Linux
### Debian
La manera més fàcil és fer-ho a través de la terminal amb snapd:
```
sudo apt update
sudo apt install snapd
sudo snap install cherrytree
```

També pots fer-ho manualment, però és més complicat:
1. Instal·lar dependències
```
sudo apt install wget python-dbus python-chardet python-enchant libcanberra-gtk-module libgtksourceview2.0-0 libgtksourceview2.0-common python-cairo python-gobject-2 python-gtk2 python-numpy
```
2. Descarregar *python-gtksourceview2*
```
https://pkgs.org/download/python-gtksourceview2
```
3. Instal·lar *python-gtksourceview2*
```
sudo dpkg -i python-gtksourceview2_XXX_amd64.deb
```
4. Descarrega CherryTree

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-08-05-cherrytree/cherry2.png)

5. Instal·lar CherryTree
```
sudo dpkg -i cherrytree_XXX_all.deb
```

Nota: substituir XXX per la versió que t'hagis descarregat

### Ubuntu
Igual que amb Debian, pots instal·lar-ho de forma manual. Una alternativa més visual és utilitzar Ubuntu Software:
1. Obrir l'aplicació de Ubuntu Software
2. Anar a la pestanya "Other Software"
3. Afegir el següent text:
```
ppa:giuspen/ppa
```
4. Clicar "Add Source" i introduir la contrasenya d'administrador
5. Confirmar que el PPA s'ha afegit correctament

![](https://raw.githubusercontent.com/investigacio-online/investigacio-online.github.io/master/img/2020-08-05-cherrytree/cherry3.png)

6. Clicar "Reload" i introduir la contrasenya per instal·lar les actualitzacions
7. Obrir una altra vegada el "Ubuntu Software" i buscar "Cherrytree"
8. Seleccionar l'aplicació i instal·lar-la

## Mac OS
Malauradament, no existeix actualment un paquet preparat per instal·lar CherryTree al sistema operatiu Mac OS fàcilment.

La manera més fàcil és utilitzar un programa com [*PlayOnMac*](https://www.playonmac.com/en/) que virtualitza aplicacions de Windows perquè es puguin utilitzar en Mac OS.

Instal·la *PlayOnMac*, descarrega l'executable per Windows i instal·la'l mitjançant *PlayOnMac*.

Una alternativa és utilitzar Port a través de la terminal, tot i que no és una versió oficial:
1. Instal·lar X11 server si no el tens instal·lat:
```
sudo port -v -N install xorg-server
```
2. Instal·lar el CherryTree:
```
sudo port -v install cherrytree
```

# Referències
* **Github CherryTree**: [enllaç](https://github.com/giuspen/cherrytree)
* **Característiques CherryTree**: [enllaç](https://www.giuspen.com/cherrytree/#features)
* **Descàrrega CherryTree**: [enllaç](https://www.giuspen.com/cherrytree/#downl)
* **MAnual instal·lació CherryTree**: [enllaç](https://giuspen.com/cherrytreemanual/#_installation)
* **PlayOnMac**: [enllaç](https://www.playonmac.com/en/)