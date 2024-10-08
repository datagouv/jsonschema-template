# Template de départ pour Json Schema

Ce dépôt contient les fichiers nécessaires pour démarrer la création d'un dépôt pour un schéma [Json Schema](https://json-schema.org/).

## Utiliser ce template

- Si vous créez votre dépôt sur GitHub, il vous suffit d'appuyer sur le bouton vert "Use this template". Consultez [la documentation](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) pour plus d'infos ;
- Si votre projet sera hébergé ailleurs (par exemple Gitlab), vous pouvez cloner ce répertoire ou télécharger les fichiers correspondants. Utilisez le bouton "Clone or download".

## Fichiers disponibles

Ce dépôt contient un ensemble de fichiers utiles pour un dépôt d'un schéma [Json Schema](https://json-schema.org/).

- [`product.json`](product.json) est le schéma au format Json Schema (à renommer) ;
- [`exemple-valide.json`](exemple-valide.json) est un fichier json d'exemple conforme par rapport au schéma décrit dans `product.json`  ;
- [`CHANGELOG.md`](CHANGELOG.md) contient la liste des changements entre les différentes versions de votre schéma ;
- [`LICENSE.md`](LICENSE.md) est le fichier de licence du dépôt. Nous recommandons d'utiliser la [Licence Ouverte](https://www.etalab.gouv.fr/licence-ouverte-open-licence), cette licence est recommandée par l'administration française pour le partage de données et de documents ;
- [`README.md`](README.md) est le fichier que vous lisez actuellement. À terme, il devra présenter votre schéma ;
- [`requirements.txt`](requirements.txt) liste les dépendances Python nécessaires pour effectuer des tests en intégration continue sur votre dépôt ;
- [`schemas.yml`](schema.yml) est le fichier technique qui lie le schéma à schema.data.gouv.fr.

### Intégration continue

Ce dépôt est configuré pour utiliser de l'intégration continue, si vous utilisez GitHub. À chaque commit, une suite de tests sera lancée via [GitHub Actions](https://github.com/features/actions) afin de vérifier :

- que votre schéma est valide à la spécification Json Schema ;
- que vos fichiers d'exemples sont conformes au schéma.

Si vous n'utilisez pas GitHub, vous pouvez lancer ces tests sur votre machine ou sur un autre service d'intégration continue comme Gitlab CI, Jenkins, Circle CI, Travis etc. Consultez la configuration utilisée dans [`.github/workflows`](.github/workflows).


## Documentation

Pour vous aider dans la construction de votre dépôt, nous vous recommandons de vous référer à :

- [Le guide à destination des producteurs de schéma](https://guides.data.gouv.fr/guides-open-data/guide-qualite/maitriser-les-schemas-de-donnees)
- [La documentation de schema.data.gouv.fr](https://schema.data.gouv.fr)
- [La spécification Json Schema](https://json-schema.org/)