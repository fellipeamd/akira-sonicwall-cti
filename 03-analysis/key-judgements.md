
*Assessment date: 27 September 2026. Horizon: next 6–12 months.*

**Probability** (ICD 203): almost no chance (1–5%) – very unlikely (5–20%) – unlikely (20–45%) – roughly even chance (45–55%) – likely (55–80%) – very likely (80–95%) – almost certain (95–99%)
**Confidence:** low / moderate / high

1. We assess it is **likely** (**moderate** confidence) that Akira's primary initial access vector against SonicWall devices is access to internet-exposed SSL VPN portals without MFA, either by exploiting CVE-2024-40766 or by using valid, stolen or brute-forced credentials. (Sources: S01, S02, S03)

2. We assess it is **likely** (**moderate** confidence) that the window between initial access and data exfiltration is measured in hours rather than days in at least some intrusions, leaving defenders limited time to respond before encryption. (Sources: S01)

3. We assess it is **likely** (**moderate** confidence) that organisations which patched CVE-2024-40766 without resetting local SSL VPN credentials and enforcing MFA remain exposed, as shown by the 2025 wave against patched Gen 7 devices. (Sources: S02)

4. We assess it is **very likely** (**moderate** confidence) that Akira will continue to use internet-exposed SSL VPN appliances, including SonicWall, as an initial access vector over the next 6–12 months. (Sources: S01, S02, S03, FIRST EPSS)

5. We assess there is a **roughly even chance** (**low** confidence) that Belgian organisations in Akira's preferred sectors have been or will be targeted through this vector; Akira's preferred sectors overlap with many NIS2 entities, but no Belgian-specific data was found. (Sources: S01, S05)

**Limitations:** The most recent sources on this campaign date from November 2025, so these judgements may not reflect changes in Akira's activity in 2026. All sources are open-source; closed-community intelligence was not available.