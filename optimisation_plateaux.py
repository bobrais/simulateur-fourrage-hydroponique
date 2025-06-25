# optimisation_plateaux.py

def generer_configurations_standard(
    longueur_dispo,
    largeur_dispo,
    tailles_plateaux=[(0.7, 0.3), (0.6, 0.4), (1.0, 0.5), (0.8, 0.4)],
    niveaux=7,
    plateaux_par_niveau=4,
    production_par_plateau=8,
    objectif_journalier=None
):
    configurations = []

    for L, l in tailles_plateaux:
        for orientation in ["longueur_face", "largeur_face"]:
            if orientation == "longueur_face":
                largeur_rack = L * 2
                profondeur_rack = l * 2
            else:
                largeur_rack = l * 2
                profondeur_rack = L * 2

            surface_rack = largeur_rack * profondeur_rack
            surface_totale = longueur_dispo * largeur_dispo
            max_racks = int(surface_totale // surface_rack)
            total_plateaux = max_racks * niveaux * plateaux_par_niveau
            production_theorique = total_plateaux * production_par_plateau

            configurations.append({
                "plateau_L": L,
                "plateau_l": l,
                "orientation": orientation,
                "surface_rack": round(surface_rack, 3),
                "racks_max": max_racks,
                "total_plateaux": total_plateaux,
                "production": production_theorique,
                "objectif_atteint": objectif_journalier is not None and production_theorique >= objectif_journalier
            })

    return sorted(configurations, key=lambda c: (-c["production"], c["surface_rack"]))
