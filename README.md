# akira-sonicwall-cti
CTI assessment of Akira ransomware exploiting SonicWall SSL VPN

# Akira Ransomware & SonicWall SSL VPN: A CTI Assessment for Belgium

## Objective

This project has two goals: to learn, and to demonstrate that I can apply cyber threat intelligence methods in practice.

I built it as a hands-on way to learn the full intelligence cycle, working on a real and current threat rather than a theoretical exercise: Akira ransomware gaining initial access through SonicWall SSL VPN devices. 

At the same time, the project is meant to show the technical capabilities I can bring to a CTI role: working with public APIs in Python (NVD, FIRST EPSS, CISA KEV), writing and converting Sigma rules for different SIEMs, using MISP and PyMISP, and turning analysis into products for both technical and policy audiences.

I chose this case because it matters for defenders in Belgium. Ransomware remains one of the top threats in the EU, edge devices are a leading initial access vector, and many NIS2 entities rely on them. The assessment is written from the perspective of a national cybersecurity authority and uses only open sources and passive research.


## Methodology
Intelligence lifecycle: requirements → collection → analysis → dissemination.
Frameworks: MITRE ATT&CK, Cyber Kill Chain, Admiralty Code, estimative language.

## Key Findings
(the key judgements, short)

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
- MISP event with ATT&CK galaxies and PyMISP enrichment
- YARA rules for Akira artefacts

## License
Code (scripts, Sigma rules) is released under the MIT License.
Reports and documentation are released under CC BY 4.0.