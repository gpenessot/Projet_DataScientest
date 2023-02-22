import streamlit as st


title = "Classification d’images de biopsie du col de l’utérus"
sidebar_name = "Introduction"


def run():

    st.image("https://storage.googleapis.com/kaggle-competitions/kaggle/11848/logos/header.png")

    st.title(title)

    st.markdown("---")

    st.markdown(
        """
        #### Notre projet avait pour but de classifier des images de biopsie de col de l’utérus pour détecter la présence d’un cancer et le cas échéant, d’en déterminer son grade.

        En effet, le cancer du col de l’utérus est l’un des rares cancers pour lequel le stade précurseur persiste de nombreuses années avant d’évoluer vers un authentique cancer invasif, ce qui peut offrir un temps suffisant pour le détecter et le traiter. Une détection précoce permet donc de sauver potentiellement des vies avant une dégradation plus avancée où les chances des patients se réduisent.

        Pour cela, la société [**Ummon HealthTech**](https://www.ummonhealthtech.com/) nous a fourni un dataset d’images extraites de biopsie.

        """
    )
