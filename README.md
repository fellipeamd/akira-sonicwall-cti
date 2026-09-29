# Akira Ransomware & SonicWall SSL VPN: A CTI Assessment for Belgium
CTI project of Akira ransomware exploiting SonicWall SSL VPN

## Objective

This project has two goals: to learn, and to demonstrate that I can apply cyber threat intelligence methods in practice.

I built it as a hands-on way to learn the full intelligence cycle, working on a real and current threat rather than a theoretical exercise: Akira ransomware gaining initial access through SonicWall SSL VPN devices. 

At the same time, the project is meant to show the technical capabilities I can bring to a CTI role: working with public APIs in Python (NVD, FIRST EPSS, CISA KEV), writing and converting Sigma rules for different SIEMs, using MISP and PyMISP, and turning analysis into products for both technical and policy audiences.

I chose this case because it matters for defenders in Belgium. Ransomware remains one of the top threats in the EU, edge devices are a leading initial access vector, and many NIS2 entities rely on them. The assessment is written from the perspective of a national cybersecurity authority and uses only open sources and passive research.


## Methodology
Intelligence lifecycle: requirements → collection → analysis → dissemination.
Frameworks: MITRE ATT&CK, Cyber Kill Chain, Admiralty Code, estimative language.

## Bottom Line Up Front
[the 4–5 line BLUF]

**Key judgements:** five assessed judgements with probability and confidence
levels (ICD 203) are in [Key Judgements](03-analysis/key-judgements.md) and
the [Technical Report](06-reports/technical-report.md).

**MISP Dashboard**

## Why MISP?

MISP is the standard open-source platform for storing and sharing threat
intelligence in Europe, used by national CERTs and ISACs. I used it to check
whether open community feeds added independent evidence on Akira and
CVE-2024-40766, and to package this assessment's indicators as a MISP event

## Setup
- Local MISP instance, version 2.5.47, deployed with [Docker]
  on MacOS.
- Enabled and fetched the CIRCL OSINT feed.
  
  *Local MISP instance after importing the CIRCL OSINT feed
(1,679 events, 582,973 attributes), 27 September 2026.*
  <img width="2987" height="1590" alt="misp-dashboard" src="https://github.com/user-attachments/assets/bb68d39b-16f1-4444-ada1-07f4a22863a8" />

### What I did
1. Searched the feed for Akira and CVE-2024-40766.
2. Connected with PyMISP using an API key stored in a .env file.

### Findings
- The feed contains one Akira event (event 1330), which reproduces the
  April 2024 version of the CISA/FBI advisory (S01). Matching hashes are
  therefore circular reporting, not independent corroboration.

## Deliverables
- [Technical Report](06-reports/technical-report.md)
- [Policy Brief](06-reports/policy-brief.md)
- [Requirements & Collection Plan](01-requirements.md)
- [Source Log](02-source-log.md)
- [ATT&CK Layer](03-analysis/)
- [Sigma Rules](05-detection/sigma/)

## Rules of Engagement
Passive OSINT only. No interaction with threat actors, no active scanning.
All outputs TLP:CLEAR.

## Limitations

## Future Work
- Aggregate attack surface analysis of Belgian exposure (Shodan/Shadowserver)
- Sector impact analysis mapped to NIS2
- YARA rules for Akira artefacts
- Invest more into Events on MISP

## License
Code (scripts, Sigma rules) is released under the MIT License.
Reports and documentation are released under CC BY 4.0.
