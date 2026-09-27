import os, urllib3
from dotenv import load_dotenv
from pymisp import PyMISP
load_dotenv(); urllib3.disable_warnings()
misp = PyMISP(os.environ["MISP_URL"], os.environ["MISP_KEY"], ssl=False)
print("Total events:", len(misp.search(controller="events", metadata=True)))
for term in ["%akira%", "%sonicwall%", "%40766%"]:
    events = misp.search(searchall=term, metadata=True, pythonify=True)
    print(f"\n{term} -> {len(events)} event(s)")
    for e in events:
        print(f"  {e.id} | {e.date} | {e.info}")
   