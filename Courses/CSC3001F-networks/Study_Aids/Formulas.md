---
tags:
  - networks
---

# CSC3001F Networks Formula Sheet

**Subject**: CSC3001F Networks  
**Source**: Current notes in `Courses/CSC3001F-networks/`  
**Format**: Markdown with Obsidian/MathJax-compatible LaTeX.

---

## Introduction

### Scaling

$$
\text{direct full-mesh ISP interconnections} = O(N^2)
$$

### Packet Delay

$$
d_{\text{trans}} = \frac{L}{R}
$$

$$
d_{\text{prop}} = \frac{d}{s}
$$

$$
d_{\text{nodal}} =
d_{\text{proc}} + d_{\text{queue}} + d_{\text{trans}} + d_{\text{prop}}
$$

Where:

- $L$ = packet length in bits
- $R$ = link transmission rate in bits per second
- $d$ = physical link distance
- $s$ = propagation speed in the medium

### Traffic Intensity

$$
\rho = \frac{La}{R}
$$

Where:

- $\rho$ = traffic intensity
- $a$ = average packet arrival rate

$$
\begin{cases}
\rho \approx 0 & \text{small queueing delay} \\
\rho \rightarrow 1 & \text{large queueing delay} \\
\rho > 1 & \text{work arrives faster than service; average delay grows without bound}
\end{cases}
$$

### Throughput

$$
\text{throughput} = \min(R_s, R_c)
$$

$$
\text{per-connection throughput} = \min(R_s, R_c, R/3)
$$

Where:

- $R_s$ = server access-link rate
- $R_c$ = client access-link rate
- $R/3$ = fair share of a shared backbone link used by three equal flows

---

## Application Layer

### Non-Persistent HTTP

$$
\begin{aligned}
T_{\text{HTTP object}}
&= 1\,RTT_{\text{TCP setup}}
 + 1\,RTT_{\text{request/first response bytes}}
 + T_{\text{trans}} \\
&= 2RTT + T_{\text{trans}}
\end{aligned}
$$

### Web Cache Utilization

$$
U_{\text{access}} =
\frac{\text{miss rate} \times \text{original data rate}}
{\text{access-link rate}}
$$

### DNS Resource Record

$$
RR = (\text{name},\ \text{value},\ \text{type},\ \text{ttl})
$$

---

## Transport Layer

### Stop-And-Wait

$$
U_{\text{sender}} =
\frac{L/R}{RTT + L/R}
$$

### TCP RTT Estimation

$$
\text{EstimatedRTT}_{\text{new}} =
(1-\alpha)\text{EstimatedRTT}_{\text{old}} + \alpha\text{SampleRTT}
$$

$$
\text{DevRTT}_{\text{new}} =
(1-\beta)\text{DevRTT}_{\text{old}}
+ \beta\left|\text{SampleRTT} - \text{EstimatedRTT}\right|
$$

$$
\text{TimeoutInterval} = \text{EstimatedRTT} + 4\text{DevRTT}
$$

### TCP Connection Management

$$
\begin{aligned}
\text{client} &\rightarrow \text{server}: \mathrm{SYN},\ \mathrm{Seq}=x \\
\text{server} &\rightarrow \text{client}: \mathrm{SYNACK},\ \mathrm{Seq}=y,\ \mathrm{ACK}=x+1 \\
\text{client} &\rightarrow \text{server}: \mathrm{ACK},\ \mathrm{ACK}=y+1
\end{aligned}
$$

$$
\mathrm{FIN}=1
$$

### TCP Flow Control

$$
rwnd = \text{free receiver buffer space}
$$

$$
\text{unACKed in-flight data} \le rwnd
$$

$$
\text{LastByteSent} - \text{LastByteAcked} \le rwnd
$$

### TCP Congestion Control

$$
\text{LastByteSent} - \text{LastByteAcked} \le cwnd
$$

$$
\text{TCP congestion rate} \approx \frac{cwnd}{RTT}
$$

$$
cwnd_0 = 1\,MSS
$$

$$
cwnd \text{ roughly doubles every } RTT \text{ during slow start}
$$

### AIMD

$$
\Delta cwnd \approx +1\,MSS \text{ per RTT until loss}
$$

$$
cwnd \leftarrow \frac{cwnd}{2} \text{ on loss}
$$

---

## Network Layer Data Plane

### CIDR

$$
\text{CIDR format} = a.b.c.d/x
$$

$$
x = \text{number of prefix bits}
$$

$$
\#\text{CIDR blocks from } /a \text{ to } /b = 2^{b-a}
$$

### Longest Prefix Matching

$$
\text{chosen route}
= \arg\max_{\text{matching prefixes}}(\text{prefix length})
$$

### NAT

$$
(\text{private IP},\ \text{private port})
\rightarrow
(\text{public IP},\ \text{new port})
$$

$$
(\text{NAT public IP},\ \text{port})
\rightarrow
(\text{LAN private IP},\ \text{port})
$$

$$
\text{incoming reply}
\rightarrow
\text{original }(\text{private IP},\ \text{port})
$$

### IPv6

