# Akira Ransomware: Initial Access via SonicWall SSL VPN

**Technical Report**

| | |
|---|---|
| **Classification** | TLP:CLEAR |
| **Assessment date** | 27 September 2026 |
| **Audience** | Network defenders, SOC analysts, incident responders |
| **Author** | Fellipe Desinde |
| **Scope** | August 2024 – present; EU, with a focus on Belgium |

> *Portfolio assessment written from the perspective of a national cybersecurity authority. It is not an official product of any organisation and is based exclusively on open sources and passive research. Source IDs (S01–S06) refer to `02-source-log.md`.*

---

## 1. Bottom Line Up Front

Akira ransomware actors gain access to victim networks through internet-exposed SonicWall SSL VPN portals, either by exploiting CVE-2024-40766 (Critical Improper Access Control Vulnerability) or by logging in with valid, stolen or brute-forced credentials. The common enabler is an SSL VPN without multi-factor authentication (MFA).

**Patching alone is not enough.** In 2025, patched SonicWall Gen 7 devices were compromised because local SSL VPN passwords had been migrated from older Gen 6 devices without being reset (S02). Once inside, Akira can move from access to data exfiltration in hours (S01).

**Priority actions:** patch or replace affected devices, reset all local SSL VPN credentials, enforce MFA, restrict VPN access to trusted sources, and monitor SSL VPN logins. No public Sigma rule covers this initial access stage, so organisations must build that detection on their own firewall logs.

---

## 2. Intelligence Requirement

**PIR:** How does Akira ransomware gain initial access through SonicWall SSL VPN, and what should Belgian defenders prioritise to detect and stop an intrusion before encryption?

| EEI | Question | Answered in |
|---|---|---|
| 1 | Which initial access vectors does Akira use against SonicWall devices? | Section 4 |
| 2 | How severe and how actively exploited is CVE-2024-40766? | Section 5 |
| 3 | Which techniques does Akira use between initial access and encryption? | Section 6 |
| 4 | How much time typically passes between access and encryption? | Section 6 |
| 5 | Which log sources and detection rules can catch these techniques early? | Section 7 |

---

## 3. Key Judgements

*Probability terms follow ICD 203: almost no chance (1–5%) – very unlikely (5–20%) – unlikely (20–45%) – roughly even chance (45–55%) – likely (55–80%) – very likely (80–95%) – almost certain (95–99%).*

1. We assess it is **likely** (**moderate** confidence) that Akira's primary initial access vector against SonicWall devices is access to internet-exposed SSL VPN portals without MFA, either by exploiting CVE-2024-40766 or by using valid, stolen or brute-forced credentials. (S01, S02, S03)
2. We assess it is **likely** (**moderate** confidence) that the window between initial access and data exfiltration is measured in hours rather than days in at least some intrusions, leaving defenders limited time to respond before encryption. (S01)
3. We assess it is **likely** (**moderate** confidence) that organisations which patched CVE-2024-40766 without resetting local SSL VPN credentials and enforcing MFA remain exposed. (S02)
4. We assess it is **very likely** (**moderate** confidence) that Akira will continue to use internet-exposed SSL VPN appliances, including SonicWall, as an initial access vector over the next 6–12 months. (S01, S02, S03, S06)
5. We assess there is a **roughly even chance** (**low** confidence) that Belgian organisations in Akira's preferred sectors have been or will be targeted through this vector. (S01, S05)

---

## 4. Initial Access (EEI 1)

Akira actors use three related vectors against SonicWall devices:

| Vector | ATT&CK | Evidence | Rating |
|---|---|---|---|
| Exploitation of CVE-2024-40766 | T1190 | CISA/FBI assess that Akira likely abused this vulnerability for initial access (S01). SonicWall confirms it affects SonicOS management access and SSL VPN (S02). | B3 |
| Valid, stolen or brokered VPN credentials | T1078, T1133 | Access through compromised VPN credentials, potentially bought from initial access brokers (S01). | B2 |
| Brute force and password spraying | T1110, T1110.003 | Brute-forcing of VPN endpoints and password spraying (S01). SonicWall recommends account lockout, consistent with this threat (S02). | B2 |

**Enabling condition:** both sources point to SSL VPN access without MFA as the key weakness (S01, S02).

**Assessment.** The three vectors are connected. SonicWall asked Gen 5 and Gen 6 customers to reset local SSL VPN passwords, not only to patch (S02). The 2025 wave confirmed why: credentials that remained valid after patching were reused against Gen 7 devices (S02). An attacker can therefore obtain credentials through the vulnerability and use them long after the patch is applied.

