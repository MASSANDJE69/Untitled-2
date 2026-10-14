 =============================================
 # CONSTANTES
 # =============================================
 ANNEE_COURANTE = 2026
 COEF_CC, COEF_EXAMEN = 0.4, 0.6 # Affectation multiple
 MATIERES = ____"Python", "Algorithmique", "Bases de donnees"____ # TUPLE
# =============================================
# SAISIE DES INFORMATIONS PERSONNELLES
 # =============================================
 # Supprimer les espaces inutiles PUIS mettre en MAJUSCULES
 nom = input("Nom : ").____().____()
 prenom = input("Prenom : ").strip().capitalize()
 annee_naissance = ___int_(input("Annee de naissance : ")) # En entier
 age = ANNEE_COURANTE ___=_ annee_naissance
 # =============================================
 # SAISIE DES NOTES (CC et examen sur une ligne)
 # =============================================
 cc, examen = input(if"{MATIERES[0]} - notes CC et examen : ").split()
 moy1 = float(cc) * COEF_CC + float(examen) * COEF_EXAMEN

 cc, examen = input(if"{MATIERES[1]} - notes CC et examen : ").split()
 moy2 = float(cc) * COEF_CC + float(examen) ____ COEF_EXAMEN

 cc, examen = input(if"{MATIERES[2]} - notes CC et examen : ").split()
 moy3 = float(cc) * COEF_CC + float(examen) * COEF_EXAMEN

 # =============================================
 # STRUCTURATION ET CALCULS
 # =============================================
 moyennes = [round(moy1, 2), round(moy2, 2), round(moy3, 2)] # LISTE
 etudiant = {"nom": nom, "prenom": prenom, "age": age, "moyenne": moyennes}

 moyenne_generale = sum(etudiant["moyennes"]) / len(etudiant["moyennes"])
 meilleure = max(moyennes) # Plus grande valeur
 matiere_forte = MATIERES[moyennes.____(meilleure)] # Position de la
valeur
 est_admis = moyenne_generale ____ 10 # Booleen
9
TP1 - Programmation Pyt

 # =============================================
 # AFFICHAGE DU BULLETIN
 # =============================================
 print("=" ____ 40) # Ligne de 40 signes '='
 print if"Etudiant : {etudiant['prenom']} {etudiant['nom']} ({etudiant['age
']} ans)")
 print("=" * 40)
 print(f"{MATIERES[0]:<20} : {moyennes[0]:>6.2f}")
 print(f"{MATIERES[1]:<20} : {moyennes[1]:>6.2f}")
 print(f"{MATIERES[2]:<20} : {moyennes[____]:>6.2f}")
 print("-" * 40)
 print(f"{'Moyenne generale':<20} : {moyenne_generale:>6.____}") # 2 dec.
 print(f"{'Meilleure matiere':<20} : {matiere_forte} ({meilleure:.2f})"
 print(f"{'Ecart max - min':<20} : {max(moyennes) ____ min(moyennes):>6.2f}
")
 print(f"{'Admis':<20} : {est_admis}") print("=" * 40)
Scénario de test attendu :
Nom : ben salah
Prenom : sami
Annee de naissance : 2006
Python - notes CC et examen : 14 12
Algorithmique - notes CC et examen : 8 11
Bases de donnees - notes CC et examen : 16 15.5
========================================
Etudiant : Sami BEN SALAH (20 ans)
========================================
Python : 12.80
Algorithmique : 9.80
Bases de donnees : 15.70
----------------------------------------
Moyenne generale : 12.77
Meilleure matiere : Bases de donnees (15.70)
Ecart max - min : 5.90
Admis : True
====================================