# Policy Brief: Ransomware Entering Through Firewall VPNs

**TLP:CLEAR** · 27 September 2026 · Author: Fellipe Desinde

> *Portfolio assessment written from the perspective of a national cybersecurity authority. Not an official product of any organisation. Based on open sources only.*

---

## Bottom line

The Akira ransomware group breaks into organisations through the remote-access feature (SSL VPN) of SonicWall firewalls. **Organisations that installed the security update but did not reset their VPN passwords and turn on two-step login are likely still exposed.** Once inside, attackers can steal data within hours.

## Why it matters for Belgium

- **Ransomware remains one of the top cyber threats in the EU**, and Akira is one of the most active groups, having claimed about USD 244 million in ransom payments by September 2025.
- **Akira favours sectors covered by NIS2**, such as manufacturing, healthcare, finance, food and education, and mainly targets small and medium-sized organisations.
- **Firewalls and VPNs sit at the edge of every network.** They are exposed to the internet by design, which makes them a preferred way in for attackers.
- **The weakness is serious and actively used.** It is rated critical, is on the U.S. government's list of weaknesses already used in real attacks, including by ransomware, and is among the 3% of known weaknesses most likely to be exploited.

## What we assess

- Akira will **very likely** keep using firewall VPNs as a way in over the next 6–12 months.
- Organisations that only installed the update **likely** remain exposed: in 2025, updated devices were breached using passwords that had never been changed.
- Attackers **likely** move from entry to data theft in hours, not days, which leaves little time to react.
- There is a **roughly even chance** that Belgian organisations have been or will be targeted this way. No Belgian-specific data was found, so this judgement has low confidence.

## What decision-makers should ask for

**For organisations using SonicWall firewalls:**
1. Confirm that devices are updated, and replace old models that will never receive the fix.
2. Reset all VPN passwords, especially after any hardware replacement or migration.
3. Require two-step login (MFA) for everyone using the VPN.
4. Make sure VPN logins are monitored, since standard community detection rules do not cover this entry point.

**For a national authority:**
1. Remind NIS2 entities that updating is not enough: password resets and MFA are part of the fix.
2. Encourage organisations to share incident data, to close the Belgian evidence gap identified in this assessment.

## What we do not know

- How often attackers exploit the weakness directly versus simply logging in with stolen passwords.
- Whether Akira's methods have changed in 2026: the latest detailed public reporting dates from November 2025.
- How many Belgian organisations use affected devices or have been targeted.

---

*Sources: CISA/FBI Akira advisory (updated Nov 2025); SonicWall security advisory and 2025 notice; CISA Known Exploited Vulnerabilities Catalog; FIRST EPSS. Full analysis and references in the technical report.*