# Elephant


## test plan - Navigation 
  ### retour home : 
    desciption : retourner à la page principale depuis chacune des pages
    resultat attendu : la page home est bien accessible depuis chacune des pages
    resultat obtenu : la page home est bien accessible depuis chacune des pages

  ### accès aux pages : 
    desciption : accéder à chacune des pages depuis le menu
    resultat attendu : chacune des pages est accéssible depuis home
    resultat obtenu : chacune des pages est accéssible depuis home

## test plan - Fonctions

  ### Tester les champs du forms employer :
    desciption : tester les différents champs du form employer pour identifier lesquels laissent passer des valeurs inccorectes (correct ou incorrect)

      - Name : Ne fonctionne pas si non rempli, pas de message veuillez saisir un nom si nom manquant, laisse des chiffres être rentrer
      - Email : Ne fonctionne pas si non rempli, pas de message veuillez saisir un email si email manquant, vérifie si la structure est bonne (même si non indiqué si non)
      - Adress : Ne fonctionne pas si non rempli, champs d’adresse dupliqué mais fonctionne si 
      - City : Demande à remplir si vide
      - Zip code : Demande à remplir si vide, une lettre ne peut pas être rentrée sauf un seul e (mais renvoie une erreur à la création), permet de mettre plus de 5 chiffres
      - Hiring date : Demande à remplir si vide, jour et mois corrects mais l'année peut avoir plus de 4 chiffres
      - Job title : Demande à remplir si vide

  ### créer un employer 
    desciption : créer un employer en renseignant tous les champs correctement 
    resultat attendu : créer un employer complet
    resultat obtenu : l'employé est créé

  ### créer un employer incomplet :  
    desciption : créer un employer sans renseigner tous les champs
    resultat attendu : l'employer ne doit pas se créer 
    resultat obtenu : l'employer n'est pas créé

  ### créer un employer incorrect :  
    desciption : créer un employer en renseignant mal des champs
    resultat attendu : l'employer ne doit pas se créer 
    resultat obtenu : l'employer est créé


  ### créer une équipe :  
    desciption : créer une équipe en renseignant tous les champs correctement
    resultat attendu : l'équipe doit se créer
    resultat obtenu : l'équipe est créée

  ### page modifier un employer :
    description : se rendre sur la page de modification d'un employer
    resultat attendu : il est possible de se rendre sur la page correctement
    resultat obtenu : il est possible de se rendre sur la page correctement

  ### Update basic info : 
    description : modification des champs name et email d'un employer
    resultat attendu : les champs name et email sont bien mis à jour
    resultat obtenu : les champs name et email sont bien mis à jour

  ### Update adress :
    description : modification des champs de l'adresse d'un employer
    resultat attendu : les champs de l'adresse, ville et code postal sont bien mis à jour
    resultat obtenu : La 2ème ligne de l’adresse ne peut pas etre modifiée

  ### Update contract :
    description : modification des champs du contrat
    resultat attendu : les champs de "Hiring date" et Job title
    resultat obtenu : impossible d’update la hiring date

  ### Promote as manager :
    description : modification d'un employer pour le promouvoir mamanger
    resultat attendu : l'employer est bien promu manager
    resultat obtenu : l'employer est bien promu manager

  ### Demote as employee :
    description : modification d'un employer manager pour le retrograder employer
    resultat attendu : l'employer manager est bien retrogradé employer
    resultat obtenu : l'employer manager est bien promu manager

  ### Add to team :
    description : ajout de l'employer à une équipe 
    resultat attendu : l'employer est bien ajouté à une équipe 
    resultat obtenu : l'employer est bien ajouté à une équipe 

  ### Delete employee :
    description : supression d'un employer de la BDD
    resultat attendu : l'employer est bien supprimé de la BDD
    resultat obtenu : Impossible de supprimer un employee, anque un bouton “Proceed” après avoir cliquer sur delete 

  ### View team members :
    description : accéder à la page view members depuis la page teams
    resultat attendu : les membres de l'équipe et leurs roles sont bien affichés
    resultat obtenu : les membres de l'équipe et leurs roles sont bien affichés

  ### Delete team :
    description : supression d'une équipe de la BDD 
    resultat attendu : l'équipe est bien supprimée de la BDD
    resultat obtenu : l'équipe est bien supprimée de la BDD

  ### Delete employee from team :
    description : supression d'un employer dans une équipe 
    resultat attendu : l'employé est supprimé de l'équipe 
    resultat obtenu : Une fois un employé ajouté a une team il est impossible de le retirer de celle-ci

  ### Delete DB
    description : supression totale de la BDD depuis la page rest_db
    resultat attendu : la base de donnée est bien vidée
    resultat obtenu : la base de donnée est bien vidée

    