# Newsletter et compteur : que faut-il pour qu'ils marchent ?

## Réponse courte

- **Newsletter** : oui, ne marche qu'après mise en ligne **et** configuration Brevo + Cloudflare.
- **Compteur de menaces** : ne dépend pas de la mise en ligne du site, mais d'un dépôt GitHub configuré.

## Newsletter

État actuel : `data-endpoint=""` (page principale et `en/home.html`) → le formulaire affiche « inscription momentanément indisponible ».

À faire, dans l'ordre (détails : `NEWSLETTER-BREVO.md`) :
1. Compte Brevo + liste + modèle de confirmation + clé API.
2. Déployer `newsletter-api/worker.js` sur Cloudflare Workers (gratuit), avec les variables.
3. Domaine du site publié : nécessaire pour
   - `ALLOWED_ORIGINS` (seul le vrai domaine peut appeler l'API),
   - `DOI_REDIRECT_URL` (retour après confirmation),
   - le domaine d'envoi Brevo (DNS DKIM/DMARC, expéditeur `newsletter@...`).
4. Mettre l'URL du Worker dans `data-endpoint` (2 fichiers) puis republier.
5. Tester avec sa propre adresse (section 6 de `NEWSLETTER-BREVO.md`).

Le Worker peut être créé avant la mise en ligne, mais le test complet exige le site en ligne.

## Compteur de menaces

Le navigateur lit un fichier JSON sur GitHub (`raw.githubusercontent.com/.../data/cyber-counter.json`), pas sur ton site. Donc il fonctionne depuis n'importe quelle adresse, dès que le JSON existe.

Prérequis (détails : `COMPTEUR-MENACES.md`) :
1. Clé abuse.ch (Auth-Key) enregistrée en secret GitHub `URLHAUS_AUTH_KEY`.
2. Workflow `compteur-menaces.yml` présent sur la branche par défaut (`main`).
3. Premier lancement manuel dans l'onglet *Actions*.
4. Branche `data` créée par le workflow.

Attention :
- Le dépôt actuel `site-` ne contient **aucun** dossier `.github` (workflow et script absents). Le `data-endpoint` pointe vers le dépôt `cesarsgw/SITE-PRINCIPALE`. Il faut que le workflow soit bien dans ce dépôt-là.
- Tant que le JSON n'existe pas : le compteur affiche « Données indisponibles ».
- abuse.ch peut demander un abonnement pour usage commercial : à confirmer par mail.
