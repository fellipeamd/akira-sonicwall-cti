# Cyber Kill Chain

| Phase | What Akira does | Source | Defensive opportunity |
|-------|-----------------|--------|-----------------------|
| **Reconnaissance** | Identifies internet-exposed SonicWall SSL VPN portals (inferred from targeting pattern) | S01 | Reduce exposure<br>Restrict VPN access to trusted sources |
| **Weaponisation** | Obtains valid VPN credentials (initial access brokers, brute force, password spraying) or prepares exploitation of CVE-2024-40766 | S01 | Monitor for leaked credentials<br>Enforce account lockout |
| **Delivery** | Connects to the internet-facing SSL VPN portal | S01 | Log all SSL VPN logins<br>Alert on logins from hosting providers or unusual locations<br>Enable botnet filtering |
| **Exploitation** | Exploits CVE-2024-40766 or uses valid credentials, including local passwords carried over from Gen 6 to Gen 7 migrations | S01, S02, S03 | Patch<br>Enforce MFA<br>Reset credentials |
| **Installation** | Installs remote access tools (AnyDesk, LogMeIn) and creates new admin accounts (e.g. "itadm") | S01 | Detect new remote access software<br>Detect new privileged accounts |
| **Command & Control** | Tunnels traffic through Ngrok and Cloudflare Tunnel; uses SystemBC and Cobalt Strike | S01 | Block or alert on tunnelling tools<br>Monitor unusual outbound connections |
| **Actions on Objectives** | Dumps credentials, moves laterally, deletes shadow copies, exfiltrates data (RClone, WinSCP), encrypts systems including ESXi hypervisors | S01 | Detect LSASS access and shadow copy deletion<br>Monitor large outbound transfers<br>Keep offline, immutable backups |