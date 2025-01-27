# Elephant


## test plan - Navigation 
  ### retour home : 
    desciption : retourner à la page principale depuis chacune des pages
    resultat attendu : la page home est bien accessible depuis chacune des pages
    resultat obtenu : la page home est bien accessible depuis chacune des pages
    resultat obtenu V 1.0.9 : la page home est bien accessible depuis chacune des pages

  ### accès aux pages : 
    desciption : accéder à chacune des pages depuis le menu
    resultat attendu : chacune des pages est accéssible depuis home
    resultat obtenu : chacune des pages est accéssible depuis home
    resultat obtenu V 1.0.9 : chacune des pages est accéssible depuis home

  ### revenir à la page parente :
    description : revenir à la page précédente après avoir cliquer sur une autre page 
    resultat attendu : il est possible de revenir à la page précédente
    resultat obtenu : aucun bouton pour revenir à la page parente n'existe. Il est possible de revenir à la page parente avec la flèche "Précédent" du navigateur, ou bien avec une sourie / macro effectuant la même fonction.
    resultat obtenu V 1.0.9 : aucun bouton pour revenir à la page parente n'existe. Il est possible de revenir à la page parente avec la flèche "Précédent" du navigateur, ou bien avec une sourie / macro effectuant la même fonction.

## test plan - Fonctions

  ### Tester les champs du forms employer :
    desciption : tester les différents champs du form employer pour identifier lesquels laissent passer des valeurs inccorectes (correct ou incorrect)
    resultat attendu :
      - Name : Ne fonctionne pas si non rempli, ne laisse que des lettres être données
      - Email : Ne fonctionne pas si non rempli, vérifie si la structure est bonne
      - Adress : Ne fonctionne pas si non rempli
      - City : Demande à remplir si vide
      - Zip code : Demande à remplir si vide, seulement un nombre à 5 chiffres peut être donné
      - Hiring date : Demande à remplir si vide, une date impossible ne doit pas fonctionner
      - Job title : Demande à remplir si vide
    résultat obtenu :
      - Name : Ne fonctionne pas si non rempli, pas de message veuillez saisir un nom si nom manquant, laisse des chiffres et charactère spéciaux être rentrés
      - Email : Ne fonctionne pas si non rempli, pas de message veuillez saisir un email si email manquant, vérifie si la structure est bonne (même si non indiqué si non)
      - Adress : Ne fonctionne pas si non rempli, champs d’adresse dupliqué mais fonctionne si un seul des deux est rempli
      - City : Demande à remplir si vide
      - Zip code : Demande à remplir si vide, une lettre ne peut pas être rentrée sauf un seul e (mais renvoie une erreur à la création), permet de mettre plus de 5 chiffres ou des entiers négatifs
      - Hiring date : Demande à remplir si vide, jour et mois corrects mais l'année peut avoir plus de 4 chiffres
      - Job title : Demande à remplir si vide
    résultats obtenus V1.0.9 :
      - Name : Ne fonctionne pas si non rempli, pas de message veuillez saisir un nom si nom manquant, laisse des chiffres et charactère spéciaux être rentrés
      - Email : Ne fonctionne pas si non rempli, pas de message veuillez saisir un email si email manquant, vérifie si la structure est bonne (même si non indiqué si non)
      - Adress : Ne fonctionne pas si non rempli, champs d’adresse dupliqué mais fonctionne si un seul des deux est rempli
      - City : Demande à remplir si vide
      - Zip code : Demande à remplir si vide, une lettre ne peut pas être rentrée sauf un seul e (mais renvoie une erreur à la création), permet de mettre plus de 5 chiffres ou des entiers négatifs
      - Hiring date : Demande à remplir si vide, une date impossible ne fonctionne pas
      - Job title : Demande à remplir si vide

  ### créer un employer 
    desciption : créer un employer en renseignant tous les champs correctement 
    resultat attendu : créer un employer complet
    resultat obtenu : l'employé est créé
    resultat obtenu V 1.0.9 : l'employé est créé

  ### créer un employer incomplet :  
    desciption : créer un employer sans renseigner tous les champs
    resultat attendu : l'employer ne doit pas se créer 
    resultat obtenu : l'employer n'est pas créé
    resultat obtenu V 1.0.9 : l'employer n'est pas créé

  ### créer un employer incorrect :  
    desciption : créer un employer en renseignant mal des champs
    resultat attendu : l'employer ne doit pas se créer 
    resultat obtenu : l'employer est créé
    resultat obtenu V 1.0.9 : l'employer est créé

  ### créer une équipe correctement :  
    desciption : créer une équipe en renseignant le champ correctement
    resultat attendu : l'équipe doit se créer
    resultat obtenu : l'équipe est créée
    resultat obtenu V 1.0.9 : l'équipe est créée

  ### créer une équipe avec champ vide ou espaces :
    description : créer une équipe en ne renseignant pas le champ ou bien avec seulement des espaces
    resultat attendu : l'équipe ne se créé pas
    résultat obtenu : ne permet de pas créer une équipe avec un champ vide, renvoie une erreur lors de la création d'équipe avec uniquement des espaces renvoie une erreur 500 
    resultat obtenu V 1.0.9 : ne permet de pas créer une équipe avec un champ vide, renvoie une erreur lors de la création d'équipe avec uniquement des espaces renvoie une erreur 500 

  ### page modifier un employer :
    description : se rendre sur la page de modification d'un employer
    resultat attendu : il est possible de se rendre sur la page correctement
    resultat obtenu : il est possible de se rendre sur la page correctement
    resultat obtenu V 1.0.9 : il est possible de se rendre sur la page correctement

  ### Update basic info : 
    description : modification des champs name et email d'un employer
    resultat attendu : les champs name et email sont bien mis à jour
    resultat obtenu : les champs name et email sont bien mis à jour
    resultat obtenu V 1.0.9 : les champs name et email sont bien mis à jour

  ### Update adress :
    description : modification des champs de l'adresse d'un employer
    resultat attendu : les champs de l'adresse, ville et code postal sont bien mis à jour
    resultat obtenu : La 2ème ligne de l’adresse ne peut pas etre modifiée, ville et code postal sont bien mis à jour
    resultat obtenu V 1.0.9 : La 2ème ligne de l’adresse ne peut pas etre modifiée, ville et code postal sont bien mis à jour

  ### Update contract :
    description : modification des champs du contrat
    resultat attendu : les champs de "Hiring date" et Job title
    resultat obtenu : impossible d’update la hiring date, mais job title fonctionne
    resultat obtenu V 1.0.9 : impossible d’update la hiring date, mais job title fonctionne

  ### Promote as manager :
    description : modification d'un employer pour le promouvoir mamanger
    resultat attendu : l'employer est bien promu manager
    resultat obtenu : l'employer est bien promu manager
    resultat obtenu V 1.0.9 : l'employer est bien promu manager

  ### Demote as employee :
    description : modification d'un employer manager pour le retrograder employer
    resultat attendu : l'employer manager est bien retrogradé employer
    resultat obtenu : impossible de rétrograder un employer manger en employer (pas de fonction)
    resultat obtenu V 1.0.9 : impossible de rétrograder un employer manger en employer (pas de fonction)

  ### Add to team :
    description : ajout de l'employer à une équipe 
    resultat attendu : l'employer est bien ajouté à une équipe 
    resultat obtenu : l'employer est bien ajouté à une équipe 
    resultat obtenu V 1.0.9 : l'employer est bien ajouté à une équipe

  ### Delete employee :
    description : supression d'un employer de la BDD
    resultat attendu : l'employer est bien supprimé de la BDD
    resultat obtenu : Impossible de supprimer un employee, manque un bouton “Proceed” après avoir cliquer sur delete 
    resultat obtenu V 1.0.9 : l'employer est bien supprimé de la BDD

  ### View team members :
    description : accéder à la page view members depuis la page teams
    resultat attendu : les membres de l'équipe et leurs roles sont bien affichés
    resultat obtenu : les membres de l'équipe et leurs roles sont bien affichés
    resultat obtenu V 1.0.9 : les membres de l'équipe et leurs roles sont bien affichés

  ### Delete team :
    description : supression d'une équipe de la BDD 
    resultat attendu : l'équipe est bien supprimée de la BDD
    resultat obtenu : l'équipe est bien supprimée de la BDD
    resultat obtenu V 1.0.9 : l'équipe est bien supprimée de la BDD mais supprime également les employers présents dans l'équipe

  ### Delete employee from team :
    description : supression d'un employer dans une équipe 
    resultat attendu : l'employé est supprimé de l'équipe 
    resultat obtenu : Une fois un employé ajouté a une team il est impossible de le retirer de celle-ci
    resultat obtenu V 1.0.9 : l'employé est supprimé de l'équipe

  ### Delete DB
    description : supression totale de la BDD depuis la page rest_db
    resultat attendu : la base de donnée est bien vidée
    resultat obtenu : la base de donnée est bien vidée
    resultat obtenu V 1.0.9 :

