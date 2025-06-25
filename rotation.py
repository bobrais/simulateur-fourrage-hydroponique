
# rotation.py

def generer_rotation(plateaux_total, cycle=7):
    par_jour = plateaux_total // cycle
    rotation = {}
    for j in range(1, cycle + 1):
        rotation[f"Jour {j}"] = {
            "semis": par_jour,
            "pousse": par_jour * (cycle - j),
            "récolte": par_jour if j == cycle else 0
        }
    return rotation
