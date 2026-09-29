# Akira Ransomware: How It Gets In Through SonicWall SSL VPN

**Technical Report** · TLP:CLEAR · 27 September 2026 · Fellipe Desinde

**Audience:** SOC analysts, network defenders, incident responders
**Scope:** August 2024 – present, EU with a focus on Belgium

> This is a portfolio project, written as if I were an analyst at a national cybersecurity authority. It is not an official product of any organisation. I used only public sources and passive research. Source IDs (S01–S06) are listed in [`02-source-log.md`](../02-source-log.md).

---

## 1. Summary

Akira gets into networks through SonicWall SSL VPN portals that are exposed to the internet. It does this in two ways: by exploiting CVE-2024-40766, or by logging in with valid passwords that were stolen, bought or guessed. In both cases, the main weakness is a VPN without multi-factor authentication (MFA).

**Installing the patch is not enough.** In 2025, patched SonicWall Gen 7 devices were still hacked, because their VPN passwords had been copied over from older Gen 6 devices and never changed (S02). Once inside, Akira can steal data within a few hours (S01).

**What to do:** patch or replace old devices, reset all VPN passwords, turn on MFA, limit who can reach the VPN, and watch VPN logins. I could not find any public detection rule for this first step, so organisations need to build their own.

---

## 2. The question I wanted to answer

**Main question:** How does Akira get in through SonicWall SSL VPN, and what should Belgian defenders focus on to detect and stop it before files are encrypted?

I split it into five smaller questions:

| # | Question | Section |
|---|---|---|
| 1 | How does Akira get into SonicWall devices? | 4 |
| 2 | How serious is CVE-2024-40766, and is it really being exploited? | 5 |
| 3 | What does Akira do between getting in and encrypting? | 6 |
| 4 | How much time do defenders have? | 6 |
| 5 | Which logs and rules can catch it early? | 7 |

---

## 3. Key Judgements

*I use the ICD 203 scale for probability (e.g. likely = 55–80%, very likely = 80–95%) and rate my confidence as low, moderate or high, depending on how strong my sources are.*

1. We assess it is **likely** (**moderate** confidence) that Akira's primary initial access vector against SonicWall devices is access to internet-exposed SSL VPN portals without MFA, either by exploiting CVE-2024-40766 or by using valid, stolen or brute-forced credentials. (S01, S02, S03)
2. We assess it is **likely** (**moderate** confidence) that the window between initial access and data exfiltration is measured in hours rather than days in at least some intrusions, leaving defenders limited time to respond before encryption. (S01)
3. We assess it is **likely** (**moderate** confidence) that organisations which patched CVE-2024-40766 without resetting local SSL VPN credentials and enforcing MFA remain exposed, as shown by the 2025 wave against patched Gen 7 devices. (S02)
4. We assess it is **very likely** (**moderate** confidence) that Akira will continue to use internet-exposed SSL VPN appliances, including SonicWall, as an initial access vector over the next 6–12 months. (S01, S02, S03, S06)
5. We assess there is a **roughly even chance** (**low** confidence) that Belgian organisations in Akira's preferred sectors have been or will be targeted through this vector; Akira's preferred sectors overlap with many NIS2 entities, but no Belgian-specific data was found. (S01, S05)

---

## 4. How Akira gets in (Question 1)

My sources describe three ways in:

| How | ATT&CK | What the sources say | Rating |
|---|---|---|---|
| Exploiting CVE-2024-40766 | T1190 | CISA/FBI say Akira *likely* used this vulnerability (S01). SonicWall confirms it affects the SSL VPN (S02). | B3 |
| Stolen or bought VPN passwords | T1078, T1133 | Akira logs in with compromised VPN accounts, sometimes bought from access brokers (S01). | B2 |
| Guessing passwords | T1110, T1110.003 | Brute force and password spraying against VPN logins (S01). SonicWall recommends account lockout (S02). | B2 |

*The "Rating" column rates each piece of information, not the whole source. The CVE link gets B3 because CISA/FBI only say "likely".*

**What they have in common:** both main sources point to the same weakness, a VPN without MFA (S01, S02).

**How I read it:** these three ways are connected. SonicWall told customers to reset their VPN passwords, not only to patch (S02). The 2025 wave showed why: passwords that stayed the same after patching were used to break into Gen 7 devices (S02). So an attacker can steal passwords through the vulnerability and still use them long after the patch is installed.

**Confidence: moderate.** Only one source (S01) links Akira to this CVE, and it uses careful wording.

---

## 5. The vulnerability: CVE-2024-40766 (Question 2)

I collected these numbers partly with a small Python script (`04-vulnerability/prioritise.py`) that queries the EPSS API and the CISA KEV list.

