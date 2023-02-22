import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


title = "Le cancer du col de l'utérus"
sidebar_name = "Le cancer du col de l'utérus"


def run():

    st.title(title)

    st.markdown(
        """
## La cellule

La _cellule_ est l&#39;unité fondamentale de la vie, le corps humain en comprend entre 50 et 100 millions de millions. On trouve dans notre organisme environ 200 types de cellules aux formes, tailles, et fonctions très diverses.

Une cellule humaine comporte trois régions principales :

- la _membrane plasmique_ : elle forme la limite extérieure de la cellule.
- le _cytoplasme_ : liquide intracellulaire dans lequel baignent des _organites_ (petites structures assurant certaines fonctions à l&#39;intérieur de la cellule).
- le _noyau_ : un organite qui régit toutes les activités de la cellule.
  - il contient les _gènes_ qui contiennent notre patrimoine génétique possédant entre autres les instructions nécessaires à l&#39;élaboration des protéines de l&#39;organisme
  - il traite une extraordinaire complexité en faisant à la fois le travail d&#39;un ordinateur, d&#39;un architecte, d&#39;un chef de chantier et d&#39;un conseil d&#39;administration
"""
    )

    st.image(Image.open("assets/cellule.jpg"))

    st.markdown("""
## Les tissus

Un _tissu_ est un ensemble de cellules qui ont une structure semblable et qui remplissent des fonctions identiques ou analogues.
"""
    )

    st.image(Image.open("assets/tissus.jpg"))

    st.markdown("""
Nous voyons que quatre tissus primaires s&#39;enchevêtrent pour former la trame du corps humain, nous nous concentrerons par la suite sur le _tissu épithélial_ présent, entre-autres, au niveau du col de l&#39;utérus.

Ci-dessous un schéma d&#39;un _épithélium_ (tissu épithélial) sain :

- la partie haute de l&#39;épithélium est la partie externe, en contact avec la lumière vaginale (et donc, avec le mucus vaginal et l&#39;air extérieur).
- l&#39;épithélium est l&#39;&quot;empilement&quot; de cellules de l&#39;imagedont la structure globale va différer en fonction de leur positionnement, de leur composition interne, de leur forme, etc
- tout en bas, l&#39;épithélium repose sur la « _lame basale_ » qui sépare l&#39;épithélium du tissu conjonctif sous-jacent (en dessous). Ce dernier contient les vaisseaux sanguins, entre-autres, par lesquels sont acheminés les nutriments essentiels à son fonctionnement.
"""
    )

    st.image(Image.open("assets/Epithelium.jpg"))

    st.markdown("""
## Le cancer

Une cellule normale est « programmée » pour se diviser (par _mitose_) un nombre limité de fois, entre 50 et 70 fois. Lorsque les mécanismes normaux de régulation de ce processus n&#39;ont plus d&#39;effet sur la division des cellules, celles-ci se reproduisent de façon incontrôlée et donnent naissance à une masse anormale appelée _néoplasme_ (« nouvelle croissance »).

On distingue 2 types de néoplasmes :

- Les néoplasmes bénins : strictement localisés et de masse compacte souvent encapsulées, ont une croissance plutôt lente et tuent rarement leur hôte si on les retire avant qu&#39;ils compriment un organe vital.
- Les néoplasmes malins : des masses non encapsulées à croissance rapide et qui peuvent _métastaser_, c&#39;est-à-dire être à l&#39;origine de néoplasmes secondaires.

A l&#39;origine des cancers se trouve le phénomène de _mutation_. Il s&#39;agit de modifications quantitatives ou qualitatives de l&#39;_ADN_ (la substitution d&#39;une seule base azotée par une autre est parfois suffisante) qui altèrent l&#39;expression de certains gènes.

L&#39;organisme dispose de mécanismes pour contrecarrer ces phénomènes et la majorité des mutations ne produisent pas de cancer, cependant ils peuvent être débordés.

Plusieurs facteurs peuvent contribuer à ces mutations :

- Certains facteurs physiques comme des traumatismes mécaniques ou des rayonnements (UV, etc).
- Certaines infections virales ou bactériennes
- Plusieurs substances chimiques nocives qui peuvent pénétrer dans l&#39;organisme :
  - goudron du tabac
  - pollutions diverses de l&#39;air, de l&#39;eau ou de l&#39;alimentation
- Des facteurs héréditaires génétiques


## Le cancer du col de l&#39;utérus

Le cancer du col utérin (CCU) est un cancer invasif qui se développe à partir de l&#39;épithélium du col de l&#39;utérus :

- Il se développe lentement et dans une immense majorité des cas après une infection persistante par un papillomavirus humain ou un virus sexuellement transmissible.
- Plus de 1100 femmes meurent chaque année de ce cancer en France
- Ce cancer du col est l&#39;un des rares cancers pour lequel le stade précurseur (lésion précancéreuse) persiste de nombreuses années avant d&#39;évoluer vers un authentique cancer invasif, ce qui peut offrir un temps suffisant pour le détecter et le traiter.

On appelle les cancers des tissus épithéliaux des _carcinomes_.


## Processus d&#39;obtention d&#39;image pour analyse des tissus

Parmi les différentes techniques de dépistage du cancer de l&#39;utérus, la _biopsie_ (prélèvement d&#39;un fragment de tissu présumé cancéreux) intra-utérine est recommandée pour caractériser précisément le _grade_ du cancer (nous expliquons plus loin comment le déterminer).

Le tissu prélevé est ensuite étalé sur une _lame_ en une couche unicellulaire.

Ces lames sont ensuite séchées et colorées. Le processus de coloration est un processus complexe de plusieurs étapes faisant appel à l&#39;humain. Le temps de trempage dans les solutions est un facteur important car ils vont impacter le degré de coloration donc la gamme et l&#39;intensité de couleur finales.

Les 2 colorants les plus importants utilisés lors de ce processus sont :

- l&#39;_hématoxyline_ : couleur bleu ou bleu-noir
- l&#39;_éosine_ : couleur orange-rosée
"""
    )

    st.image(Image.open("assets/coloration.png"))

    st.markdown("""
Ci-dessus :

- un exemple de séquence de coloration
- des lames trempant dans de l&#39;hématoxyline durant une de ces étapes.

Les lames sont ensuite photographiées et stockées dans des images de très large dimension : couramment aux alentours de 100.000 \* 100.000 pixels.

Du fait de leur énorme taille (en Giga octets), elles doivent être manipulées par des techniques logicielles spécifiques pour ne pas déborder les capacités mémoire de la machine, par exemple à l&#39;aide de la librairie open slide ([https://openslide.org/](https://openslide.org/)).

Même un processus standardisé va avoir de multiples facteurs amenant beaucoup de variabilité dans l&#39;image finale obtenue :

- géométrie finale :
  - La technique de prélèvement choisie par le praticien va être déterminante pour la localisation finale des différentes zones : épithélium, lame basale, tissu de support de l&#39;épithélium.
  - des déformations mécaniques s&#39;y ajoutent avec la manipulation du prélèvement et sa pose sur la lame
- espace colorimétrique final impacté en plus par :
  - processus de coloration utilisé
  - produits utilisés
  - opérateurs humains sur des bains de colorants ou le temps est un facteur sensible
- netteté de l&#39;image :
  - réglage de l&#39;appareil de prise de la photo

De ce fait, des lames provenant d&#39;un _centre d&#39;analyse_ particulier seront en général assez homogènes (on devrait être à iso processus, opérateurs et matériels) mais on aura quand même de la variabilité. Entre 2 centres d&#39;analyse, la variation peut être grande.

Ci-dessous, un exemple de lame complète avec la zone d&#39;intérêt au centre où se trouve l&#39;épithélium est indiquée, nous allons détailler la méthode d&#39;analyse dans la section suivante.
"""
    )

    st.image(Image.open("assets/cervix_lame_complete.jpg"), width=400)

    
