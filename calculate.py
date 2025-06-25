
# calculate.py

from config import GRAINES

def calculer_production(params):
    hauteur = params["hauteur"]
    longueur = params["longueur"]
    largeur = params["largeur"]
    plateau_L = params["plateau_L"]
    plateau_l = params["plateau_l"]
    hauteur_niveau = params["hauteur_niveau"]
    graine = params["graine"]
    objectif = params["objectif"]

    rendement_cycle = GRAINES[graine]["rendement_cycle_kg"]
    cycle = 7  # jours
    surface_dispo = longueur * largeur
    surface_plateau = plateau_L * plateau_l

    niveaux_par_rack = int(hauteur / hauteur_niveau)
    surface_par_rack = 0.8  # m² approximatif occupé par un rack
    plateaux_par_niveau = int(surface_par_rack / surface_plateau)
    plateaux_par_rack = plateaux_par_niveau * niveaux_par_rack

    production_par_plateau = rendement_cycle / cycle
    plateaux_requis = int(objectif / production_par_plateau) + 1
    racks_requis = int(plateaux_requis / plateaux_par_rack) + 1
    plateaux_total = racks_requis * plateaux_par_rack
    surface_totale = racks_requis * surface_par_rack
    prod_estimee = plateaux_total * production_par_plateau

    return {
        "plateaux_requis": plateaux_requis,
        "racks": racks_requis,
        "niveaux": niveaux_par_rack,
        "plateaux_par_niveau": plateaux_par_niveau,
        "plateaux_par_rack": plateaux_par_rack,
        "plateaux_total": plateaux_total,
        "production_jour": prod_estimee,
        "surface_occupée": surface_totale,
        "objectif_atteint": prod_estimee >= objectif
    }
