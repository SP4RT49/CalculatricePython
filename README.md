# CalculatricePython
Calculatrice développé en python

# Git ?

Git est un système de gestion de version décentralisé, largement utilisé pour le développement de logiciels, mais aussi dans d'autres domaines où la gestion de versions est importante.

## Qu'est-ce qu'un dépot ?


Un dépôt Git, souvent appelé simplement "repository" en anglais, est un endroit où Git stocke l'historique des modifications d'un ensemble de fichiers.

Un dépôt Git contient généralement les éléments suivants :

1. Les fichiers de votre projet : Tous les fichiers sources, documents, images, etc., qui font partie de votre projet.

2. L'historique des modifications : Git conserve un historique de toutes les modifications apportées aux fichiers du projet. Chaque modification est enregistrée avec un commentaire (message de commit) qui décrit la nature de la modification, la date et l'auteur de la modification.

3. Les branches : Git permet de créer différentes branches (ou branches de développement) dans un dépôt. Chaque branche peut représenter une version différente du projet, une fonctionnalité en cours de développement, etc.

4. Les tags : Les tags sont des références statiques à un état particulier du projet. Ils sont souvent utilisés pour marquer des versions stables ou des jalons importants.

5. Les informations sur les contributeurs : Git conserve également des informations sur les auteurs de chaque modification, ce qui permet de suivre qui a contribué à quelles parties du projet.

Les dépôts Git sont essentiels pour le développement collaboratif, car ils permettent à plusieurs personnes de travailler sur le même projet en parallèle. Chaque personne peut créer sa propre copie du dépôt (un "clone"), apporter des modifications à sa copie, puis fusionner ces modifications dans le dépôt principal. Git gère les conflits éventuels entre les modifications apportées par différentes personnes.

## Comment créer un dépot ?

