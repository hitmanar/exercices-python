
tasks = []

# Ajout de tâches
tasks.append("Faire les courses")
tasks.append("Étudier le Python")
tasks.append("Appeler un ami")


print("--- VOS TÂCHES ACTUELLES ---")

if not tasks:
    print("Vous n'avez aucune tâche !")
else:
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

if tasks:  # Vérifie qu'il y a au moins une tâche
    completed_task = tasks.pop(0)
    print(f'\nTâche terminée : "{completed_task}"')

print("\n--- LISTE MISE À JOUR ---")

if not tasks:
    print("Toutes les tâches ont été terminées 🎉")
else:
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
