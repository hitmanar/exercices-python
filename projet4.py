print("--- RAPPORT D'INVENTAIRE ACTUEL ---")
products = [
    ('p01', 'T-shirt', 19.99),
    ('p02', 'Jean', 39.99),
    ('p03', 'Chaussures', 59.99)
]


stock_levels = {
    'p01': 50,
    'p02': 30,
    'p03': 20
}

# 3. Choisir le produit à vendre
product_to_sell = 'p01'

# 4. Parcourir la liste pour trouver le produit correspondant
for pid, name, price in products:
    if pid == product_to_sell:
        # Vérifier s'il y a du stock
        if stock_levels[pid] > 0:
            # Diminuer le stock de 1
            stock_levels[pid] -= 1
            # Afficher le message de confirmation
            print(f"Vendu : {name} pour {price} €. Stock restant : {stock_levels[pid]}.")
        else:
            print(f"Le produit {name} est en rupture de stock.")
        break
