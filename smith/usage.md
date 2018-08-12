# SmithMeter Protocol
The SmithMeter protocol is used to communicate with FMCTechnologies devices. These are usually used for control of
valves, data collection, and monitoring of a given product (Ex. Oil). The protocol itself is simple and is sent in
plaintext. It takes on three  different forms: ASCII LRC, ASCII CR, and binary LRC. These different forms specify error checking mechanisms and whether or not the data being transfered should be interpreted as ASCII or as the raw binary.

Ics-pwn chose to implement the SmithProtocol at three different layers. The toolset layer provides ready to use tools
that abstract the details of the protocol in order to send high level commands easily. The library layer provides a
convenient method to create Scapy packets that are ready to send. The Scapy dissection layer provides low-level control over the packets themselves, useful for overriding the protocol implementation itself or crafting a packet for a new SmithMeter device that utilizes new codes for the packet fields.

## Toolset

## SmithMeter Library

## Scapy Dissection
A basic usage of the dissection:

```python
smith_default_packet = IP() / Smith(address=1, dataType=2, func=3, sub=4, off=5, cmd=6)
smith_default_packet.show()
```

Note that the `byteCount` and `lrc` part of the SmithMeter protocol are automated but can be overwritten like any other
packet field. For example:

```python
Smith(byteCount=20, cmd=2, lrc=17)
```
