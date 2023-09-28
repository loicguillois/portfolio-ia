# Portfolio IA et Machine Learning

Bienvenue sur mon dépôt GitHub où je présente une collection de cas d'usages et de démonstrateurs autour de l'Intelligence Artificielle (IA) et du Machine Learning. Ce portfolio vise à illustrer mon éventail de compétences à travers des exemples concrets basés sur des données ouvertes.

## Caractéristiques

### Prédiction

L'objectif de ce projet est de prédire les émissions de CO2 d'une automobile en s'appuyant sur sa fiche technique (poids, puissance, consommation...). La méthode d'entraînement retenue est XGBoost, qui fonctionne particulièrement bien pour ce type de prédiction d'une variable numérique (continue).

## Textes

### Moteur de recommandation

Ce projet montre comment on peut implémenter un moteur de recommandation en s'appuyant sur la similarité de contenu textuel. Dans cet exemple, des données descriptives de musées sont vertorisées à l'aide du modèle camemBERT, ce qui permet d'obtenir une liste de musée similaire à un musée donné.

## Images

### Colorisation

Ce projet présente un système de colorisation d'images utilisant une architecture vanilla (auto-encodeur) avec le framework Keras. Entrainé sur un sous-ensemble d'ImageNet, le modèle vise à revitaliser des images en noir et blanc en générant des couleurs naturelles. Des techniques de post-traitement ont été intégrées pour affiner la colorimétrie, offrant ainsi des résultats visuellement plus intéressant.

## Séries temporelles

### Traces GPS: Détection du type d'activité

À partir de la trace GPS, être capable de détecter le type d'activité : vélo ou course à pied ? Ce modèle s'appuie sur un réseau de neuronne et en particulier un réseau LSTM particulièrement adapté aux séries temporelles.

### Traces GPS: Prédiction de trajectoires

À partir de la trace GPS, être capable de prédire la suite du parcours. Il s'agit donc d'une IA dite générative. Ce modèle met également en oeuvre un réseau LSTM. Malheuresement les trajectoires sont trop erratiques. Il doit être possible d'améliorer l'efficacité de ce modèle en intégrant la carte routière pour le vélo sur route et IGN pour la course à pied sur chemin. Pour les trajectoires "à vol d'avion", bien plus linéaire, ce modèle serait suffisant.