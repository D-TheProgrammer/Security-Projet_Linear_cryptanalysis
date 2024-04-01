# Security-Projet_Linear_cryptanalysis
[French] Projet de cryptanalyse   
[English]  Linear cryptanalysis (First it will be the French README then the English README After)     

#### SOMMAIRE / SUMMARY
- [Présentation en francais / Presentation in French](#presentation-en-francais)
- [Présentation en anglais / Presentation in English](#english-presentation)
- [Tutoriel dans les deux langues / Tutorial in both languages](#tutoriel--tutorial)

## [PRESENTATION EN FRANCAIS]
Implémentation d’une attaque par cryptanalyse linéaire sur un algorithme de chiffrement ToyCipher en utilisant des approximations linéaires de la boîte de substitution pour réduire l'espace de recherche des clés. Ensuite, il teste les K0 retenus pour retrouver la clé de chiffrement. Pour cela, j'ai dû :
- Initialiser des tables de substitution Sbox et son inverse Xobs.
- Utiliser des fonctions de chiffrement et de déchiffrement.
- Calculer la parité des nombres en entrée et en sortie de la boîte S.
- Approximer linéairement la boîte S en calculant le nombre de paires entrée/sortie de la boîte S ayant la même parité binaire pour différentes combinaisons de masques, et en sélectionnant la meilleure paire de masques en se basant sur le tableau de scores obtenu précédemment.
- Générer une liste de paires aléatoires de messages et de chiffres.
- Calculer le score pour chaque masque K0 potentiel et sélectionner les K0 qui satisfont les conditions spécifiées pour la recherche de la clé.
- Enfin, retrouver la clé à partir des K0.


## [ENGLISH PRESENTATION]
Implementation of a linear cryptanalysis attack on a ToyCipher encryption algorithm using linear approximations of the substitution box to reduce the key search space. Then, it tests the retained K0 values to retrieve the encryption key. For this, I had to:
- Initialize substitution tables Sbox and its inverse Xobs.
- Use encryption and decryption functions.
- Calculate the parity of numbers at the input and output of box S.
- Linearly approximate box S by calculating the number of input/output pairs of box S with the same binary parity for different mask combinations, and selecting the best pair of masks based on the previously obtained score table.
- Generate a list of random pairs of messages and ciphertexts.
- Calculate the score for each potential K0 mask and select the K0 that satisfy the specified conditions for key search.
- Finally, retrieve the key from the selected K0 values.


## [Tutoriel / Tutorial]
[FRENCH] Quand le programme se lance, un tableau de parité avec les masques est montré. On y voit la meilleure paire, la clé utilisée, la liste des K0 potentiels conservés et enfin la clé qui est retrouvée  
[ENGLISH] When the program starts, a parity table with the masks is shown. We see the best pair, the key used, the list of retained potential K0 values, and finally the retrieved key  
<div align="center">
<img width="417" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_Linear_cryptanalysis/assets/151149998/288f1a1a-52c3-4a95-8ee7-6e4d57594a7a">
</div>