| What | Value | Source | Checked on |
|---|---|---|---|
| CVSS v3 (SonicWall) | 9.3 Critical | S02 | — |
| CVSS v3 (NVD) | 9.8 Critical | S04 | 28 Sep 2026 |
| EPSS | 0.1838 (97th percentile) | S06 | 26 Sep 2026 |
| CISA KEV | Yes, since 9 Sep 2024, known ransomware use | S03 | 26 Sep 2026 |

**What these mean in simple terms:**
- **CVSS** says how bad the vulnerability is in theory. Both scores are critical; SonicWall and NVD just score it a bit differently.
- **EPSS** estimates the chance it gets exploited in the next 30 days. 18% sounds low, but it is higher than 97% of all known vulnerabilities.
- **KEV** means CISA has confirmed it is being exploited in real attacks, including by ransomware.

**Affected devices (S02):** SonicWall Gen 5 and Gen 6 firewalls, and Gen 7 devices on SonicOS 7.0.1-5035 or older. Old end-of-life models (NSA 2600, Gen 5 except SOHO) will never get a fix.

**Timeline**

| Date | What happened | Source |
|---|---|---|
| 22 Aug 2024 | SonicWall publishes the vulnerability | S02 |
| 6 Sep 2024 | SSL VPN added as affected; possible exploitation mentioned | S02 |
| 9 Sep 2024 | Added to CISA KEV, with known ransomware use | S03 |
| Jul–Aug 2025 | New attacks on Gen 7 devices; SonicWall links them to this CVE and old passwords, not a new zero-day | S02 |
| 13 Nov 2025 | CISA/FBI update links Akira's initial access to this CVE | S01 |

**Why this should be a top priority:** it is confirmed as exploited (S03), linked to Akira (S01), still in the top 3% for EPSS almost two years later (S06), and it sits on a device that faces the internet by design. Most importantly, patching alone does not fix it: passwords must be reset too, and old devices will stay vulnerable forever (S02).

---

## 6. What Akira does once inside (Questions 3 and 4)

After getting in, Akira mostly uses normal admin tools, which makes it harder to spot (S01). I mapped what CISA/FBI describe to MITRE ATT&CK:

| Stage | Technique | What Akira does (S01) |
|---|---|---|
| Initial Access | T1133, T1078, T1190 | Logs into the SSL VPN with stolen passwords or exploits the CVE |
| Credential Access | T1110 | Brute force and password spraying on the VPN |
| Persistence | T1136 | Creates new admin accounts, e.g. `itadm` |
| Credential Access | T1003.001, T1003.003 | Mimikatz and LaZagne; dumps LSASS; steals NTDS.dit by copying a domain controller's virtual disk |
| Discovery | T1018, T1482, T1046 | `nltest`, `net` commands, Advanced IP Scanner, SoftPerfect NetScan |
| Defense Evasion | T1562.001 | Turns off or removes antivirus/EDR, including with vulnerable drivers (BYOVD) |
| Privilege Escalation | T1068 | Exploits unpatched Veeam Backup & Replication (CVE-2023-27532, CVE-2024-40711) |
| Lateral Movement | T1021.001, T1021.004 | RDP and SSH |
| Command and Control | T1219, T1572 | AnyDesk, LogMeIn; tunnels through Ngrok and Cloudflare Tunnel; SystemBC; Cobalt Strike |
| Exfiltration | T1567.002, T1048 | RClone to cloud storage (e.g. MEGA), WinSCP, FileZilla |
| Impact | T1490, T1486 | Deletes shadow copies; encrypts Windows systems and hypervisors (VMware ESXi, Hyper-V, Nutanix AHV) |

**How fast (Question 4):** in some cases, Akira stole data just over two hours after getting in (S01). I found no source that says how long it *usually* takes until encryption. Either way, defenders need to catch it at the very start.

**A note on the Cyber Kill Chain:** I also tried the Kill Chain ([`03-analysis/kill-chain.md`](../03-analysis/kill-chain.md)), but it only partly fits. When the attacker just logs in with a valid password, "weaponisation", "delivery" and "exploitation" all happen in one step. So I only use it as a high-level summary.

---

## 7. How to detect it (Question 5)

| Technique | Log source | Public Sigma rule? | My rule |
|---|---|---|---|
| T1078 VPN login with valid account | SonicWall SSL VPN / firewall logs | **None found** | Ideas below |
| T1219.002 Remote access tools | Windows process creation | Yes (SigmaHQ AnyDesk rules) | — |
| T1490 Shadow copy deletion | Windows process creation | Yes (SigmaHQ) | `shadow-copy-deletion.yml` |

**The biggest gap is at the start.** I found no public Sigma rule for suspicious SonicWall VPN logins, and Sigma has no standard log source for SonicWall. So organisations have to build this on their own logs. Things worth alerting on:

