# Link Failure Detection and Recovery using SDN

## Problem Statement
Detect link failures and dynamically update routing to restore connectivity using Software Defined Networking (SDN).

---

## Project Overview
This project demonstrates how SDN enables adaptive networking by separating the control plane from the data plane. A centralized controller (POX) monitors the network topology and dynamically updates routing when a link failure occurs.

---

## Technologies Used
- Mininet (Network Emulator)  
- POX Controller  
- OpenFlow Protocol  
- Open vSwitch (OVS)  

---

## Network Topology
- Hosts: h1, h2  
- Switches: s1, s2, s3  
- One primary path and one backup path 
``` 
h1 — s1 — s2 — h2
      \     /
       \   /
         s3
```
---
## Key Features
- Link failure detection  
- Dynamic flow rule updates  
- Alternate path routing  
- Centralized control  

---

## Expected Output
- Connectivity works initially  
- Packet loss occurs after link failure  
- Connectivity is restored after recovery  

---

## Explanation
Initially, traffic flows through the primary path (s1 → s2).  
When the link fails, existing flow rules become invalid, causing packet loss.  
After clearing flow tables, the controller recomputes the path and installs new flow rules through the alternate path (s1 → s3 → s2), restoring connectivity.  

---

# Demonstration Steps

```bash
# Step 1: Start Controller
cd pox
./pox.py openflow.discovery openflow.spanning_tree forwarding.l2_learning forwarding.link_logger

# Step 2: Start Mininet
sudo mn --custom topo.py --topo mytopo --controller=remote

# Step 3: Verify initial connectivity
pingall

# Step 4: Simulate link failure (primary path)
link s1 s2 down

# Step 5: Observe network impact
pingall

# Step 6: Trigger recovery
dpctl del-flows
pingall

# Step 7: Restore link
link s1 s2 up

# Step 8: Verify connectivity again
pingall

```
## Conclusion
This project shows how SDN enables resilient networking by dynamically responding to topology changes and maintaining connectivity through intelligent routing.
