''' for python 3 reqires for of textFSM avialable at https://github.com/jonathanslenders/textfsm


 Copyright 2016 Hewlett Packard Enterprise Development LP.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.'''
import jtextfsm as textfsm
import json
import os


displayinterfaces = """Ten-GigabitEthernet1/0/38
Current state: DOWN
Line protocol state: DOWN
IP packet frame type: Ethernet II, hardware address: d07e-28ec-aa96
Description: Ten-GigabitEthernet1/0/38 Interface
Bandwidth: 10000000 kbps
Loopback is not set
Media type is twisted pair
Port hardware type is 10G_BASE_T
Unknown-speed mode, unknown-duplex mode
Link speed type is autonegotiation, link duplex type is autonegotiation
Flow-control is not enabled
Maximum frame length: 10000
Allow jumbo frames to pass
Broadcast max-ratio: 100%
Multicast max-ratio: 100%
Unicast max-ratio: 100%
PVID: 1
MDI type: Automdix
Port link-type: Access
 Tagged VLANs:   None
 Untagged VLANs: 1
Port priority: 0
Last clearing of counters: Never
 Peak input rate: 0 bytes/sec, at 2011-01-01 00:01:20
 Peak output rate: 0 bytes/sec, at 2011-01-01 00:01:20
 Last 300 second input: 0 packets/sec 0 bytes/sec -%
 Last 300 second output: 0 packets/sec 0 bytes/sec -%
 Input (total):  0 packets, 0 bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Input (normal):  0 packets, - bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Input:  0 input errors, 0 runts, 0 giants, 0 throttles
	 0 CRC, 0 frame, - overruns, 0 aborts
	 - ignored, - parity errors
 Output (total): 0 packets, 0 bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Output (normal): 0 packets, - bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Output: 0 output errors, - underruns, - buffer failures
	 0 aborts, 0 deferred, 0 collisions, 0 late collisions
         0 lost carrier, - no carrier

Ten-GigabitEthernet1/0/39
Current state: DOWN
Line protocol state: DOWN
IP packet frame type: Ethernet II, hardware address: d07e-28ec-aa97
Description: Ten-GigabitEthernet1/0/39 Interface
Bandwidth: 10000000 kbps
Loopback is not set
Media type is twisted pair
Port hardware type is 10G_BASE_T
Unknown-speed mode, unknown-duplex mode
Link speed type is autonegotiation, link duplex type is autonegotiation
Flow-control is not enabled
Maximum frame length: 10000
Allow jumbo frames to pass
Broadcast max-ratio: 100%
Multicast max-ratio: 100%
Unicast max-ratio: 100%
PVID: 1
MDI type: Automdix
Port link-type: Access
 Tagged VLANs:   None
 Untagged VLANs: 1
Port priority: 0
Last clearing of counters: Never
 Peak input rate: 0 bytes/sec, at 2011-01-01 00:01:20
 Peak output rate: 0 bytes/sec, at 2011-01-01 00:01:20
 Last 300 second input: 0 packets/sec 0 bytes/sec -%
 Last 300 second output: 0 packets/sec 0 bytes/sec -%
 Input (total):  0 packets, 0 bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Input (normal):  0 packets, - bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Input:  0 input errors, 0 runts, 0 giants, 0 throttles
	 0 CRC, 0 frame, - overruns, 0 aborts
	 - ignored, - parity errors
 Output (total): 0 packets, 0 bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Output (normal): 0 packets, - bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Output: 0 output errors, - underruns, - buffer failures
	 0 aborts, 0 deferred, 0 collisions, 0 late collisions
	 0 lost carrier, - no carrier

Ten-GigabitEthernet1/0/40
Current state: DOWN
Line protocol state: DOWN
IP packet frame type: Ethernet II, hardware address: d07e-28ec-aa98
Description: Ten-GigabitEthernet1/0/40 Interface
Bandwidth: 10000000 kbps
Loopback is not set
Media type is twisted pair
Port hardware type is 10G_BASE_T
Unknown-speed mode, unknown-duplex mode
Link speed type is autonegotiation, link duplex type is autonegotiation
Flow-control is not enabled
Maximum frame length: 10000
Allow jumbo frames to pass
Broadcast max-ratio: 100%
Multicast max-ratio: 100%
Unicast max-ratio: 100%
PVID: 1
MDI type: Automdix
Port link-type: Access
 Tagged VLANs:   None
 Untagged VLANs: 1
Port priority: 0
Last clearing of counters: Never
 Peak input rate: 0 bytes/sec, at 2011-01-01 00:01:20
 Peak output rate: 0 bytes/sec, at 2011-01-01 00:01:20
 Last 300 second input: 0 packets/sec 0 bytes/sec -%
 Last 300 second output: 0 packets/sec 0 bytes/sec -%
 Input (total):  0 packets, 0 bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Input (normal):  0 packets, - bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Input:  0 input errors, 0 runts, 0 giants, 0 throttles
	 0 CRC, 0 frame, - overruns, 0 aborts
	 - ignored, - parity errors
 Output (total): 0 packets, 0 bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Output (normal): 0 packets, - bytes
	 0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Output: 0 output errors, - underruns, - buffer failures
	 0 aborts, 0 deferred, 0 collisions, 0 late collisions
	 0 lost carrier, - no carrier
"""

template = open("./templates/displayinterfaces.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(displayinterfaces)

print (len(fsm_results))

for i in fsm_results:
    print (i)