- VPN logins from hosting providers, VPS ranges or unusual countries;
- a successful login right after many failed ones;
- logins by accounts that should have MFA, or outside business hours;
- logins from accounts that have not been used for a long time (for example, old accounts carried over in a migration).

**Later steps are easier to catch.** I wrote a Sigma rule for shadow copy deletion with vssadmin (`shadow-copy-deletion.yml`) and converted it for Splunk and Microsoft Sentinel. One thing I learned while converting it: it only works well with EDR or Sysmon data, because native Windows event 4688 does not record the original file name. Details are in [`05-detection/coverage.md`](../05-detection/coverage.md).

---

## 8. Indicators of Compromise

These come from the CISA/FBI advisory (S01). Check them before blocking. Hashes change easily between campaigns, so the behaviour-based detection in Section 7 will last longer.

| Type | Value | What it is |
|---|---|---|
| SHA-256 | `d2fd0654710c27dcf37b6c1437880020824e161dd0bf28e3a133ed777242a0ca` | Akira encryptor (w.exe) |
| SHA-256 | `dcfa2800754e5722acf94987bb03e814edcb9acebda37df6da1987bf48e5b05e` | Akira encryptor (Win.exe) |
| SHA-256 | `3298d203c2acb68c474e5fdad8379181890b4403d6491c523c13730129be3f75` | Akira_v2 (Linux/ESXi) |
| SHA-256 | `0ee1d284ed663073872012c7bde7fac5ca1121403f1a5d2d5411317df282796c` | Akira_v2 (Linux/ESXi) |
| Account name | `itadm` | Admin account created to stay in the network |
| File extension | `.akira`, `.powerranges`, `.akiranew`, `.aki` | Encrypted files |
| Ransom note | `akira_readme.txt`, `fn.txt` | Ransom note file names |

I left out the IP addresses from the SonicWall advisory (S02), because they are not linked to Akira and are from late 2024.

**Checking MISP:** I set up a local MISP instance and loaded the public CIRCL OSINT feed (S05). It has only one Akira event, and it is a copy of the April 2024 version of the CISA/FBI advisory (S01), never updated since. So its matching hashes do not count as extra confirmation. The feed has no event about CVE-2024-40766.

---

## 9. Recommendations

**Right away (devices and access)**
1. Update affected SonicWall devices; replace end-of-life models, which will never be patched.
2. Reset all local SSL VPN passwords, including accounts moved from Gen 6 to Gen 7.
3. Turn on MFA for all VPN users.
4. Only allow VPN and management access from trusted sources, or close it to the internet where possible.
5. Lock accounts after repeated failed logins.

**Detection and response**
6. Send VPN login logs to a SIEM and alert on the patterns in Section 7.
7. Alert on new remote access tools, new admin accounts (e.g. `itadm`) and shadow copy deletion.
8. Collect EDR or Sysmon data, not only native Windows logs.

**Resilience**
9. Patch Veeam Backup & Replication (CVE-2023-27532, CVE-2024-40711), which Akira uses after getting in.
10. Keep offline backups that cannot be changed, and test restoring them regularly.

---

## 10. What I don't know

- **One source for the CVE link.** Only S01 links Akira to CVE-2024-40766.
- **No numbers on how often each method is used.** I don't know whether most attacks use the CVE or stolen passwords.
- **Old information.** The newest reporting is from November 2025; Akira may have changed since.
- **No Belgian data.** No public source had Belgian or EU-specific cases.
- **Only public sources.** I had no access to closed sharing groups (national CERTs, sector ISACs). The public CIRCL feed covers this campaign very little (S05).
- **Real scale unclear.** SonicWall reported fewer than 40 confirmed incidents in the 2025 wave (S02); the real number is probably higher.

---

## 11. Sources

| ID | Source | Rating |
|---|---|---|
| S01 | CISA/FBI et al., #StopRansomware: Akira Ransomware, AA24-109A (updated 13 Nov 2025) | B2 |
| S02 | SonicWall PSIRT, SNWLID-2024-0015 (updated 20 Nov 2024), and Gen 7 SSL VPN threat activity notice (Aug 2025) | B2 |
| S03 | CISA Known Exploited Vulnerabilities Catalog, CVE-2024-40766 | B1 |
| S04 | NIST National Vulnerability Database, CVE-2024-40766 | B1 |
| S05 | CIRCL OSINT feed via local MISP, event 1330 (copy of S01) | B2 |
| S06 | FIRST EPSS API, CVE-2024-40766 (checked 26 Sep 2026) | B2 |

Full details and rating reasons: [`02-source-log.md`](../02-source-log.md).