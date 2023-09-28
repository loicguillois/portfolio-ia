# Détection du type d'activité

À partir de la trace GPS, être capable de détecter le type d'activité : vélo ou course à pied ? Ce modèle s'appuie sur un réseau de neuronne et en particulier un réseau LSTM particulièrement adapté aux séries temporelles.

# Prédiction de trajectoires

À partir de la trace GPS, être capable de prédire la suite du parcours. Il s'agit donc d'une IA dite générative. Ce modèle met également en oeuvre un réseau LSTM. Malheuresement les trajectoires sont trop erratiques. Il doit être possible d'améliorer l'efficacité de ce modèle en intégrant la carte routière pour le vélo sur route et IGN pour la course à pied sur chemin. Pour les trajectoires "à vol d'avion", bien plus linéaire, ce modèle serait suffisant.