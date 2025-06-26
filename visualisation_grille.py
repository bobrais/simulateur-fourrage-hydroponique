def afficher_grille_racks(nb_lignes, nb_colonnes):
    """
    Affiche une grille simplifiée des racks au sol : nb_lignes × nb_colonnes
    Chaque rack est représenté par une 🟫 dans une case centrée.
    """
    st.markdown(f"**🧱 Grille au sol : {nb_lignes} lignes × {nb_colonnes} colonnes = {nb_lignes * nb_colonnes} racks**")

    for i in range(nb_lignes):
        ligne = " ".join(["🟫" for _ in range(nb_colonnes)])
        st.markdown(f"<div style='font-size:1.5em; text-align:center;'>{ligne}</div>", unsafe_allow_html=True)
