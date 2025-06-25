# utils.py

def demander_float(message):
    try:
        return float(input(message))
    except:
        return demander_float("🔁 Entrée invalide. Réessaye : ")

def demander_choix(message, options):
    val = input(message).lower()
    return val if val in options else demander_choix(f"🔁 Choix invalide. Choisis parmi {options} : ", options)
