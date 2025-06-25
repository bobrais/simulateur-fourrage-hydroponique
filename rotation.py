# rotation.py

def generer_rotation(plateaux_disponibles, cycle=7):
    rotation = {}
    stock_restant = plateaux_disponibles
    par_jour = plateaux_disponibles // cycle
    historique_semis = []

    rotation["J0"] = {
        "stock_initial": plateaux_disponibles,
        "semis": 0,
        "pousse": 0,
        "récolte": 0,
        "stock_restant": plateaux_disponibles
    }

    for j in range(1, cycle + 1):
        jour = f"Jour {j}"
        semis = min(par_jour, stock_restant)
        stock_restant -= semis
        historique_semis.append(semis)

        pousse = sum(historique_semis[-(cycle - 1):])  # pousse = tout sauf les semis du jour même
        recolte = historique_semis[j - cycle] if j >= cycle else 0

        rotation[jour] = {
            "semis": semis,
            "pousse": pousse,
            "récolte": recolte,
            "stock_restant": stock_restant
        }

    return rotation
