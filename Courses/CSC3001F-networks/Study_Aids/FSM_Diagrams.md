# CSC3001F Networks FSM Diagrams

**Subject**: CSC3001F Networks  
**Source**: Current notes in `Courses/CSC3001F-networks/Lecture_Notes/`, especially `../Lecture_Notes/Transport_Layer.md`  
**Format**: Mermaid `stateDiagram-v2`

---

## RDT Interface Context

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    direction LR
    [*] --> Application
    Application --> RDTSender: rdt_send(data)
    RDTSender --> UnreliableChannel: udt_send(packet)
    UnreliableChannel --> RDTReceiver: rdt_rcv(packet)
    RDTReceiver --> ApplicationReceiver: deliver_data(data)

    state "Application / upper layer" as Application
    state "RDT sender" as RDTSender
    state "Unreliable channel" as UnreliableChannel
    state "RDT receiver" as RDTReceiver
    state "Receiving application" as ApplicationReceiver
```

---

## rdt1.0 Sender

Reliable channel, so the sender only accepts data from above and sends it.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WaitCall

    state "Wait for call from above" as WaitCall

    WaitCall --> WaitCall: rdt_send(data) / make packet, udt_send(packet)
```

## rdt1.0 Receiver

Reliable channel, so the receiver only accepts packets from below and delivers data.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WaitPacket

    state "Wait for packet from below" as WaitPacket

    WaitPacket --> WaitPacket: rdt_rcv(packet) / extract data, deliver_data(data)
```

---

## rdt2.0 Sender

Bit errors possible. Sender uses checksum, ACK, NAK, and retransmission.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WaitCall

    state "Wait for call from above" as WaitCall
    state "Wait for ACK or NAK" as WaitFeedback

    WaitCall --> WaitFeedback: rdt_send(data) / make packet with checksum, udt_send(packet)
    WaitFeedback --> WaitCall: rdt_rcv(ACK)
    WaitFeedback --> WaitFeedback: rdt_rcv(NAK) / udt_send(packet again)
```

## rdt2.0 Receiver

Bit errors possible. Receiver ACKs uncorrupted packets and NAKs corrupted packets.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WaitPacket

    state "Wait for packet from below" as WaitPacket

    WaitPacket --> WaitPacket: rdt_rcv(packet) and corrupt / udt_send(NAK)
    WaitPacket --> WaitPacket: rdt_rcv(packet) and not corrupt / deliver_data(data), udt_send(ACK)
```

---

## rdt2.1 Sender

ACK or NAK can be corrupted, so sequence numbers are added. The sender alternates between sequence number 0 and sequence number 1.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WaitCall0

    state "Wait for call 0 from above" as WaitCall0
    state "Wait for ACK/NAK 0" as WaitAck0
    state "Wait for call 1 from above" as WaitCall1
    state "Wait for ACK/NAK 1" as WaitAck1

    WaitCall0 --> WaitAck0: rdt_send(data) / make pkt0, udt_send(pkt0)
    WaitAck0 --> WaitCall1: rdt_rcv(ACK) and not corrupt
    WaitAck0 --> WaitAck0: rdt_rcv(NAK) or corrupt feedback / udt_send(pkt0)

    WaitCall1 --> WaitAck1: rdt_send(data) / make pkt1, udt_send(pkt1)
    WaitAck1 --> WaitCall0: rdt_rcv(ACK) and not corrupt
    WaitAck1 --> WaitAck1: rdt_rcv(NAK) or corrupt feedback / udt_send(pkt1)
```

## rdt2.1 Receiver

