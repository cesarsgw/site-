# Optimiser Claude : guide complet

## 1. Contexte permanent (le plus gros levier)
- Fichier `CLAUDE.md` à la racine du repo : Claude le lit à chaque session.
- Y mettre : qui tu es, objectifs, style de réponse voulu, projets en cours, règles ("réponses courtes", "français", "demande avant d'agir").
- Créer avec la commande `/init`, puis éditer à la main.
- Mémoire : dis "retiens que ..." pour les préférences durables.

## 2. Économiser les tokens
- Un sujet = une session. Nouvelle tâche = nouvelle session (`/clear`).
- `/compact` quand la conversation est longue.
- Donne chemin exact du fichier au lieu de "cherche le fichier".
- Demande format court : "liste 5 puces", "tableau", "1 page max".
- Évite de coller de gros textes ; mets-les dans un fichier et cite le chemin.
- Pour recherche large, demande un sous-agent : il lit beaucoup, te rend seulement la conclusion.
- Choisis le bon modèle : petit modèle pour tâches simples, gros pour réflexion/stratégie (`/model`).

## 3. Qualité des réponses
- Donne le **rôle** : "agis comme CFO sceptique", "investisseur", "avocat du diable".
- Donne le **critère de réussite** : "bon = prêt à envoyer à une banque".
- Demande **3 à 5 variantes**, puis choisis et affine.
- Demande **critique avant exécution** : "quelles failles dans mon idée ?"
- Exemples : montre un bon exemple de ce que tu veux (few-shot).
- Étapes : "plan d'abord, j'valide, puis tu exécutes".
- Dis ce que tu **ne veux pas** ("pas de cliché, pas de généralités").
- Chiffres réels > vagues. Sinon exige "marque les hypothèses".

## 4. Créativité
- "Donne 10 idées bizarres, puis 3 réalistes."
- Contraintes fortes : "budget 0", "en 7 jours", "sans publicité".
- Croiser domaines : "comment [autre secteur] ferait ça ?"
- Inversion : "comment échouer à coup sûr ?" puis inverse.
- Pré-mortem : "dans 1 an le projet a échoué, pourquoi ?"

## 5. Outils à exploiter dans cet environnement
- **Recherche web** : marché, concurrents, prix, réglementation réels.
- **Fichiers** : Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF : produits directement.
- **Docs / Artifacts** : pages web partageables, dashboards, tableaux financiers interactifs.
- **Gmail / Calendar / Drive** (connectés) : brouillons de mails, planning, lecture de documents.
- **Sous-agents / workflows** : tâches en parallèle (ex : analyser 5 concurrents d'un coup).
- **Tâches récurrentes** : rappels, veille hebdomadaire.
- **Git** : tout versionner, retour arrière facile.

## 6. Workflow business plan optimal
1. Brief : idée, cible, pays, budget, délai, ton profil.
2. Critique de l'idée (failles, risques).
3. Étude de marché (recherche web, sources citées).
4. Offre + prix + positionnement.
5. Modèle financier (Excel, hypothèses explicites, 3 scénarios).
6. Plan marketing + ventes.
7. Plan d'action 90 jours.
8. Document final (Word/PDF) + pitch (PowerPoint).
- Un fichier par étape dans le repo ; Claude relit ce dont il a besoin.

## 7. Pièges à éviter
- Prompt vague → réponse vague.
- Tout demander en un message → qualité baisse.
- Croire sans vérifier : chiffres et lois = demander sources, vérifier.
- Session interminable → coût + dérive. Résume dans un fichier, repars neuf.
- Ne pas dire ton niveau : précise débutant/expert.

## 8. Modèle de prompt réutilisable
```
Rôle : [expert X]
Contexte : [projet, cible, pays, budget]
Tâche : [une seule chose]
Format : [tableau / 10 lignes / fichier .md]
Contraintes : [ton, longueur, à éviter]
Succès = [critère]
Avant d'agir : pose-moi les questions indispensables.
```

## 9. Réglages utiles
- `/model` : changer de modèle.
- `/compact` : résumer la conversation.
- `/clear` : repartir à neuf.
- `/init` : créer CLAUDE.md.
- Préférences utilisateur (déjà actives) : mode court, style minimal.
