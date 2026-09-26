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

## Key Findings

1. **Akira gains access to SonicWall devices through three vectors: exploitation of CVE-2024-40766, stolen or purchased VPN credentials, and brute force.** (S01, S02 — moderate confidence: the link between Akira and this CVE relies on a single source.)*

2. **CVE-2024-40766 is critical and actively exploited.** It is rated 9.3 by the vendor, has been listed in CISA KEV since 9 September 2024 with known ransomware use, and its EPSS score places it in the top 3% of all CVEs for likelihood of exploitation (0.18, retrieved 26 September 2026). *(S02, S03, FIRST EPSS — high confidence.)*

3. **Patching alone was not enough.** A new wave in 2025 compromised patched Gen 7 devices whose local SSL VPN passwords had been carried over from Gen 6 without being reset. End-of-life devices will receive no patch at all. Effective remediation requires patching, credential resets, MFA and restricted access. *(S02 — high confidence.)*

4. **Defenders have little time.** In some incidents, Akira exfiltrated data just over two hours after initial access, so detection must focus on the earliest stages of the intrusion. *(S01 — moderate confidence: based on a limited number of reported incidents.)*

5. **Detection depends on the data an organisation collects, not only on rules.** Shadow copy deletion (T1490) can be detected with a Sigma rule converted for Splunk and Microsoft Sentinel.

6. **The threat is relevant for Belgium, but Belgian-specific data is missing.** Akira's preferred sectors (critical manufacturing, healthcare, financial services, food and agriculture, education) overlap with many NIS2 entities in Belgium, but no source provides Belgian or EU-specific exploitation data. *(S01 — intelligence gap.)*

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

## License
Code (scripts, Sigma rules) is released under the MIT License.
Reports and documentation are released under CC BY 4.0.