**Confidence: moderate.** The link between Akira and CVE-2024-40766 relies on a single source (S01), which uses hedged language.

---

## 5. Vulnerability Assessment: CVE-2024-40766 (EEI 2)

| Metric | Value | Source | Retrieved |
|---|---|---|---|
| CVSS v3 (vendor) | 9.3 Critical | S02 | — |
| CVSS v3 (NVD) - NIST | 9.8 Critical | S04 | 28 Sept 2026 |
| EPSS | 0.1838 (97th percentile) | S06 | 26 Sep 2026 |
| CISA KEV | Yes, added 9 Sep 2024; known ransomware use | S03 | 26 Sep 2026 |

**Affected products (S02):** SonicWall Gen 5 and Gen 6 firewalls, and Gen 7 devices running SonicOS 7.0.1-5035 or older. End-of-life devices (NSA 2600, Gen 5 excluding SOHO) will receive no patch.

**Timeline**

| Date | Event | Source |
|---|---|---|
| 22 Aug 2024 | Vendor disclosure | S02 |
| 6 Sep 2024 | SSL VPN added as affected; potential exploitation in the wild noted | S02 |
| 9 Sep 2024 | Added to CISA KEV, with known ransomware use | S03 |
| Jul–Aug 2025 | New wave against Gen 7 devices, linked by SonicWall to CVE-2024-40766 and migrated credentials, not a zero-day | S02 |
| 13 Nov 2025 | CISA/FBI update links Akira's initial access to CVE-2024-40766 | S01 |

**Why this vulnerability should be prioritised.** CVE-2024-40766 should be treated as an immediate priority, well beyond what its CVSS score alone suggests. Exploitation is confirmed (S03), and CISA/FBI link it to Akira's initial access (S01). Its EPSS score places it among the top 3% of all CVEs for likelihood of exploitation, almost two years after disclosure (S06). It affects the SSL VPN of an edge device, exposed to the internet by design. Most importantly, a firmware update is not sufficient: the 2025 wave compromised patched devices whose local passwords had not been reset, and end-of-life devices remain permanently vulnerable (S02).

---

## 6. Attack Chain: From Access to Encryption (EEI 3 and 4)

After initial access, Akira relies heavily on legitimate tools that blend in with normal administration (S01). The ATT&CK Navigator layer (`03-analysis/attack-layer.json`) is the primary analytical model; the table below summarises the main techniques reported in S01.

| Tactic | Technique | Observed behaviour (S01) |
|---|---|---|
| Initial Access | T1133, T1078, T1190 | SSL VPN access with stolen credentials or CVE exploitation |
| Credential Access | T1110 | Brute force and password spraying of VPN endpoints |
| Persistence | T1136 | New local and domain admin accounts, e.g. `itadm` |
| Credential Access | T1003.001, T1003.003 | Mimikatz and LaZagne; LSASS dumping; NTDS.dit extracted by copying a powered-down domain controller's virtual disk |
| Discovery | T1018, T1482, T1046 | `nltest`, `net` commands, Advanced IP Scanner, SoftPerfect NetScan |
| Defense Evasion | T1562.001 | Disabling or uninstalling EDR and antivirus, including via vulnerable drivers (BYOVD) |
| Privilege Escalation | T1068 | Exploitation of unpatched Veeam Backup & Replication (CVE-2023-27532, CVE-2024-40711) |
| Lateral Movement | T1021.001, T1021.004 | RDP and SSH |
| Command and Control | T1219, T1572 | AnyDesk, LogMeIn; tunnelling through Ngrok and Cloudflare Tunnel; SystemBC; Cobalt Strike |
| Exfiltration | T1567.002, T1048 | RClone to cloud storage (e.g. MEGA), WinSCP, FileZilla |
| Impact | T1490, T1486 | Shadow copy deletion; encryption of Windows systems and hypervisors (VMware ESXi, Hyper-V, Nutanix AHV) |

**Speed (EEI 4).** In some incidents, Akira exfiltrated data just over two hours after initial access (S01). No source reported the typical time to encryption. Detection must therefore focus on the earliest stages of the intrusion.

**Note on the Cyber Kill Chain.** The Kill Chain fits these intrusions only partially: with valid credentials, weaponisation, delivery and exploitation collapse into a single login. It is used in this project only as a high-level summary (`03-analysis/kill-chain.md`).

---

## 7. Detection Opportunities (EEI 5)

| Technique | Log source | Public Sigma rule | Own rule |
|---|---|---|---|
| T1078 Valid Accounts (SSL VPN login) | SonicWall SSL VPN / firewall logs | **None found** | Detection logic below |
| T1219.002 Remote Desktop Software | Windows process creation | Yes (SigmaHQ AnyDesk rules) | — |
| T1490 Inhibit System Recovery | Windows process creation | Yes (SigmaHQ) | `shadow-copy-deletion.yml` |

