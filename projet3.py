print("--- RAPPORT DE NETTOYAGE DES CONTACTS ---")


contact_numbers = ["0612345678", "0787654321", "0612345678","0654321987","0787654321"]
contact_length = len(contact_numbers)

print(f"la liste originalest: {contact_numbers}")
print(contact_length)

unique_contacts_set = set(contact_numbers)
print(unique_contacts_set)

unique_contacts_list = list(unique_contacts_set)
#unique_contacts_sorted = sorted(unique_contacts_list)
#print(unique_contacts_sorted)

unique_contacts_list.sort()
print(unique_contacts_list)

contanct_double = len(contact_numbers) - len(unique_contacts_set)
print(f"le nombre de doublons est {contanct_double}")

print(f"la liste finale est: {unique_contacts_list}")
print(f"le nombre de contact unique est de: {len(unique_contacts_set)} ")