$$
\text{IPv6 address length}
= 128\ \text{bits}
= 8 \times 16\text{-bit groups}
$$

### Generalized Forwarding

$$
\text{match packet header fields}
\rightarrow
\text{take action}
$$

$$
\text{flow table entry}
=
(\text{match pattern},\ \text{action},\ \text{priority},\ \text{counters})
$$

---

## Network Layer Control Plane

### Routing Graph

$$
G = (N, E)
$$

Where:

- $N$ = set of routers
- $E$ = set of links

$$
c_{x,y} =
\begin{cases}
\text{cost of direct link between }x\text{ and }y, & x,y\text{ are neighbors} \\
\infty, & x,y\text{ are not direct neighbors}
\end{cases}
$$

### Dijkstra Link-State Algorithm

$$
N' = \{u\}
$$

$$
D(v) =
\begin{cases}
c(u,v), & v\text{ is adjacent to }u \\
\infty, & v\text{ is not adjacent to }u
\end{cases}
$$

$$
w = \arg\min_{z \notin N'} D(z)
$$

$$
N' \leftarrow N' \cup \{w\}
$$

$$
D(v) \leftarrow \min\left(D(v),\ D(w) + c(w,v)\right)
$$

### Bellman-Ford / Distance Vector

$$
D_x(y) =
\min_{v \in N(x)}
\left\{c_{x,v} + D_v(y)\right\}
$$

Where:

- $D_x(y)$ = node $x$'s current least-cost estimate to destination $y$
- $N(x)$ = neighbors of node $x$
- $c_{x,v}$ = direct cost from $x$ to neighbor $v$
- $D_v(y)$ = neighbor $v$'s advertised cost to destination $y$

### BGP Route Selection

$$
\text{local preference}
\rightarrow
\text{shortest AS-PATH}
\rightarrow
\text{closest NEXT-HOP}
\rightarrow
\text{additional criteria}
$$

---

## Link Layer

### Parity

$$
(\#\text{ of 1 bits in data} + \text{parity bit}) \bmod 2 = 0
$$

$$
\text{two-dimensional parity error bit}
=
(\text{bad row},\ \text{bad column})
$$

### ARP And MAC Rules

$$
\text{ARP table entry}
=
(\text{IP address},\ \text{MAC address},\ TTL)
$$

$$
\text{broadcast MAC}
=
\mathrm{FF\!-\!FF\!-\!FF\!-\!FF\!-\!FF\!-\!FF}
$$

$$
\text{switch table entry}
=
(\text{MAC address},\ \text{interface},\ \text{timestamp/TTL})
$$

$$
\text{frame destination MAC}
=
\begin{cases}
\text{target host MAC}, & \text{same subnet} \\
\text{first-hop router MAC}, & \text{different subnet}
\end{cases}
$$

$$
\text{IP source/destination} = \text{constant end-to-end}
$$

$$
\text{MAC source/destination} = \text{changes on every link}
$$

### Switch Forwarding Rules

$$
\begin{array}{ll}
\text{unknown destination} & \rightarrow \text{flood} \\
\text{known destination on incoming interface} & \rightarrow \text{drop} \\
\text{known destination on other interface} & \rightarrow \text{forward there}
\end{array}
$$

---

## Network Security

### Basic Crypto Notation

$$
m = \text{plaintext message}
$$

$$
K_A(m) = \text{ciphertext encrypted with key }K_A
$$

$$
m = K_B(K_A(m))
$$

### Public-Key Notation

The notes write Bob's public/private keys as `K+B` and `K-B`. In this formula sheet:

$$
K_B^+ = \text{Bob's public key}
$$

$$
K_B^- = \text{Bob's private key}
$$

$$
C = K_B^+(m)
$$

$$
m = K_B^-(C)
$$

$$
m = K_B^-\left(K_B^+(m)\right)
$$

### Digital Signatures And Hashes

$$
\sigma = K_B^-(m)
$$

$$
K_B^+(\sigma) = m
$$

$$
h = H(m)
$$

$$
\sigma = K_{\text{private}}(H(m))
$$

$$
\sigma = K_B^-(H(m))
$$

$$
x = H(m)
\Rightarrow
\text{computationally infeasible to recover or find matching }m
$$

### CBC

$$
C_0 = E(K,\ P_0 \oplus IV)
$$

$$
C_1 = E(K,\ P_1 \oplus C_0)
$$

$$
C_2 = E(K,\ P_2 \oplus C_1)
$$

$$
C_i = E(K,\ P_i \oplus C_{i-1}) \quad \text{for } i \ge 1
$$

### Secure Email

$$
\begin{aligned}
K_S &= \text{random session key} \\
C &= K_S(m) \\
E &= K_B^+(K_S) \\
S &= K_A^-(H(m))
\end{aligned}
$$

$$
\begin{aligned}
K_S &= K_B^-(E) \\
m &= K_S(C) \\
\text{verify }S&\text{ with }K_A^+
\end{aligned}
$$

The notes write Alice's private signing key as `K-A`. In this formula sheet:

$$
K_A^-(H(m))
$$
