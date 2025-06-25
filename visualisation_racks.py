import streamlit as st

def afficher_rack_vertical(niveaux, hauteur_dispo, hauteur_plateau, marge_hauteur=0.3):
    hauteur_totale = niveaux * hauteur_plateau
    depassement = hauteur_totale > (hauteur_dispo - marge_hauteur)

    st.markdown(f"**Rack vertical ({niveaux} niveaux × {hauteur_plateau:.2f} m)**")

    # Affichage visuel
    for i in range(niveaux, 0, -1):
        st.markdown("🟩 Niveau " + str(i))
    
    if depassement:
        st.error(f"❌ Trop haut ! ({hauteur_totale:.2f} m > {hauteur_dispo - marge_hauteur:.2f} m utilisables)")
    else:
        st.success(f"✅ OK — Hauteur totale : {hauteur_totale:.2f} m / Espace max : {hauteur_dispo - marge_hauteur:.2f} m")