Receiver uses sequence numbers to detect duplicates after corrupted ACK/NAK feedback.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> Wait0

    state "Wait for packet 0" as Wait0
    state "Wait for packet 1" as Wait1

    Wait0 --> Wait0: rdt_rcv(pkt) and corrupt / udt_send(NAK)
    Wait0 --> Wait1: rdt_rcv(pkt0) and not corrupt / deliver_data(data), udt_send(ACK)
    Wait0 --> Wait0: rdt_rcv(pkt1 duplicate) / udt_send(ACK)

    Wait1 --> Wait1: rdt_rcv(pkt) and corrupt / udt_send(NAK)
    Wait1 --> Wait0: rdt_rcv(pkt1) and not corrupt / deliver_data(data), udt_send(ACK)
    Wait1 --> Wait1: rdt_rcv(pkt0 duplicate) / udt_send(ACK)
```

---

## rdt2.2 Sender

NAKs are removed. Duplicate ACKs are used to trigger retransmission.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WaitCall0

    state "Wait for call 0 from above" as WaitCall0
    state "Wait for ACK 0" as WaitAck0
    state "Wait for call 1 from above" as WaitCall1
    state "Wait for ACK 1" as WaitAck1

    WaitCall0 --> WaitAck0: rdt_send(data) / make pkt0, udt_send(pkt0)
    WaitAck0 --> WaitCall1: rdt_rcv(ACK0) and not corrupt
    WaitAck0 --> WaitAck0: corrupt ACK or ACK1 / udt_send(pkt0)

    WaitCall1 --> WaitAck1: rdt_send(data) / make pkt1, udt_send(pkt1)
    WaitAck1 --> WaitCall0: rdt_rcv(ACK1) and not corrupt
    WaitAck1 --> WaitAck1: corrupt ACK or ACK0 / udt_send(pkt1)
```

## rdt2.2 Receiver

Receiver sends ACK for the last correctly received packet instead of sending NAK.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> Wait0

    state "Wait for packet 0" as Wait0
    state "Wait for packet 1" as Wait1

    Wait0 --> Wait1: rdt_rcv(pkt0) and not corrupt / deliver_data(data), udt_send(ACK0)
    Wait0 --> Wait0: corrupt packet or duplicate pkt1 / udt_send(ACK1)

    Wait1 --> Wait0: rdt_rcv(pkt1) and not corrupt / deliver_data(data), udt_send(ACK1)
    Wait1 --> Wait1: corrupt packet or duplicate pkt0 / udt_send(ACK0)
```

---

## rdt3.0 Sender

Loss is possible. Sender adds a timer and retransmits on timeout.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WaitCall0

    state "Wait for call 0 from above" as WaitCall0
    state "Wait for ACK 0" as WaitAck0
    state "Wait for call 1 from above" as WaitCall1
    state "Wait for ACK 1" as WaitAck1

    WaitCall0 --> WaitAck0: rdt_send(data) / make pkt0, udt_send(pkt0), start timer
    WaitAck0 --> WaitCall1: rdt_rcv(ACK0) and not corrupt / stop timer
    WaitAck0 --> WaitAck0: timeout / udt_send(pkt0), restart timer
    WaitAck0 --> WaitAck0: corrupt ACK or ACK1 / ignore

    WaitCall1 --> WaitAck1: rdt_send(data) / make pkt1, udt_send(pkt1), start timer
    WaitAck1 --> WaitCall0: rdt_rcv(ACK1) and not corrupt / stop timer
    WaitAck1 --> WaitAck1: timeout / udt_send(pkt1), restart timer
    WaitAck1 --> WaitAck1: corrupt ACK or ACK0 / ignore
```

## rdt3.0 Receiver

Receiver behavior is effectively the same ACK-only duplicate-handling logic as rdt2.2.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> Wait0

    state "Wait for packet 0" as Wait0
    state "Wait for packet 1" as Wait1

    Wait0 --> Wait1: rdt_rcv(pkt0) and not corrupt / deliver_data(data), udt_send(ACK0)
    Wait0 --> Wait0: corrupt packet or duplicate pkt1 / udt_send(ACK1)

    Wait1 --> Wait0: rdt_rcv(pkt1) and not corrupt / deliver_data(data), udt_send(ACK1)
    Wait1 --> Wait1: corrupt packet or duplicate pkt0 / udt_send(ACK0)
