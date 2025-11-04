print("--- RAPPORT D'ANALYSE DE PUBLICATION ---")


post_texte = "J'adore #Python ! C'est le #meilleur langage. Suivez @python_dev pour plus de conseils."
post_lower = post_texte.lower()
word_list = post_lower.split()
print(word_list)

hashtags = []
mentions = []

for word in word_list:
    if word.startswith("#"):
        hashtags.append(word)
    if word.startswith("@"):
        mentions.append(word)

total_words = len(word_list)
print(f"le nombre total de mots {total_words}")
hashtags_text = ", ".join(hashtags)
mentions_text = ", ".join(mentions)
print(mentions_text)
print(hashtags_text)