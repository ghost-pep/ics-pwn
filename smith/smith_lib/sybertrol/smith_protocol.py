#! /usr/bin/env python

# Set log level so when this is run interactively we get Scapy warnings
import logging
logging.getLogger("scapy").setLevel(1)

from scapy.all import *

#constants
FRAME_LEN=1
BYTECOUNT_LEN=2

class Smith(Packet):
    name = "Smith Ascii LRC Packet "
    fields_desc = [
            XByteField("frame", 2),
            ShortField("byteCount", None),
            ShortField("address", None),
            ByteField("dataType", None),
            ShortField("func", None),
            ShortField("sub", None),
            ShortField("off", None),
            ByteField("cmd", None),
            FieldListField("data", None, ByteField("", None)),
            XByteField("lrc", None)
            ]

    # override the last building of the packet
    def post_build(self, current_layer, payload):
        #calculate LRC using method specified in protocol docs
        if self.lrc is None:
            lrc = current_layer[1]
            for i in range(2, len(current_layer)):
                lrc ^= current_layer[i]
            lrc = bytes([lrc])
            current_layer = current_layer[:-1] + lrc

        #calculate byteCount
        if self.byteCount is None:
            count = len(current_layer) - FRAME_LEN - BYTECOUNT_LEN
            count = bytes([count])
            #update current_layer
            current_layer = current_layer[:FRAME_LEN] + count + current_layer[2:]
            
        return current_layer + payload


# library can be launched as a standalone script to interface with the interpreter
if __name__ == "__main__":
    interact(mydict=globals(), mybanner="Loaded SmithMeter Protocol Library.")
