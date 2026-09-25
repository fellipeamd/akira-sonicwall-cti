# Intelligence Requirements

## Stakeholder
A national cybersecurity authority, i.e. in here CCB responsible for protecting
government, critical infrastructure and vital sectors in Belgium.

## Why this requirement
- Ransomware is one of the top threats in the ENISA Threat Landscape -and in the world. 
- Edge devices (VPNs, firewalls) are a leading initial access vector.
- NIS2 entities in Belgium rely on such devices.
- Supports decisions on warnings and recommendations to Belgian operators.

## PIR
How does Akira gain initial access through SonicWall SSL VPN, and which
detections allow defenders to stop the intrusion before encryption?
Scope: April 2025 – September 2026, EU with focus on Belgium.

## EEIs
1. Which initial access vectors does Akira use against SonicWall devices?
2. How severe and how actively exploited is CVE-2024-40766?
3. Which techniques does Akira use between initial access and encryption?
4. How much time typically passes between access and encryption?
5. Which log sources and detection rules can catch these techniques early?

## Collection Plan
| EEI | Source | Method | Priority | Status |
|-----|--------|--------|----------|--------|
| 1 | CISA/FBI Akira advisory; SonicWall advisory; vendor IR reports | Read & extract | High | To do |
| 2 | NVD, FIRST EPSS, CISA KEV | Python script | High | To do |
| 3 | CISA advisory; MITRE ATT&CK; vendor reports | ATT&CK mapping | High | To do |
| 4 | Vendor IR reports | Extract & compare | Medium | To do |
| 5 | MITRE ATT&CK; SigmaHQ; Elastic rules | Coverage review | High | To do |

## Intelligence Gaps