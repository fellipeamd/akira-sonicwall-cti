# Detection Coverage

This table maps key Akira techniques to the log sources and Sigma rules that can detect them, from initial access to impact.

| Technique | Kill Chain phase | Log source | Public rule? | Own rule |
|-----------|------------------|------------|--------------|----------|
| T1078 Valid Accounts | Exploitation | SonicWall SSL VPN / firewall logs | **No** (only an unrelated 2021 SonicWall exploit rule found) | — (see detection logic below) |
| T1219.002 Remote Desktop Software | Installation | Windows process creation | Yes (SigmaHQ: *Remote Access Tool - AnyDesk Execution*, *AnyDesk Silent Installation*) | — |
| T1490 Inhibit System Recovery | Actions on Objectives | Windows process creation | Yes (SigmaHQ: *<rule title + link>*) | `shadow-copy-deletion.yml` |

**Key takeaway:** public detection coverage is good for the later stages of the intrusion, but absent for the initial access stage, which is where defenders have the best chance to stop Akira.

## Coverage gap: SSL VPN access

No public Sigma rule was found for suspicious SonicWall SSL VPN logins, the initial access stage of Akira's intrusions. Sigma has no standard log source for SonicWall firewall logs, so detection must be built on each organisation's own logs. Suggested detection logic:

- SSL VPN logins from hosting providers, VPS ranges or unusual countries
- Successful logins following multiple failed attempts (brute force)
- Logins by local accounts that should use MFA, or outside business hours
- Logins from accounts not used for a long period (credentials carried over from migrations)

## Conversion example (sigconverter.io)

Rule `shadow-copy-deletion.yml` converted with sigconverter.io (sigma-cli).

**Splunk (SPL)** — target `splunk`:

```
Image="*\\vssadmin.exe" OR OriginalFileName="VSSADMIN.EXE" CommandLine="*delete*" CommandLine="*shadows*"
```

**Microsoft Sentinel (KQL)** — target `kusto`, pipeline `microsoft_xdr` (Defender for Endpoint data):

```
DeviceProcessEvents
| where (FolderPath endswith "\\vssadmin.exe" or ProcessVersionInfoOriginalFileName =~ "VSSADMIN.EXE") and (ProcessCommandLine contains "delete" and ProcessCommandLine contains "shadows")
```

**Note:** Conversion fails with the `azure_monitor` and `sentinel_asim` pipelines, because Windows Security Event 4688 does not record the original file name. Organisations relying only on native Windows auditing cannot detect a renamed vssadmin.exe with this rule; EDR or Sysmon telemetry is required.