**The initial access stage has no public detection coverage.** No public Sigma rule was found for suspicious SonicWall SSL VPN logins, and Sigma has no standard log source for SonicWall firewall logs. Organisations should build detections on their own logs, looking for:

- SSL VPN logins from hosting providers, VPS ranges or unusual countries;
- successful logins following multiple failed attempts;
- logins by local accounts that should use MFA, or outside business hours;
- logins from accounts unused for a long period, such as credentials carried over from migrations.

The rule `shadow-copy-deletion.yml` detects shadow copy deletion with vssadmin and converts cleanly to Splunk and to Microsoft Sentinel with Defender for Endpoint data. Full details are in `05-detection/coverage.md`.

---

## 8. Indicators of Compromise

The following indicators come from the CISA/FBI advisory (S01). They should be vetted before blocking; file hashes change easily between campaigns, so behavioural detection (Section 7) is more durable.

| Type | Value | Description |
|---|---|---|
| SHA-256 | `d2fd0654710c27dcf37b6c1437880020824e161dd0bf28e3a133ed777242a0ca` | Akira encryptor (w.exe) |
| SHA-256 | `dcfa2800754e5722acf94987bb03e814edcb9acebda37df6da1987bf48e5b05e` | Akira encryptor (Win.exe) |
| SHA-256 | `3298d203c2acb68c474e5fdad8379181890b4403d6491c523c13730129be3f75` | Akira_v2 (Linux/ESXi) |
| SHA-256 | `0ee1d284ed663073872012c7bde7fac5ca1121403f1a5d2d5411317df282796c` | Akira_v2 (Linux/ESXi) |
| Account name | `itadm` | Admin account created for persistence |
| File extension | `.akira`, `.powerranges`, `.akiranew`, `.aki` | Encrypted files |
| Ransom note | `akira_readme.txt`, `fn.txt` | Ransom note file names |

The IP addresses listed in the SonicWall advisory (S02) are not attributed to Akira and date from late 2024, so they are not included here.

---

## 9. Recommendations

**Immediate (devices and access)**
1. Upgrade affected SonicWall devices to the latest firmware; replace end-of-life devices, which will not be patched.
2. Reset all local SSL VPN passwords, including accounts migrated from Gen 6 to Gen 7 devices.
3. Enforce MFA for all SSL VPN users.
4. Restrict SSL VPN and firewall management access to trusted sources, or disable them from the internet where possible.
5. Enable account lockout after repeated failed logins.

**Detection and response**
6. Forward SSL VPN login logs to a SIEM and build detections using the logic in Section 7.
7. Alert on newly installed remote access tools, new privileged accounts (e.g. `itadm`) and shadow copy deletion.
8. Collect EDR or Sysmon process telemetry, not only native Windows auditing.

**Resilience**
9. Patch Veeam Backup & Replication servers (CVE-2023-27532, CVE-2024-40711), which Akira exploits after access.
10. Keep offline, immutable backups and test restoration regularly.

---

## 10. Intelligence Gaps and Limitations

- **Single-source link.** The link between Akira and CVE-2024-40766 relies on one source (S01).
- **Access method share unknown.** No source quantifies how often each access vector is used.
- **Recency.** The most recent reporting on this campaign dates from November 2025; Akira's activity in 2026 may have changed.
- **No Belgian data.** No source provides Belgian or EU-specific exploitation or victim data.
- **Open sources only.** Closed-community intelligence (national CERTs, sector ISACs) was not available. The public CIRCL feed provides limited coverage of this campaign (S05).
- **Scale uncertain.** SonicWall reported fewer than 40 confirmed incidents in the 2025 wave (S02); the true number may be higher.

---

## 11. Sources

| ID | Source | Rating |
|---|---|---|
| S01 | CISA/FBI et al., #StopRansomware: Akira Ransomware, AA24-109A (updated 13 Nov 2025) | B2 |
| S02 | SonicWall PSIRT, SNWLID-2024-0015 (updated 20 Nov 2024), and Gen 7 SSL VPN threat activity notice (Aug 2025) | B2 |
| S03 | CISA Known Exploited Vulnerabilities Catalog, CVE-2024-40766 | B1 |
| S04 | NIST National Vulnerability Database, CVE-2024-40766 | B1 |
| S05 | CIRCL OSINT feed via local MISP, event 1330 (reproduces S01) | B2 |
| S06 | FIRST EPSS API, CVE-2024-40766 (retrieved 26 Sep 2026) | B2 |