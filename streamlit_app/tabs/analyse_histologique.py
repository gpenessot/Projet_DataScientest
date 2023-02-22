import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


title = "Analyse histologique et grade du cancer"
sidebar_name = "Analyse histologique"


def run():

    st.title(title)

    st.markdown(
        """
## Analyse du grade de cancer

Afin de déterminer la présence ou non d&#39;un cancer et le stade, le cas échéant, de celui-ci, on analyse des zones précises de tissus des lames photographiées. On appelle _histologie_ la discipline de la médecine qui étudie les tissus biologiques.

Attention à ne pas confondre deux notions distinctes :

- Le _stade_ d&#39;un cancer correspond à un état d&#39;avancement « géographique ».
- Le _grade_ correspond à l&#39;agressivité du tissu cancéreux.
"""
    )

    st.image(Image.open("assets/rappel_1.png"))

    st.markdown("""
Ci-dessus, une image en noir et blanc pour clarifier a quoi correspondent les 3 principales différentes zones épithéliales et leur intérêt respectif dans la gradation finale (+ ou -):

- les noyaux (zone foncées) - organites intracellulaires (+)
- les cytoplasmes (zones grisées) - &quot;vide&quot; intracellulaire (+)
- les zones vides sans éléments (zones blanches) - &quot;vide&quot; extracellulaire (-)

Pour déterminer le grade, nous devons :

- Repérer la zone d&#39;intérêt :
  - l&#39;épithélium
  - la lame basale (qui le sépare du tissu de support ou tissu conjonctif)
- Regarder le pourcentage de l&#39;épithélium en partant de la base (au-dessus de la lame basale) qui contient des cellules atypiques ou dont l&#39;agencement est atypique.
- Le grade retenu dans ce travail sera :
  - 0 si pas de cancer
  - entre 1 et 3 si détection d&#39;un cancer en fonction du ratio de cellule atypique dans l&#39;épithélium

Ci-dessous, des exemples d&#39;images labellisées (grossissement x40) :

- (A) **Grade 1**  : Cellules atypiques dans le tiers inférieur
- (B) **Grade 2**  : Cellules atypiques dans les deux tiers inférieurs de l&#39;épithélium.
- (C) **Grade 3**  : L&#39;entièreté de l&#39;épithélium est remplie de cellules atypiques,
- (D) **Grade « 0 »**  : Aucune cellule atypique, épithélium normal, pas de cancer
"""
    )

    st.image(Image.open("assets/rappel_4.png"))

    st.markdown("""
Il faut savoir que le système de notation des cancers est complexe et qu&#39;il varie en fonction du type de cancer, l&#39;approche ici décrite n&#39;est pas applicable en l&#39;état à tous les cancers.

## Caractéristiques des « cellules atypiques »

Une _cellule atypique_ est une cellule qui n&#39;aura pas les caractéristiques attendues d&#39;une cellule saine a une certaine localisation du tissu.

Plus le cancer est avancé, plus la multiplication des cellules sera anormale :

- multiplication plus rapide
- moins les cellules arriveront à leur forme finale normale, donc elles seront moins _différenciées_ en termes de structure donc moins on trouvera des structures différentes en fonction de la localisation

La différenciation est le critère le plus facile à détecter visuellement.
"""
    )

    st.image(Image.open("assets/Epithelium.jpg"))

    st.markdown("""
Pour rappel, voici le modèle théorique d&#39;un épithélium sain avec la lame basale en bas.
 On voit bien qu&#39;en fonction de la position géographique des cellules, les cellules vont avoir des structures différentes. Les cellules proches de la lame basale possèdent un gros noyau, sont de forme ronde et sont peu différenciées. Plus on s&#39;éloigne de la lame basale (et on se rapproche de la lumière vaginale), plus le noyau rapetisse, les cellules se déforment (s&#39;allongent). Elles &quot;meurent&quot; (_apoptose_ - mort physiologique) et finissent par desquamer (mortes, elles rejoignent la lumière vaginale).

D&#39;autres critères en dérivent mais sont moins aisés à distinguer visuellement :

- forme des noyaux
- mitoses atypiques

## Partenariat avec la société « Ummon HealthTech »

Ce travail a été fait en partenariat avec la société « Ummon HealthTech », société spécialisée dans l&#39;amélioration des soins médicaux par une amélioration de la détection des cancers, qui nous a fourni le jeu de données.

Ce projet est lié à des données confidentielles, et nous avons signé un engagement de confidentialité.

## Complexité du domaine fonctionnel

Comme on peut le voir, le contexte fonctionnel de notre projet est très complexe car c&#39;est en fait un domaine de spécialité de la médecine. La société « Ummon HealthTech » nous a fourni une formation fonctionnelle pour introduire ces différents concepts.

Monter en compétence sur ce domaine a demandé un très grand investissement de notre part.

En termes d&#39;arrière-plan sur ce domaine, un seul participant du projet avait des connaissances préalables en médecine (vétérinaire), mais même pour lui, cela restait un domaine de spécialité sur lequel il n&#39;a pas été formé en détail et dont il n&#39;avait pas toutes les clés.

Que ce soit donc tant du côté scientifique (médecine) que du côté technique (apprentissage profond), nous partions donc de 0 et avons nécessité un long ramp-up. Ce projet était en effet en décalage complet avec nos métiers quotidiens sur tous ces aspects.
        """
    )