Pour créer un dépot GIT, il faut le faire depuis le site web [GitHub](https://github.com/) ou [GitLab](https://gitlab.com/).

Une fois le répository créé, il vous suffit d'effectuer les commandes suivantes afin de le récupérer en local sur cotre machine :

`git clone [url_du_repository]`.

Si toutefois, vous avez déjà créer les fichiers en local. il vous suffira d'éffectuer les commandes suivantes :

```
git remote add origin [url_du_repository]
git branch -M main
git push -u origin main
```

## Qu'est-ce qu'un commit ?

Un commit Git est une opération fondamentale dans le système de gestion de versions Git. Un commit représente un point dans l'historique de votre projet, généralement associé à une série de modifications apportées à vos fichiers. Chaque commit est accompagné d'un message de commit qui décrit les changements effectués. Les commits sont essentiels pour suivre l'évolution de votre code et pour collaborer efficacement avec d'autres développeurs.

Voici quelques points clés sur les commits Git :

1. Instantané des fichiers : Lorsque vous effectuez un commit, Git crée un instantané (ou une "capture") de l'état actuel de vos fichiers dans le répertoire de travail. Il enregistre les modifications apportées depuis le dernier commit.

2. Historique linéaire : Les commits sont stockés dans un ordre linéaire, formant une chaîne chronologique d'instants de l'historique de votre projet. Chaque commit a un identifiant unique (hash) basé sur le contenu des modifications, ce qui garantit l'intégrité de l'historique.

3. Messages de commit : Chaque commit est accompagné d'un message de commit. Ce message doit être informatif et décrire de manière concise les changements apportés dans le commit. Les messages de commit aident les développeurs à comprendre pourquoi les modifications ont été apportées.

4. Références de branches : Les commits sont associés à des branches (ou des étiquettes) dans un dépôt Git. Ils définissent l'état actuel de la branche à laquelle ils sont rattachés. Les branches évoluent à mesure que de nouveaux commits sont ajoutés.

5. Facilité de navigation dans l'historique : Vous pouvez naviguer dans l'historique de votre projet en remontant et en descendant dans les commits. Cela vous permet de revenir à un état antérieur du projet ou de suivre les changements entre deux points de l'historique.

5. Revue de code et collaboration : Les commits facilitent la collaboration entre développeurs. Les membres de l'équipe peuvent examiner les commits, ajouter des commentaires, et discuter des modifications apportées dans le contexte de chaque commit.

Pour effectuer un commit, vous pouvez utiliser la commande git commit en spécifiant un message de commit. Par exemple :

`git commit -m "Ajout de la fonction de connexion à l'application"`

Les commits sont l'une des principales raisons pour lesquelles Git est un outil puissant pour la gestion de versions. Ils vous permettent de suivre et de documenter les changements apportés à votre projet au fil du temps, ce qui facilite la collaboration, le débogage et la gestion des versions de votre logiciel.

## Qu'est-ce qu'une branche ?

Une branche (ou branch en anglais) est une fonctionnalité essentielle de Git, un système de gestion de versions décentralisé. Les branches permettent aux développeurs de travailler sur des versions distinctes d'un projet en parallèle. Chaque branche représente une ligne de développement indépendante avec son propre historique de commits, ce qui facilite la gestion de versions, la collaboration et le développement de nouvelles fonctionnalités.

Voici quelques points clés concernant les branches Git :

1. Isolation du développement : L'utilisation de branches permet d'isoler le développement de différentes fonctionnalités, correctifs ou expériences. Cela signifie que vous pouvez travailler sur une fonctionnalité sans affecter le code en cours sur la branche principale (généralement appelée "master" ou "main").

2. Historique de commits distinct : Chaque branche a son propre historique de commits, ce qui signifie que les commits effectués sur une branche n'affectent pas les autres branches. Vous pouvez donc expérimenter, tester des idées et effectuer des modifications sans perturber le travail des autres membres de l'équipe.

3. Passage d'une branche à l'autre : Vous pouvez passer d'une branche à l'autre à tout moment en utilisant la commande git checkout ou git switch pour travailler sur une branche différente. Par exemple, pour passer à une branche appelée "feature-nouvelle", vous pouvez utiliser la commande :
`git checkout feature-nouvelle`

4. Fusion de branches : Une fois que vous avez terminé de travailler sur une branche (par exemple, lorsque vous avez développé une nouvelle fonctionnalité), vous pouvez fusionner cette branche avec une autre branche (généralement la branche principale) pour incorporer les modifications. La fusion combine les modifications apportées dans une branche avec celles d'une autre.
`git merge feature-nouvelle`

5. Création de nouvelles branches : Vous pouvez créer de nouvelles branches à tout moment pour travailler sur des tâches spécifiques. Par exemple, pour créer une nouvelle branche appelée "feature-exemple", vous pouvez utiliser la commande :
`git checkout -b feature-exemple`

6. Suppression de branches : Une fois qu'une branche n'est plus nécessaire, vous pouvez la supprimer en utilisant la commande git branch -d. Par exemple :
`git branch -d feature-exemple`

Les branches Git offrent une grande flexibilité dans la gestion de versions et la collaboration sur des projets, car elles permettent aux développeurs de travailler de manière parallèle tout en maintenant un historique clair et organisé des modifications. Cela rend également plus facile la gestion de correctifs, le développement de nouvelles fonctionnalités et la gestion de versions stables de votre logiciel.

# Type de licence
## Licence MIT

**La licence MIT est une licence de logiciel libre qui accorde des droits considérables aux utilisateurs du code source. Voici les caractéristiques clés de cette licence :**

**Utilisation libre :** Les utilisateurs sont autorisés à utiliser, copier, modifier, fusionner, publier, distribuer, sous-licencier et/ou vendre le code, que ce soit à des fins commerciales ou non.

**Clause de limitation de responsabilité :** La licence MIT inclut une clause de limitation de responsabilité, déchargeant essentiellement l'auteur de toute responsabilité pour les éventuels dommages causés par l'utilisation du code.

**Clause de droits d'auteur :** Les utilisateurs doivent conserver l'avis de droits d'auteur dans les copies du code.

**Clause de licence :** Les utilisateurs doivent inclure une copie complète de la licence MIT dans leurs distributions.

# Résumé des différentes étapes pour créer et utiliser un dépôt GitHub

## 1. Créer un compte GitHub

- Inscrivez-vous sur [github.com](https://github.com/).
- Fournissez un nom d'utilisateur, une adresse e-mail, et un mot de passe.

## 2. Créer un Nouveau Dépôt

- Cliquez sur "Your repositories" depuis votre profil.
- Sélectionnez "New" pour créer un nouveau dépôt.
- Nommez votre dépôt, ajoutez une description, et choisissez sa visibilité.
- Optionnel : initialisez avec un fichier README, .gitignore, ou choisissez une licence.
- Cliquez sur "Create repository".

## 3. Cloner le Dépôt

- Copiez l'URL du dépôt depuis GitHub.
- Ouvrez un terminal et exécutez `git clone [URL]`.

## 4. Faire des Modifications Locales

- Naviguez dans le dossier du dépôt cloné.
- Créez ou modifiez des fichiers.
- Utilisez `git add [fichier]` et `git commit -m "message de commit"` pour enregistrer vos changements.

## 5. Pousser les Modifications sur GitHub

- Exécutez `git push origin main` pour envoyer vos modifications.

## 6. Gestion des Branches

- Créez des branches avec `git branch [nom_de_la_branche]`.
- Basculer entre les branches avec `git checkout [nom_de_la_branche]`.

## 7. Pull Requests et Fusion (Merge)

- Créez ou modifiez des fichiers.
- Utilisez `git add [fichier]` et `git commit -m "message de commit"` pour enregistrer vos changements.
- Exécutez `git push origin [nom_de_la_branche]` pour envoyer vos modifications.
- Créez une "Pull Request" sur GitHub sur la branche `main` pour proposer vos changements.
- Les mainteneurs peuvent examiner, discuter, et fusionner vos modifications.

## 8. Récupérer les Dernières Modifications

- Retourner sur main `git checkout main`
- Utilisez `git pull` pour récupérer et fusionner les modifications depuis GitHub.

## Conclusion

GitHub est essentiel pour la gestion de version et la collaboration dans des projets de programmation.
