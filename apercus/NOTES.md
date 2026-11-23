# Récap modifs

| Demande | Fait |
|---|---|
| Palette pptx | `#13171B` `#212326` `#404245` `#FFFFFF` bronze `#84482D` `#5F3420` + drapeau `#002395` `#ED2939`. Tout CSS/HTML remappé (var `--signal` = bronze). Tons intermédiaires = mélanges de ces couleurs (`color-mix`). |
| Drapeau plein écran | Cause probable : filtre SVG `feTurbulence` énorme (région 140 %, animé) → GPU dépasse limite texture en grand écran/HiDPI → drapeau disparaît. Fix : filtre supprimé, drapeau = bandes + plis en dégradé animés en CSS. Testé 1440/1920/2560/3840 : visible. Plus masqué si « réduire animations ». |
| Titre | « LES MOTS DU PRÉSIDENT » → « LE MOT DU PRÉSIDENT » (singulier, correct en français ; dis-moi si tu veux vraiment « LE MOTS »). |
| Citation | 2 paires « … » : phrase en gras + 3 paragraphes suivants. |
| Hyperviseur → Sécurité | `index.html` (titre, liste déroulante, pied de page), `videosurveillance.html` (titre + h1), `404.html`. Aussi EN : Hypervisor → Security. |
| Quadrillage | `.hero-grid` supprimé (HTML + CSS). |
| Logo | 56 → 72 px (sous-pages 40 → 54 px), décalé vers la gauche. |
| Polices | `polices.html` (6 propositions). Pas encore appliquée. Reco : n°1 (Prata = police du pptx). |

Site modifié : dossier `www/`. Avant/après : `apercus/*-avant.png` / `*-apres.png`.
