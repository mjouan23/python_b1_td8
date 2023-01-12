# Exercice 1
# 1.Déclarez le tuple contenant la classication Dewey
dewey = ('Généraux', 'Philosophie', 'Religieux', 'Sciences sociales', 'Langue', 'Science pure', 'Technologie', 'Arts et loisirs', 'Littérature', 'Histoire et géographie')
# # 2.Tant que l'utilisateur n'aura pas saisi "stop", lui demander la référence d'un livre sur 3 chiffres. Exemple : 312
# # 3.A partir de cette référence en déduire sa classe Dewey et l'afficher à l'aide du tuple
ref = ""
while ref != "stop" :
    ref = input("Référence livre : ")
# 4.Afin d’optimiser votre code, vous devrez contrôler si la saisie de l’utilisateur est bien composée de 3 chiffres.
# Si ce n’est pas le cas, affichez le message suivant : « Votre référence est invalide ». Puis réitérez la demande.
    if(len(ref) > 3 or not(ref.isnumeric())) :
        print("Votre référence est invalide.")
    else:
        indice = int(ref[0])
        print(f"La classe Dewey de votre livre est \"{dewey[indice]}\"")