# optimisation_plateaux.py

def generer_configurations_standard(
    longueur_dispo,
    largeur_dispo,
    hauteur_dispo,
    hauteur_plateau=0.35,
    tailles_plateaux=[(0.7, 0.3), (0.6, 0.4), (1.0, 0.5), (0.8, 0.4)],
    plateaux_par_niveau=4,
    production_par_plateau=8,
    objectif_journalier=None
):
    configurations = []

    # Nombre de niveaux calculé dynamiquement selon la hauteur disponible
    niveaux = max(1, int(hauteur_dispo // hauteur_plateau))

    for L, l in tailles_plateaux:
        for orientation in ["longueur_face", "largeur_face"]:
            if orientation == "longueur_face":
                largeur_rack = L * 2
                profondeur_rack = l * 2
            else:
                largeur_rack = l * 2
                profondeur_rack = L * 2

            # Placement en grille (pavage au sol)
            nb_racks_largeur = int(largeur_dispo // largeur_rack)
            nb_racks_longueur = int(longueur_dispo // profondeur_rack)
            racks_max = nb_racks_largeur * nb_racks_longueur

            total_plateaux = racks_max * niveaux * plateaux_par_niveau
            production_theorique = total_plateaux * production_par_plateau

            configurations.append({
                "plateau_L": L,
                "plateau_l": l,
                "orientation": orientation,
                "surface_rack": round(largeur_rack * profondeur_rack, 3),
                "racks_max": racks_max,
                "niveaux": niveaux,
                "plateaux_par_niveau": plateaux_par_niveau,
                "total_plateaux": total_plateaux,
                "production": round(production_theorique, 2),
                "objectif_atteint": objectif_journalier is not None and production_theorique >= objectif_journalier
            })

    return sorted(configurations, key=lambda c: (-c["production"], c["surface_rack"]))
