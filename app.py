import streamlit as st
from calculate import calculer_production
from rotation import generer_rotation
from visualization_2d import afficher_plan_2d
from visualization_3d import afficher_plan_3d
from config import GRAINES
from optimisation_plateaux import generer_configurations_standard

st.set_page_config(page_title="Simulateur Fourrage Hydroponique", layout="wide")
st.title("🌱 Simulateur Hydroponique Pro")

if "local_verrouillé" not in st.session_state:
    st.session_state.local_verrouillé = False
if "dimensions" not in st.session_state:
    st.session_state.dimensions = {
        "hauteur": 2.5, "longueur": 5.0, "largeur": 4.0
    }

with st.sidebar:
    st.header("Paramètres de culture")

    with st.expander("📐 Dimensions du local", expanded=True):
        if not st.session_state.local_verrouillé:
            st.session_state.dimensions["hauteur"] = st.number_input("Hauteur (m)", 1.0, 5.0, st.session_state.dimensions["hauteur"])
            st.session_state.dimensions["longueur"] = st.number_input("Longueur (m)", 1.0, 10.0, st.session_state.dimensions["longueur"])
            st.session_state.dimensions["largeur"] = st.number_input("Largeur (m)", 1.0, 10.0, st.session_state.dimensions["largeur"])
        else:
            st.markdown(f"- Hauteur : **{st.session_state.dimensions['hauteur']} m**")
            st.markdown(f"- Longueur : **{st.session_state.dimensions['longueur']} m**")
            st.markdown(f"- Largeur : **{st.session_state.dimensions['largeur']} m**")

        verrou = st.checkbox("🔒 Verrouiller les dimensions", value=st.session_state.local_verrouillé)
        st.session_state.local_verrouillé = verrou

    graine = st.selectbox("🌾 Type de graine", list(GRAINES.keys()))
    plateau_L = st.number_input("Longueur plateau (m)", 0.3, 1.2, 0.8)
    plateau_l = st.number_input("Largeur plateau (m)", 0.2, 1.0, 0.4)
    hauteur_niveau = st.number_input("Hauteur entre niveaux (m)", 0.2, 0.7, 0.35)
    objectif = st.number_input("🎯 Objectif journalier (kg)", 10.0, 1000.0, 500.0)

params = {
    "hauteur": st.session_state.dimensions["hauteur"],
    "longueur": st.session_state.dimensions["longueur"],
    "largeur": st.session_state.dimensions["largeur"],
    "plateau_L": plateau_L,
    "plateau_l": plateau_l,
    "hauteur_niveau": hauteur_niveau,
    "graine": graine,
    "objectif": objectif
}

result = calculer_production(params)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Résultats")
    st.metric("Plateaux requis", result['plateaux_requis'])
    st.metric("Racks nécessaires", result['racks'])
    st.metric("Production estimée", f"{result['production_jour']:.1f} kg/jour")
    st.write(f"Niveaux par rack : {result['niveaux']}")
    st.write(f"Plateaux par niveau : {result['plateaux_par_niveau']}")
    st.write(f"Surface occupée estimée : {result['surface_occupée']:.2f} m²")
    if result['objectif_atteint']:
        st.success("✅ Objectif de production atteint")
    else:
        st.warning("⚠️ Objectif NON atteint")

with col2:
    st.subheader("🔁 Planning de rotation (7 jours)")
    rotation = generer_rotation(result["plateaux_total"])
    for jour, infos in rotation.items():
        if jour == "J0":
            st.markdown(f"**{jour}** — Stock initial de plateaux : **{infos['stock_initial']}**")
        else:
            st.markdown(
            f"**{jour}** ➤ "
            f"Semis : `{infos['semis']}` | "
            f"Pousse : `{infos['pousse']}` | "
            f"Récolte : `{infos['récolte']}` | "
            f"Stock restant : `{infos['stock_restant']}`"
        )


st.divider()
st.subheader("🧱 Visualisation 2D")
afficher_plan_2d(result["racks"], result["niveaux"], result["plateaux_par_niveau"])

st.subheader("📦 Visualisation 3D")
afficher_plan_3d(result["racks"], result["niveaux"], result["plateaux_par_niveau"])
