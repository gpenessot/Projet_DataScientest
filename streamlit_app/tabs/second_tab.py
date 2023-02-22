import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


title = "Jeu de données"
sidebar_name = "Jeu de données"


def run():

    st.title(title)

    st.markdown(
        """
        ## Histopathologies
        
        La société **Ummon HealthTech** est propriétaire de ce dataset. Le jeu de données contient 5.926 images issues de biopsies du col de l’utérus. Ces images étaient extraites de lames complète et le grade associé donné par un expert.
        
        #### Echantillon d'images

        Ci-après quelques images de chaque grade pour donner une idée de leur diversité (orientation générale de l’organisation épithéliale, couleur (intensité et gamme), etc) et de la difficulté à analyser ces images.

        """
    )

    st.image(Image.open("assets/echantillon.png"))

    st.markdown("""
        ## Analyse des images

        #### Distribution des images par type et grade

        Le nom des images est la concaténation des métadonnées suivantes :
        * Identification du centre médical où a été produit la lame : CXX_
        * Identification de la lame d’où a été tirée l’image : BXX_SXX_
        * Numéro de l’image extraite sur cette lame : XX

        Le grade du cancer pour chaque image était donné dans un fichier .csv associé au jeu de données.

        Ci-après quelques visualisations de base pour comprendre la structure du jeu de données.



    """)


    image1 = Image.open("assets/repartition_type.png")
    image2 = Image.open("assets/repartition_grade.png")

    col1, col2 = st.columns(2)
    #col1.header("Répartition par type")
    col1.image(image1, use_column_width=True)
    #col2.header("Répartition par grade")
    col2.image(image2, use_column_width=True)

    st.markdown("""
    
    #### Nombre d'images par centre de prélèvement
    
    Le nombre d'images par centre est très variable. 
    

    """)

    st.image(Image.open("assets/nombre_img_par_centre.png"))

    st.markdown("""
    #### Taille des images en fonction du centre ou elles ont été prises
    """)

    st.image(Image.open("assets/taille-images.png"))

    st.markdown("""
#### Représentation de la répartition des grades des images au sein de quelques lames
    """)

    st.image(Image.open("assets/repartition_lames.png"))

    st.markdown("""
On peut avoir pour plusieurs images extraites de la même lame des grades différents car la zone épithéliale n&#39;est pas atteinte partout au même niveau. En cas de diagnostic, le grade de la lame globale serait le grade le plus élevé trouvé sur les sous parties de la lame.

#### Comparaison de l&#39;intensité de couleur moyenne de l&#39;image en fonction de cancer ou non
    """)

    st.image(Image.open("assets/distribution_couleurs.png"))

    st.markdown("""
On constate qu&#39;évidemment, plus le grade est avancé, plus l&#39;image tendra en moyenne vers des couleurs plus sombres, car le nombre de cellules sera en moyenne plus élevé donc l&#39;image comporte plus de zones sombres associées aux noyaux et cytoplasmes.

Cependant, ce n&#39;est pas un critère suffisant en soi pour caractériser un grade avec un modèle simple sur cette simple base du fait de multiples niveaux de variations :

- dus aux processus de coloration variables (nous avons évoqué qu&#39;ils sont très variables entre centres, et aussi au sein d&#39;un centre à moindre niveau)
- du pourcentage de représentation de différentes zones variables :
  - zone blanche sans cellule
  - zone de l&#39;épithélium qui nous intéresse
  - zone de la couche du tissu de support

#### Autres analyses non détaillées

Nous avons également utilisé d&#39;autres visualisations des images dans leur totalité, pour pouvoir analyser les variations en fonction des centres et des grades.

Il en ressort qu&#39;il y a vraiment une grande variabilité et une grande difficulté à donner un grade pour un être humain non expert du domaine.

Nous avons aussi regardé des images de lames complètes en python en utilisant la librairie « open slide ».

Toutes les images de notre dataset sont censées représenter pour un pixel la même taille dans la réalité car le zoom et la méthode de prise de cliché de la lame sont censés être homogènes.


## Pertinence des datas

Concernant la qualité de notre dataset, sur la _volumétrie_, nous pouvons déjà remarquer que 5.926 images ne constituent pas une grande volumétrie de data pour de la classification avec réseaux de neurones profonds.

Ensuite sur la _qualité des notes du grade_ des images, elle est censée être bonne car faite par des opérateurs humains, experts du domaine.

Cependant, nous avons découvert lors de notre phase d&#39;analyse des images certains artefacts dans les images qui nous ont fait douter du niveau de qualité du dataset.

Voici des exemples d&#39;images présentes dans notre dataset et comportant des artefacts :

- image avec des plis de tissus (1 et 2)
- image vide (3)
- image avec des éléments apparemment &quot;parasites&quot; (4 et 5)
    """)

    col1, col2, col3 = st.columns(3)
    col1.image(Image.open("assets/C19_B028_S21_4.jpeg"))
    col1.image(Image.open("assets/C02_B198_S21_3.jpeg"))

    col2.image(Image.open("assets/C13_B238_S11_1.jpeg"))
    col2.image(Image.open("assets/C06_B109_S21_1.jpeg"))

    col3.image(Image.open("assets/C10_B003_S10_3.jpeg"))

    st.markdown("""
Ce type d&#39;erreur est très marginal mais il laisse planer quelques doutes sur la manière dont a été constitué le dataset et sur le fait qu&#39;un opérateur humain en ai vérifié/validé le contenu.
    """)



