# Guide pas à pas : compteur + newsletter

Ordre conseillé : **A. Publier le site → B. Compteur → C. Newsletter.**
Temps : A ≈ 30 min, B ≈ 15 min, C ≈ 1 h (DNS Brevo : attente possible).

---

## A. Publier le site (obligatoire pour la newsletter)

1. Choisir l'hébergeur (Cloudflare Pages, Netlify, OVH, etc.) et y déposer le contenu du dossier `site/`.
2. Acheter/relier le nom de domaine (ex. `mgc-paris.fr`).
3. Vérifier que `https://TON-DOMAINE/` affiche la page d'accueil.
4. Si le domaine n'est pas `mgc-paris.fr` : remplacer `https://www.mgc-paris.fr` par le vrai domaine dans tous les fichiers (`sitemap.xml`, balises `canonical`, `og:url`, JSON-LD).

---

## B. Compteur de menaces

Le compteur lit un fichier JSON sur GitHub. Un robot GitHub (Actions) le met à jour toutes les 15 min.

### B1. Vérifier que le robot existe
Dans le dépôt GitHub qui héberge le compteur (`cesarsgw/SITE-PRINCIPALE`, voir `data-endpoint` dans `MGC_page_principale.html`), ces 2 fichiers doivent exister :
- `.github/workflows/compteur-menaces.yml`
- `.github/scripts/urlhaus_fr_counter.py`

**Le dépôt `site-` ne les contient pas.** S'ils manquent aussi dans `SITE-PRINCIPALE` : me demander de les recréer.

### B2. Créer la clé abuse.ch
1. Aller sur https://auth.abuse.ch/ et créer un compte gratuit.
2. Copier l'**Auth-Key** affichée.

### B3. Enregistrer la clé dans GitHub
1. Dépôt → **Settings** → **Secrets and variables** → **Actions**.
2. **New repository secret**.
3. Name : `URLHAUS_AUTH_KEY`. Secret : la clé. **Add secret**.

### B4. Mettre les fichiers sur la branche principale
GitHub n'exécute les tâches planifiées que sur la branche par défaut (`main`). Fusionner (merge) la branche de travail dans `main`.

### B5. Premier lancement
1. Onglet **Actions** du dépôt.
2. Cliquer **Compteur menaces (URLhaus FR)**.
3. **Run workflow** → **Run workflow**.
4. Attendre la coche verte. Si rouge : ouvrir le journal.

### B6. Vérifier
Ouvrir dans le navigateur :
`https://raw.githubusercontent.com/cesarsgw/SITE-PRINCIPALE/data/cyber-counter.json`
Le texte doit contenir `"ok": true` et un nombre.

### B7. Résultat
Recharger le site : le header affiche « MENACES ACTIVES · FR » avec le nombre.

### Si ça ne marche pas
| Symptôme | Cause | Solution |
|---|---|---|
| « Données indisponibles » | JSON absent | refaire B5, B6 |
| `"error": "cle_absente"` | secret manquant | B3 |
| `http_401` / `http_403` | clé refusée | regénérer la clé (B2) |
| `http_429` | trop de requêtes | passer le cron à `*/30` |
| Plus de mise à jour | GitHub coupe les tâches après 60 j d'inactivité (dépôt public) | onglet Actions → réactiver |

À faire aussi : écrire à abuse.ch pour confirmer que l'usage sur le site d'une entreprise est gratuit.

---

## C. Newsletter (Brevo + Cloudflare)

Principe : le site envoie l'email à un petit serveur (Worker Cloudflare) qui parle à Brevo avec la clé secrète. Double opt-in : l'inscription n'est valide qu'après clic sur l'email de confirmation.

### C1. Compte Brevo
1. Créer un compte gratuit sur https://www.brevo.com.

### C2. Domaine d'envoi (nécessite le domaine de l'étape A)
1. Brevo → **Expéditeurs, domaines et IP dédiées** → **Domaines** → ajouter le domaine.
2. Brevo affiche des enregistrements DNS (DKIM, DMARC…). Les ajouter chez le gestionnaire du domaine.
3. Cliquer **Authentifier** (peut prendre de quelques minutes à 48 h).
4. Créer l'expéditeur : `newsletter@TON-DOMAINE`.

