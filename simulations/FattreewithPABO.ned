//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

package fattreewithpabo.simulations;

import inet.networklayer.configurator.ipv4.IPv4NetworkConfigurator;
import inet.node.ethernet.Eth1G;
import inet.node.inet.StandardHost;
import inet.linklayer.ethernet.switch.FattreeSwitch;
//import inet.node.ethernet.EtherSwitch;

//
// TODO auto-generated type
//
network FattreewithPABO
{
    @display("bgb=924,732");
    submodules:
        configurator: IPv4NetworkConfigurator {
            @display("p=107,52");
        }
        coreSwitch1: FattreeSwitch {
            @display("p=276,124");
        }

        coreSwitch2: FattreeSwitch {
            @display("p=391,124");
        }
        coreSwitch3: FattreeSwitch {
            @display("p=509,124");
        }
        coreSwitch4: FattreeSwitch {
            @display("p=628,124");
        }
        podSwitch3: FattreeSwitch {
            @display("p=56,252");
        }
        podSwitch4: FattreeSwitch {
            @display("p=147,252");
        }
        podSwitch1: FattreeSwitch {
            @display("p=56,349");
        }
        podSwitch2: FattreeSwitch {
            @display("p=153,349");
        }
        podSwitch7: FattreeSwitch {
            @display("p=288,258");
        }
        podSwitch8: FattreeSwitch {
            @display("p=391,258");
        }
        podSwitch5: FattreeSwitch {
            @display("p=288,349");
        }
        podSwitch6: FattreeSwitch {
            @display("p=391,349");
        }
        podSwitch11: FattreeSwitch {
            @display("p=529,258");
        }
        podSwitch12: FattreeSwitch {
            @display("p=628,258");
        }
        podSwitch9: FattreeSwitch {
            @display("p=529,349");
        }
        podSwitch10: FattreeSwitch {
            @display("p=628,349");
        }
        podSwitch15: FattreeSwitch {
            @display("p=753,258");
        }
        podSwitch16: FattreeSwitch {
            @display("p=840,252");
        }
        podSwitch13: FattreeSwitch {
            @display("p=753,349");
        }
        podSwitch14: FattreeSwitch {
            @display("p=840,349");
        }

        host1: StandardHost {
            @display("p=29,453");
        }
        host2: StandardHost {
            @display("p=76,453");
        }
        host3: StandardHost {
            @display("p=138,453");
        }
        host4: StandardHost {
            @display("p=186,453");
        }
        host5: StandardHost {
            @display("p=263,453");
        }
        host6: StandardHost {
            @display("p=315,453");
        }
        host7: StandardHost {
            @display("p=376,453");
        }
        host8: StandardHost {
            @display("p=422,453");
        }
        host9: StandardHost {
            @display("p=499,453");
        }
        host10: StandardHost {
            @display("p=548,453");
        }
        host11: StandardHost {
            @display("p=611,453");
        }
        host12: StandardHost {
            @display("p=657,453");
        }
        host13: StandardHost {
            @display("p=734,453");
        }
        host14: StandardHost {
            @display("p=782,453");
        }
        host15: StandardHost {
            @display("p=840,453");
        }
        host16: StandardHost {
            @display("p=889,453");
        }

    connections:


        podSwitch1.ethg++ <--> Eth1G <--> host1.ethg++;
        podSwitch1.ethg++ <--> Eth1G <--> host2.ethg++;
        podSwitch2.ethg++ <--> Eth1G <--> host3.ethg++;
        podSwitch2.ethg++ <--> Eth1G <--> host4.ethg++;
        podSwitch5.ethg++ <--> Eth1G <--> host5.ethg++;
        podSwitch5.ethg++ <--> Eth1G <--> host6.ethg++;
        podSwitch6.ethg++ <--> Eth1G <--> host7.ethg++;
        podSwitch6.ethg++ <--> Eth1G <--> host8.ethg++;
        podSwitch9.ethg++ <--> Eth1G <--> host9.ethg++;
        podSwitch9.ethg++ <--> Eth1G <--> host10.ethg++;
        podSwitch10.ethg++ <--> Eth1G <--> host11.ethg++;
        podSwitch10.ethg++ <--> Eth1G <--> host12.ethg++;
        podSwitch13.ethg++ <--> Eth1G <--> host13.ethg++;
        podSwitch13.ethg++ <--> Eth1G <--> host14.ethg++;
        podSwitch14.ethg++ <--> Eth1G <--> host15.ethg++;
        podSwitch14.ethg++ <--> Eth1G <--> host16.ethg++;

        podSwitch3.ethg++ <--> Eth1G <--> podSwitch1.ethg++;
        podSwitch3.ethg++ <--> Eth1G <--> podSwitch2.ethg++;
        podSwitch4.ethg++ <--> Eth1G <--> podSwitch1.ethg++;
        podSwitch4.ethg++ <--> Eth1G <--> podSwitch2.ethg++;
        podSwitch7.ethg++ <--> Eth1G <--> podSwitch5.ethg++;
        podSwitch7.ethg++ <--> Eth1G <--> podSwitch6.ethg++;
        podSwitch8.ethg++ <--> Eth1G <--> podSwitch5.ethg++;
        podSwitch8.ethg++ <--> Eth1G <--> podSwitch6.ethg++;
        podSwitch11.ethg++ <--> Eth1G <--> podSwitch9.ethg++;
        podSwitch11.ethg++ <--> Eth1G <--> podSwitch10.ethg++;
        podSwitch12.ethg++ <--> Eth1G <--> podSwitch9.ethg++;
        podSwitch12.ethg++ <--> Eth1G <--> podSwitch10.ethg++;
        podSwitch15.ethg++ <--> Eth1G <--> podSwitch13.ethg++;
        podSwitch15.ethg++ <--> Eth1G <--> podSwitch14.ethg++;
        podSwitch16.ethg++ <--> Eth1G <--> podSwitch13.ethg++;
        podSwitch16.ethg++ <--> Eth1G <--> podSwitch14.ethg++;



        coreSwitch1.ethg++ <--> Eth1G <--> podSwitch3.ethg++;
        coreSwitch1.ethg++ <--> Eth1G <--> podSwitch7.ethg++;
        coreSwitch1.ethg++ <--> Eth1G <--> podSwitch11.ethg++;
        coreSwitch1.ethg++ <--> Eth1G <--> podSwitch15.ethg++;

        coreSwitch2.ethg++ <--> Eth1G <--> podSwitch3.ethg++;
        coreSwitch2.ethg++ <--> Eth1G <--> podSwitch7.ethg++;
        coreSwitch2.ethg++ <--> Eth1G <--> podSwitch11.ethg++;
        coreSwitch2.ethg++ <--> Eth1G <--> podSwitch15.ethg++;

        coreSwitch3.ethg++ <--> Eth1G <--> podSwitch4.ethg++;
        coreSwitch3.ethg++ <--> Eth1G <--> podSwitch8.ethg++;
        coreSwitch3.ethg++ <--> Eth1G <--> podSwitch12.ethg++;
        coreSwitch3.ethg++ <--> Eth1G <--> podSwitch16.ethg++;

        coreSwitch4.ethg++ <--> Eth1G <--> podSwitch4.ethg++;
        coreSwitch4.ethg++ <--> Eth1G <--> podSwitch8.ethg++;
        coreSwitch4.ethg++ <--> Eth1G <--> podSwitch12.ethg++;
        coreSwitch4.ethg++ <--> Eth1G <--> podSwitch16.ethg++;




}
