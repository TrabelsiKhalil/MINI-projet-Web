# Mini Project Web
> Gestion de collection de jeux vidéo

### Contenu

- [Mini Project Web](#mini-project-web)
    - [Contenu](#contenu)
  - [Description](#description)
  - [## les composantes](#-les-composantes)
    - [composant app](#composant-app)
      - [description](#description-1)
    - [fonctionalités](#fonctionalités)
    - [composant card deck](#composant-card-deck)
      - [description](#description-2)
    - [fonctionalités](#fonctionalités-1)
    - [composant card](#composant-card)
      - [description](#description-3)
    - [fonctionalités](#fonctionalités-2)
    - [composant add game (dialog)](#composant-add-game-dialog)
      - [description](#description-4)
    - [fonctionalités](#fonctionalités-3)
    - [composant info page](#composant-info-page)
      - [description](#description-5)
    - [fonctionalités](#fonctionalités-4)
    - [composant result page](#composant-result-page)
      - [description](#description-6)
    - [fonctionalités](#fonctionalités-5)
    - [composant header](#composant-header)
      - [description](#description-7)
    - [fonctionalités](#fonctionalités-6)
    - [composant footer](#composant-footer)
      - [description](#description-8)
    - [fonctionalités](#fonctionalités-7)
  - [- N/A](#--na)

---

## Description
Angular est un framework d'application Web open source basé sur TypeScript dirigé par l'équipe Angular de Google et par une communauté d'individus et d'entreprises. Angular est une réécriture complète de la même équipe qui a construit AngularJS 


[Retour au sommet](#mini-project-web)

## les composantes
---
### composant app
 ```typescript
 selector: 'app-root' 
 ```

#### description
c'est le composant principlae  et le parent de tout les composants de notre application  
il joue le role du controlleur

### fonctionalités
- il gère tout les requêtes vers le backend  

---

### composant card deck
 ```typescript
 selector: 'app-card-deck' 
 ```

#### description
c'est le composant qui regroupe les cartes

### fonctionalités
- il gere les cartes  
- il facilite la communications entre les carte et le controlleur(composant app)
  
---

### composant card 
 ```typescript
 selector: 'app-card' 
 ```

#### description
c'est le composant qui represente l'information du jeux 

### fonctionalités
- déléguer les interactions de l'utilisateur au composant parent (composant card deck)


---

### composant add game (dialog) 
 ```typescript
 selector: 'app-add-game' 
 ```

#### description
c'est le composant qui gere le dialog (popup) 
- il s'agit de deux type de dialog:
    - dialog Ajouter
    - dialog modifier

### fonctionalités
- déléguer les informations obtenu  au composant parent (composant qui lui a appellé)

---

### composant info page 
 ```typescript
 selector: 'app-info-page' 
 ```

#### description
c'est le composant qui represent les informations sur un jeu particulié 

### fonctionalités
- N/A

---

### composant result page 
 ```typescript
 selector: 'app-result-page' 
 ```

#### description
c'est le composant qui represent les informations sur un recherche particulié 

### fonctionalités
- N/A

---


### composant header
 ```typescript
 selector: 'app-header' 
 ```

#### description
c'est le composant qui represent la barre du navigation de notre application 

### fonctionalités
- permet l'ajout d'un jeu a travers le button "ADD"
- permet la recherche d'un jeu a travers le input "search"

---

### composant footer
 ```typescript
 selector: 'app-footer' 
 ```

#### description
c'est le composant qui represent la bas de page

### fonctionalités
- N/A
---
  
  









