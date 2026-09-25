# akira-sonicwall-cti
CTI assessment of Akira ransomware exploiting SonicWall SSL VPN

# Akira Ransomware & SonicWall SSL VPN: A CTI Assessment for Belgium

## Objective
(1 paragraph: stakeholder perspective, what the project answers)

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