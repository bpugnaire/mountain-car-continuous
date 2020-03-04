# mountain-car-continuous

Projet d'apprentissage par renforcement réalisé lors de mon master Intelligence Artificielle et Apprentissage Automatique (Aix-Marseille Université) en paralèlle de mes études à l'École Centrale Marseille.

## Objectifs

- Concevoir des agents SARSA et Q-learning afin de résoudre le problème 'MountainCarContinuous" du module gym d'openAI (https://gym.openai.com/envs/MountainCarContinuous-v0/).
- Comparer les performances des agents entre eux et pour un nombre d'états et/ou d'actions variable

## Le Problème

Il faut parvenir à faire monter la voiture en haut de la colline en utilisant le moins de carburant possible : le reward obtenu en arrivant en haut est égal à 100, chaque dépense d'essence engendre un reward négatif proportionnel à la dépense.

## Performances

Les deux agents parviennent régulièrement à résoudre le problème avec plus ou moins de régularité.

L'agent SARSA obtient un reward moyen de 72.
L'agent Q-learning obtient un reward moyen de 91.

Empiriquement, les meilleurs rewards atteints étaient toujours inférieurs à 97.
