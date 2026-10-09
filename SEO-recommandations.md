# Améliorer le référencement — site MGC SAS

## Déjà en place
- Balises `<title>` et meta description sur chaque page
- hreflang FR/EN, sitemap.xml, robots.txt
- Données structurées (JSON-LD `ProfessionalService`) sur les accueils
- Un seul `<h1>` par page, images avec attribut alt

## À corriger sur le site (je peux le faire)
1. **Titres d'accueil** : « projets sensibles » est resté dans le `<title>` et les meta de l'accueil FR/EN. À remplacer par « OSINT & Intelligence ».
2. **Meta description de la page Hyperviseur** : elle parle encore de caméras IP et d'archivage. À réécrire pour l'hyperviseur de sûreté et de sécurité.
3. **Meta description OSINT** : texte générique, à rendre plus précis (veille, investigation numérique, analyse de données).
4. **Canonical et JSON-LD** : présents seulement sur les accueils. À ajouter sur toutes les pages (`<link rel="canonical">`, données structurées `Service`).
5. **Open Graph / Twitter** : à ajouter sur les sous-pages (aperçu des liens partagés sur LinkedIn, etc.).
6. **Noms de fichiers** : `videosurveillance.html` → `hyperviseur.html` (EN : `hypervisor.html`), avec redirection 301 depuis l'ancienne URL.
7. **sitemap.xml** : ajouter `<lastmod>` et le mettre à jour à chaque modification.
8. **Contenu des pages** : 300 à 600 mots utiles par page, avec les mots-clés que tes clients tapent (ex. « hyperviseur de sécurité », « supervision multi-sites », « audit NIS2 », « OSINT entreprise »).
9. **Liens internes** : relier les pages entre elles (ex. Hyperviseur ↔ Cybersécurité) avec des textes de lien explicites.

## À faire hors du site (toi)
1. **Google Search Console** : ajouter `mgc-paris.fr`, vérifier le domaine, envoyer `sitemap.xml`, demander l'indexation de chaque page.
2. **Bing Webmaster Tools** : importer le site depuis Search Console.
3. **Fiche Google Business Profile** : créer ou réclamer la fiche (Paris 8e, et Nice), même adresse/téléphone que sur le site. Gros effet sur la recherche locale.
4. **Annuaires et réseaux** : LinkedIn entreprise, Societe.com, Pappers, annuaires cybersécurité/sécurité privée. Garder le même nom, adresse, téléphone partout.
5. **Backlinks** : articles invités, partenaires, clients, presse spécialisée. Un lien depuis un site fiable vaut plus que dix annuaires.
6. **Blog / actualités** : 1 article par mois (NIS2, RGPD, vidéoprotection, OSINT). Pousse sur les requêtes longues.

## Technique
- Vitesse : tester sur pagespeed.web.dev. Images en WebP et dimensionnées (fait pour l'hyperviseur).
- HTTPS et redirection `mgc-paris.fr` → `www.mgc-paris.fr` (une seule version).
- Mobile : tester dans Search Console, rapport « Ergonomie mobile ».
- Page 404 : déjà en place.

## Priorités
1. Search Console + sitemap
2. Google Business Profile
3. Points 1 à 5 de la liste du site
4. Contenu et backlinks (effet lent, 3 à 6 mois)

Le référencement prend du temps : compter plusieurs semaines pour l'indexation, plusieurs mois pour monter dans les résultats.