```

---

## Go-Back-N Sender

The notes describe the GBN sender as maintaining a window, cumulative ACKs, and one timer for the oldest in-flight packet.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WindowAvailable

    state "Window has space" as WindowAvailable
    state "Window full" as WindowFull
    state "Waiting for ACKs" as Waiting

    WindowAvailable --> Waiting: rdt_send(data) / send packet, if base == nextseqnum start timer
    WindowAvailable --> WindowFull: nextseqnum reaches base + N
    Waiting --> WindowAvailable: cumulative ACK advances base / slide window
    Waiting --> WindowFull: window becomes full
    WindowFull --> WindowAvailable: cumulative ACK advances base / slide window
    Waiting --> Waiting: timeout oldest packet / retransmit from base through nextseqnum - 1, restart timer
    WindowFull --> WindowFull: rdt_send(data) / refuse or buffer until window space
```

## Go-Back-N Receiver

The notes describe the receiver as accepting only the next expected in-order packet and re-ACKing the highest in-order packet.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WaitExpected

    state "Wait for expected packet rcv_base" as WaitExpected

    WaitExpected --> WaitExpected: expected packet arrives and not corrupt / deliver_data, send cumulative ACK, advance rcv_base
    WaitExpected --> WaitExpected: corrupt or out-of-order packet / discard, resend ACK for highest in-order packet
```

---

## Selective Repeat Sender

Selective Repeat individually tracks packets and retransmits only the timed-out packet.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WindowOpen

    state "Window has space" as WindowOpen
    state "Packet outstanding" as Outstanding
    state "Window full" as WindowFull

    WindowOpen --> Outstanding: rdt_send(data) / send packet, start packet timer
    Outstanding --> WindowOpen: individual ACK for base packet / mark received, slide base over ACKed packets
    Outstanding --> Outstanding: individual ACK for non-base packet / mark received
    Outstanding --> Outstanding: timeout for packet n / retransmit only packet n, restart timer n
    WindowOpen --> WindowFull: all window slots outstanding
    WindowFull --> WindowOpen: ACK frees one or more window slots
```

## Selective Repeat Receiver

Selective Repeat buffers out-of-order packets and individually ACKs correctly received packets.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> WaitPacket

    state "Wait for packet in receive window" as WaitPacket

    WaitPacket --> WaitPacket: packet in window and not corrupt / buffer if needed, send individual ACK
    WaitPacket --> WaitPacket: packet equals receive base / deliver in-order buffered data, slide receive window
    WaitPacket --> WaitPacket: packet outside window but previously received / resend ACK
    WaitPacket --> WaitPacket: corrupt packet / discard
```

---

## TCP Connection Management

The notes cover the three-way handshake and graceful close. This Mermaid FSM is a compact study version of those states.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
stateDiagram-v2
    [*] --> Closed

    state "CLOSED" as Closed
    state "SYN-SENT" as SynSent
    state "SYN-RECEIVED" as SynReceived
    state "ESTABLISHED" as Established
    state "FIN-WAIT" as FinWait
    state "CLOSE-WAIT" as CloseWait
    state "LAST-ACK" as LastAck
    state "TIME-WAIT" as TimeWait

    Closed --> SynSent: client sends SYN, Seq=x
    Closed --> SynReceived: server receives SYN, sends SYNACK, Seq=y, ACK=x+1
    SynSent --> Established: receives SYNACK, sends ACK=y+1
    SynReceived --> Established: receives ACK

    Established --> FinWait: active close, send FIN=1
    Established --> CloseWait: receive FIN, send ACK
    CloseWait --> LastAck: application closes, send FIN=1
    LastAck --> Closed: receive ACK for FIN

    FinWait --> TimeWait: receive FIN from peer, send ACK
    TimeWait --> Closed: timeout after final ACK safety period
```
