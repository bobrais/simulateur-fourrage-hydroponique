
# visualization_2d.py
import streamlit as st
import matplotlib.pyplot as plt



def afficher_plan_2d(racks, niveaux, plateaux_par_niveau):
    fig, ax = plt.subplots(figsize=(10, 6))
    for r in range(racks):
        for n in range(niveaux):
            for p in range(plateaux_par_niveau):
                rect = plt.Rectangle((r * 2 + p * 0.25, n), 0.2, 0.9, color="green")
                ax.add_patch(rect)
    ax.set_title("Disposition 2D des racks")
    ax.set_xlabel("Disposition horizontale")
    ax.set_ylabel("Niveaux")
    ax.set_xlim(0, racks * 2 + plateaux_par_niveau * 0.25)
    ax.set_ylim(0, niveaux + 1)
    plt.tight_layout()
    st.pyplot(fig)
