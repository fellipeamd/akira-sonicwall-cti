# Detection Coverage

| Technique | Kill Chain phase | Log source | Public rule? | Own rule |
|-----------|------------------|------------|--------------|----------|
| T1078 Valid Accounts | Exploitation | VPN / firewall logs | | |
| T1219 Remote Access Software | Installation | Process creation | | |
| T1490 Inhibit System Recovery | Actions on Objectives | Process creation | Yes (SigmaHQ) | shadow-copy-deletion.yml |

## Conversion example
(paste sigma-cli output here)