# Cyber Kill Chain

| Phase | What Akira does | Source | Defensive opportunity |
|-------|-----------------|--------|-----------------------|
| Reconnaissance | Identifies exposed SonicWall SSL VPN | | Reduce exposure; restrict VPN access |
| Weaponisation | | | |
| Delivery | | | |
| Exploitation | Exploits CVE-2024-40766 or uses valid credentials | | Patch; enforce MFA; reset credentials |
| Installation | Installs remote access tools | | Detect new remote access software |
| Command & Control | | | |
| Actions on Objectives | Deletes backups, exfiltrates, encrypts | | Detect shadow copy deletion; offline backups |