### C3. Liste de contacts
1. **Contacts** → **Listes** → **Créer une liste** → nom `Newsletter MGC`.
2. **Noter son ID** (numéro).

### C4. Email de confirmation (double opt-in)
1. **Modèles d'email** → **Nouveau modèle**.
2. Ajouter un bouton « Confirmer mon inscription » dont le lien est exactement `{{ doubleoptin }}`.
3. Ajouter le **tag** `optin`, puis **activer** le modèle.
4. **Noter son ID**. (Facultatif : un 2e modèle en anglais, avec son ID.)

### C5. Clé API
1. **SMTP & API** → **Clés API** → **Générer** (nom `site-newsletter`).
2. La copier tout de suite : elle ne s'affiche qu'une fois.

### C6. Autoriser les appels du Worker
1. **Paramètres** → **Sécurité** → **IP autorisées**.
2. **Désactiver le blocage** (sinon erreur 401 : les IP Cloudflare changent).

### C7. Créer l'API sur Cloudflare
1. Compte gratuit sur https://dash.cloudflare.com.
2. **Workers & Pages** → **Create** → **Create Worker**.
3. Nom `mgc-newsletter` → **Deploy**.
4. **Edit code** → tout effacer → coller le contenu de `newsletter-api/worker.js` → **Deploy**.
5. **Settings** → **Variables and Secrets** → ajouter :

| Nom | Type | Valeur |
|---|---|---|
| `BREVO_API_KEY` | Secret | clé de C5 |
| `BREVO_LIST_ID` | Texte | ID de C3 |
| `BREVO_DOI_TEMPLATE_ID` | Texte | ID de C4 |
| `BREVO_DOI_TEMPLATE_ID_EN` | Texte (option) | ID du modèle anglais |
| `DOI_REDIRECT_URL` | Texte | `https://TON-DOMAINE/?newsletter=confirmee#newsletter` |
| `DOI_REDIRECT_URL_EN` | Texte (option) | `https://TON-DOMAINE/en/home.html?newsletter=confirmed#newsletter` |
| `ALLOWED_ORIGINS` | Texte | `https://www.TON-DOMAINE,https://TON-DOMAINE` |

6. **Deploy**.
7. Copier l'URL du Worker : `https://mgc-newsletter.TON-COMPTE.workers.dev`.

### C8. Brancher le site
Dans `site/MGC_page_principale.html` **et** `site/en/home.html`, remplacer :
```html
<form class="newsletter-form" id="newsletterForm" data-endpoint="" novalidate>
```
par :
```html
<form class="newsletter-form" id="newsletterForm" data-endpoint="https://mgc-newsletter.TON-COMPTE.workers.dev" novalidate>
```
Republier le site.

### C9. Tester
1. Sur le site en ligne : saisir **sa propre adresse**, cocher la case, **S'inscrire** → « email de confirmation envoyé ».
2. Brevo → liste : le contact n'y est pas encore (normal).
3. Ouvrir l'email → **Confirmer** → retour sur le site « inscription confirmée ».
4. Brevo → liste : le contact est présent.
5. Se réinscrire avec la même adresse → « déjà inscrite ».
6. Envoyer une campagne test, cliquer le lien de désinscription → le contact est retiré.

### En cas d'échec
Cloudflare → Worker → **Logs**. Messages `newsletter:` avec le code Brevo :
- 401 : clé fausse ou IP non autorisées (C6)
- 400 : ID de modèle ou de liste faux
- « origine refusée » : `ALLOWED_ORIGINS` ne correspond pas au domaine

---

## D. À faire avant d'annoncer

- Boîte `dpo@mgcsas.fr` : vérifier qu'elle existe et reçoit.
- Faire valider les mentions légales par un juriste.
- Confirmer avec abuse.ch l'usage du compteur.
