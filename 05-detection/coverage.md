# Detection Coverage

| Technique | Kill Chain phase | Log source | Public rule? | Own rule |
|-----------|------------------|------------|--------------|----------|
| T1078 Valid Accounts | Exploitation | VPN / firewall logs | | |
| T1219 Remote Access Software | Installation | Process creation | | |
| T1490 Inhibit System Recovery | Actions on Objectives | Process creation | Yes (SigmaHQ) | shadow-copy-deletion.yml |

## Conversion example - Sigconverter

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

**Attention here:** Conversion fails with the `azure_monitor` and `sentinel_asim` pipelines, because Windows Security Event 4688 does not record the original file name. Organisations relying only on native Windows auditing cannot detect a renamed vssadmin.exe with this rule; EDR or Sysmon telemetry is required.