# FattreewithPABO
Evaluate PABO in a fattree topology

## This is a part of the source code, the other part is in https://github.com/Xiang-Shi/inet.git:

## 1. The whole project includes two repositories:
### (1) Inet: the core

The newly modified version of Inet, including link layer PacketBounce as well as transportlayer TCP support.

In the transportlayer, we also implemented measurement methods on packet out-of-order level of TCP -- Reorder Density (RD) and Reorder buffer-occupancy (RBD)

 
### (2) "FattreewithPABO" repository: the network settings

A fattree network topology which allows evaluating the performance of PABO together with TCP.

## 2. How to set up simulation in OMNet++ ?
###  (1) Import "Inet" and "FattreewithPABO"

###  (2) Parameter setting

   i) alter basic network settings in "FattreewithPABO/simulations/*.ini" and specify it when run
  
   ii) change the parameter of probability function P at the beginning of "inet/src/inet/linklayer/ethernet/switch/MACRelayUnit.cc"
   


### 3. Then build two projects, and choose to run projects directly or to run python scripts in "FattreewithPABO/simulations/results/"



