from flask import Flask, render_template, request, session, redirect, url_for
import json

app = Flask(__name__)

app.secret_key = 'ma_cle_secrete'

@app.route('/resultat', methods=['POST'])
def resultat():
    personnage = request.form['personnage']
    return render_template('resultat.html', personnage=personnage)

# Charger la base de données (arbre des questions)
def charger_base_de_donnees():
    try:
        with open("base_de_donnees.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Erreur de chargement du fichier JSON: {e}")
        return {}  # Retourne un dictionnaire vide en cas d'erreur

@app.route('/')
def index():
    # Charger la base de données
    base_de_donnees = charger_base_de_donnees()

    # Si l'arbre n'est pas dans la session, initialiser avec la question de départ
    if 'arbre' not in session:
        session['arbre'] = base_de_donnees
        return render_template('index.html', question=base_de_donnees["question"])

    # Si l'arbre est dans la session, vérifier si c'est un personnage ou une question
    arbre_courant = session['arbre']
    
    # Si l'arbre courant est une chaîne (un personnage), afficher le résultat
    if isinstance(arbre_courant, str):  # C'est un personnage
        return render_template('resultat.html', personnage=arbre_courant)

    # Si l'arbre courant est un dictionnaire (une question), afficher la question
    return render_template('index.html', question=arbre_courant['question'])



@app.route('/reponse', methods=['POST'])
def reponse():
    reponse_utilisateur = request.form['reponse']  # récupère la réponse de l'utilisateur

    # Si l'arbre est dans la session, avancer dans l'arbre
    if 'arbre' in session:
        arbre_courant = session['arbre']
        
        # Vérifier si l'arbre courant est un dictionnaire ou une chaîne
        if isinstance(arbre_courant, dict):
            # Mettre à jour l'arbre en fonction de la réponse (oui ou non)
            if reponse_utilisateur == "oui":
                session['arbre'] = arbre_courant.get('oui')
            elif reponse_utilisateur == "non":
                session['arbre'] = arbre_courant.get('non')

            # Vérifier si on a atteint un personnage
            if isinstance(session['arbre'], str):  # Si c'est un personnage
                return render_template('resultat.html', personnage=session['arbre'])
            else:  # Sinon, on continue avec la prochaine question
                return render_template('index.html', question=session['arbre']["question"])

    return "Erreur, l'arbre n'est pas trouvé dans la session", 500

# Nouvelle route pour recommencer
@app.route('/recommencer')
def recommencer():
    # Réinitialiser l'arbre des questions dans la session
    session.pop('arbre', None)  # Supprimer l'arbre de la session pour recommencer
    return redirect(url_for('index'))  # Rediriger vers la première question

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
