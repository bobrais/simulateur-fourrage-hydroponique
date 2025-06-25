# optimisation_plateaux.py

configurations = generer_configurations_standard(
    longueur_dispo=params["longueur"],
    largeur_dispo=params["largeur"],
    objectif_journalier=params["objectif"],
    production_par_plateau=result["rendement_plateau"],
    niveaux=result["niveaux"],
    plateaux_par_niveau=result["plateaux_par_niveau"]
)
:
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
