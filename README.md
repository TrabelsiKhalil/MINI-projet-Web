# Projet : Gestion de collection de jeux vidéo
## Aller à la section
* [Specification des besoins](#Specification-des-besoins)  
  * [Les besoins fonctionnels](#A---Les-besoins-fonctionnels)
  * [Les besoins non fonctionnels](#B---Les-besoins-non-fonctionnels)
* [Modélisation des besoins fonctionnels](#Modélisation-des-besoins-fonctionnels)
  * [diagramme de cas d’utilisation](#fig1)
* [Modélisation dynamique](#Modélisation-dynamique)
  * [Diagram de séquence ](#fig2)

## Specification des besoins :

Dans cette section, nous procedons a une etape de specification des besoins fonctionnels de notre systeme.  
Ces besoins seront modelises a travers une etude detaillee de ses fonctionnalites.   
En fait, les besoins fonctionnels servent a mieux comprendre le role de systeme en question ainsi que ses fonctionnalites essentielles.   
En effet, **notre systeme devra repondre aux besoins fonctionnels suivants :**

### A - LES BESOINS FONCTIONNELS:
L’application offre a les clients les fonctionnalites suivantes :<br> 
* Ajouter un jeu<br>
* Consulter un jeu<br>
* Modifier un jeu<br>
* Supprimer un jeu<br>

### B - Les besoins non fonctionnels :
Il s'agit des besoins qui caractérisent le système. Ce sont des besoins en matière de performance, de type de matériel ou le type de conception. 
L'application devra être capable de :

- **La fiabilité :**  
 Maturité  
 Tolérance aux fautes  
 Possibilité de récupération  
 
- **La facilité d'utilisation (utilisabilité):**  
 Facilité de compréhension.  
 Facilité d’apprentissage.  
 Facilité d’exploitation/d’utilisation.  
 Attractivité.  
 
- **Le rendement et l'efficacité:**  
 Comportement vis-à-vis du temps.  
 Comportement vis-à-vis des ressources.  
- **La maintenabilité:**  
 Facilité d’analyse.  
Facilité de modification.  
Stabilité.  
Testabilité.  

- **La portabilité:**  
Facilité d’adaptation.  
Facilité à l’installation.  
Interchangeabilité.  

## Modélisation des besoins fonctionnels
Après la présentation des besoins fonctionnels, nous passons a la modélisation de ces
besoins par la définition des cas d’utilisation.
### Identification des cas d’utilisation
Dans cette section, nous présentons le diagramme de cas d’utilisation  (cf. Figure [1](#fig1))
qui permet d’illustrer les fonctionnalites système  vis-à-vis aux acteurs présentés.


<img id="fig1" src="https://github.com/Rzgi/GameHub/blob/main/spec/Diagramme%20de%20Cas%20d'Utilisation.png"
     alt="diagramme de cas d’utilisation"
     style="float: left; margin-right: 10px;" />
     
<p align="center">
Figure 1 - diagramme de cas d’utilisation 
</p>
<br></br>

Les fonctionnalités du système sont représentées par le diagramme de cas d’utilisation illustrée dans la figure [1](#fig1).  
Ce diagramme met en valeur la répartition des fonctionnalités entre les différents acteurs.  
Dans ce diagramme, il y a un seul acteur :  
&nbsp;&nbsp;&nbsp;&nbsp;**administrateur**



L’administrateur est cens ́e de réaliser les tâches suivantes :

* Ajouter un jeu aux collections<br>
* Consulter un jeu<br>
* Modifier un jeu<br>
* Supprimer un jeu<br>  


## Modélisation dynamique
### Diagrammes de séquences
Dans cette section, nous allons présenter les diagrammes de séquence les plus importants dans notre système. Le diagramme de séquence représente une interaction entre
plusieurs éléments qui interagissent par l’envoi de messages. Il permet de décrire le dynamisme d’un système et de faire le lien entre le diagramme de cas d’utilisation et le diagramme de classe.

**La figure [2](#fig2) représente le diagramme de séquence des cas d'utilisation :**  
* ajouter
* consulter
* modifier
* supprimer


 
 <img id="fig2" src="https://github.com/Rzgi/GameHub/blob/main/spec/Diagram%20de%20s%C3%A9quence%20.png"
     alt="diagramme de séquence"
     style="float: left; margin-right: 10px;" />
     
<p align="center" >
Figure 2 - diagramme de séquence
</p>
<br></br>

