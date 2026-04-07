from pox.core import core
import pox.openflow.discovery as discovery

log = core.getLogger()

def _handle_LinkEvent(event):
    if event.removed:
        print("\n[ALERT] LINK FAILURE DETECTED")
    else:
        print("\n[INFO] LINK RESTORED")

def launch():
    core.openflow_discovery.addListenerByName("LinkEvent", _handle_LinkEvent)