#! /usr/bin/env python

#et log level to benefit from Scapy warnings
import logging
logging.getLogger("scapy").setLevel(1)

from scapy.all import *

# TODO: implement packets and functions like this -> mainly packets for now
# and the functions would maybe helper for internals or for external tools
#
# class Test(Packet):
#     name = "Test packet"
#     fields_desc = [ ShortField("test1", 1),
#                     ShortField("test2", 2) ]

# def make_test(x,y):
#     return Ether()/IP()/Test(test1=x,test2=y)

if __name__ == "__main__":
    interact(mydict=globals(), mybanner="Scapy SmithMeter protocol added to this session.")

