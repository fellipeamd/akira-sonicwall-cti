import os
from datetime import date

import urllib3
from pymisp import PyMISP

from dotenv import load_dotenv
load_dotenv()

# Local test instance uses a self-signed certificate: hide the related warnings.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

misp = PyMISP(os.environ["MISP_URL"], os.environ["MISP_KEY"], ssl=False)

# Two Akira encryptor hashes from the CISA/FBI advisory (S01)
S01_HASHES = [
    "d2fd0654710c27dcf37b6c1437880020824e161dd0bf28e3a133ed777242a0ca",
    "dcfa2800754e5722acf94987bb03e814edcb9acebda37df6da1987bf48e5b05e",
]

searches = {
    "Events with 'akira' in the title": misp.search(eventinfo="%akira%", pythonify=True),
    "Events tagged with 'akira'": misp.search(tags=["%akira%"], pythonify=True),
    "Events containing CVE-2024-40766": misp.search(value="CVE-2024-40766", pythonify=True),
    "Events containing S01 hashes": misp.search(value=S01_HASHES, pythonify=True),
}

print(f"MISP lookup | {misp.misp_instance_version['version']} | {date.today()}\n")

for label, events in searches.items():
    print(f"{label}: {len(events)} event(s)")
    for e in events[:10]:
        print(f"  {e.id} | {e.date} | {getattr(getattr(e, 'Orgc', None), 'name', '?')} | {e.info}")
    print()