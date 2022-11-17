
# Alignment free - TP 1

L'objectif du TP est de comparer 5 especes de bactéries entre elles.
Vous trouverez les données en suivant [ce lien](https://we.tl/t-WeWvheBBGX)

## Composer le TP

Vous devez forker ce projet puis compléter ses fonctions.
Le rendu sera le dépot git dans lequel vous aurrez forké.

Le but est d'obtenir toutes les distances paire à paire des différentes bactéries.
Vous pouvez modifier l'affichage final pour obtenir une matrice d'adjacence si vous les souhaitez.

En observant les distances obtenues, que pouvez-vous dire des espèces présentes dans cet échantillon ?

## TME 5 - PHYG

Auteurs: Damien Legros et Cédric Cornède

Vous retrouverez sur le git le code dans les 3 fichiers .py, l'output dans le .ipynb et les matrices dans les 3 fichiers .png.

- **Matrice d'adjacence avec score jaccard:** On observe que ASM584, ASM886 et ASM2216 sont très similaires (+93%). ASM694 et ASM824478 sont un peu moins similaires (~40%). Les autres comparaisons montrent des taux de similarités très faibles (~1%).

- **Matrice d'adjacence avec score similarité avec génome A:** On observe les memes corrélations avec des pourcentages plus élevés. On observe que ASM584, ASM886 et ASM2216 sont très similaires (+95%). ASM694 et ASM824478 sont un peu moins similaires (~67%). Les autres comparaisons montrent des taux de similarités très faibles (~3%).

- **Matrice d'adjacence avec score similarité avec génome A:** On observe a peu près les mêmes résultats. On observe que ASM584, ASM886 et ASM2216 sont très similaires (+95%). ASM694 et ASM824478 sont un peu moins similaires (~55%). Les autres comparaisons montrent des taux de similarités très faibles (~3%).

Ainsi en conclusion on a donc une forte similarité entre ASM584, ASM886 et ASM221 et une similarité plus faible entre ASM694 et ASM824478.
