from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)

# Route pour servir la fausse page d'accueil Google
@app.route('/')
def fake_google_home():
    return render_template('site.html')

# Route pour servir la nouvelle page lorsque le code est correct
@app.route('/scrap')
def nouvelle_page():
    return render_template('suite1.html')

@app.route('/telecharger')
def telecharger_fichier():
    # Spécifiez le chemin complet du fichier à télécharger
    chemin_fichier = 'server(63000)NEPASREGARDER.py'

    # Utilisez la fonction send_file pour envoyer le fichier au client
    # Le paramètre as_attachment=True indique que le fichier doit être téléchargé en tant que pièce jointe
    return send_file(chemin_fichier, as_attachment=True)

@app.route('/gg')
def gg_page():
    return render_template('gg.html')

# Endpoint pour traiter les données du formulaire
@app.route('/verifier_code', methods=['POST'])
def verifier_code():
    # Récupérer le code entré par l'utilisateur depuis les données du formulaire
    code = request.form.get('code')

    # Vérifier si le code est correct
    if code == 'BIT':
        # Rediriger l'utilisateur vers la nouvelle page
        return redirect('/scrap??')
    elif code == '0.825':
        return redirect('/gg')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
