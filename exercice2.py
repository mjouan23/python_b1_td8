import json
dewey = ('Généraux', 'Philosophie', 'Religieux', 'Sciences sociales', 'Langue', 'Science pure', 'Technologie', 'Arts et loisirs', 'Littérature', 'Histoire et géographie')

# Exercice 2
# 1.Créez une liste de dictionnaires « books », permettant de recenser toutes les informations du tableau.
# Toutes les données devront être saisies depuis le terminal sauf le rang qui devra se générer automatiquement.
# books = []
# for i in range(1,11):
#     title = input("Titre : ")
#     author = input("Auteur : ")
#     copies = input("Nombre d'exemplaires : ")
#     gender = input("Genre : ")
#     book = {
#         "rang" : i,
#         "title" : title,
#         "author" : author,
#         "copies" : int(copies),
#         "gender" : gender
#     }
#     books.append(book)

# 2.Afin d’éviter à l’utilisateur cette saisie un peu rébarbative, vous devrez, à l’aide de la librairie python json,
# convertir la liste de dictionnaire en json et enregistrer ce JSON dans un fichier « top_books_2021.json ».
# with open("top_books_2021.json", "w") as data:
#     json.dump(books, data)

# 3.Reprenez votre json enregistrez dans « top_books_2021.json », ajoutez la clé « code_dewey »
# dans laquelle vous devrez insérer la valeur au format suivant : « code en fonction du genre-3 premières lettres
# du nom de l’auteur en majuscule ». Ce traitement devra être fait de manière automatique.
f = open('top_books_2021.json')
books = json.load(f)
for book in books:
    code_author = book["author"].split()
    code_dewey = str(dewey.index(book["gender"]))+"00-"+code_author[-1][0:3].upper() 
    book["code_dewey"] = code_dewey
    # Possibilité de fusionner les 3 dernières lignes mais pas forcément pertinant en terme de lisibilité
    # book["code_dewey"] = str(dewey.index(book["gender"]))+"00-"+book["author"].split()[-1][0:3].upper()

# 4.Une fois le retraitement de la question 3. Effectué, pensez à mettre à jour votre fichier « top_books_2021.json »
# avec cette nouvelle donnée.
with open("top_books_2021.json", "w") as data:
    json.dump(books, data)

# 5.A partir de la liste "books", renvoyer le classement des genres les plus vendus avec le nombre total d'exemplaires vendus.
# Vous devrez trier ces paires du plus grand nombres d'exemplaires au plus petit.
top_gender = {}
for book in books:
    if(book["gender"] in top_gender.keys()):
        top_gender[book["gender"]] += book["copies"]
    else:
        top_gender[book["gender"]] = book["copies"]

sorted_gender = dict(sorted(top_gender.items(), key=lambda item:item[1], reverse=True))
print(sorted_gender)