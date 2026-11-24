# Lab Funbox:CTF (VulnHub) — lancer + connecter Kali

## 1. Import VM cible
- Fichier : `.ova` (ou zip → extraire)
- VirtualBox : Fichier → Importer un appareil virtuel → choisir `.ova` → Importer
- Ne pas démarrer encore

## 2. Réseau (IMPORTANT : même réseau pour 2 VM)

Option A — Host-Only (isolé, recommandé)
1. VirtualBox → Fichier → Outils → Gestionnaire réseau → Host-only → Créer (DHCP activé)
2. Funbox : Configuration → Réseau → Adaptateur 1 → "Réseau privé hôte" → vboxnet0
3. Kali : Configuration → Réseau → Adaptateur 1 → "Réseau privé hôte" → vboxnet0
   - (optionnel) Adaptateur 2 sur NAT pour avoir internet dans Kali

Option B — Réseau NAT (isolé + internet)
1. Fichier → Outils → Gestionnaire réseau → Réseaux NAT → Créer (DHCP activé)
2. Funbox + Kali : Adaptateur 1 → "Réseau NAT" → même réseau

Option C — Bridge (même LAN que box/routeur)
- Les 2 VM : "Accès par pont" → carte réseau physique
- Moins sûr (VM vulnérable exposée au LAN)

## 3. Démarrer
- Lancer Funbox (écran login = normal, pas besoin de creds)
- Lancer Kali

## 4. Trouver IP de Funbox (depuis Kali)

```bash
ip a                              # voir IP Kali + range (ex: 192.168.56.101/24)
sudo netdiscover -r 192.168.56.0/24
# ou
nmap -sn 192.168.56.0/24
# ou
sudo arp-scan -l
```

Cible = IP qui n'est pas Kali / gateway (.1 = hôte, .100 = DHCP VBox).

## 5. Tester connexion

```bash
ping -c 3 <IP_FUNBOX>
nmap -sC -sV -p- <IP_FUNBOX> -oN funbox.nmap
```

## 6. Dépannage
- Pas d'IP Kali : `sudo dhclient eth0` ou redémarrer réseau
- Ping KO : vérifier même réseau sur les 2 VM, adaptateur "Câble branché" coché
- Funbox sans IP : Adaptateur en mode "PCnet-FAST III" ou "Intel PRO/1000" (changer type de carte)
- Netdiscover vide : mauvaise interface → `sudo netdiscover -i eth0 -r <range>`
- VMware au lieu de VirtualBox : importer `.ova`, réseau Host-only (VMnet1) ou NAT (VMnet8) sur les 2 VM

## 7. Ensuite
```bash
nmap -sC -sV <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirb/common.txt
```
