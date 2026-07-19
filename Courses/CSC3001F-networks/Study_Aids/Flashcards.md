# CSC3001F Networks Flashcards

## Introduction

#flashcards/CSC3001F-networks/Introduction

What is the Internet?::A global network of interconnected networks that lets hosts exchange data using shared protocols.
What is a host or end system?::A device at the edge of the Internet that runs network applications, such as a laptop, phone, server, or IoT device.
What is a communication link?::A physical or wireless channel that carries bits between network devices.
What is a packet?::A chunk of data plus protocol headers that is sent through the network.
What is a protocol?::A set of rules that defines message formats, message order, and the actions taken when messages are sent or received.
What does the Internet look like from the "nuts and bolts" view?::Hosts are connected by communication links and packet switches, all coordinated by protocols.
What does the Internet look like from the services view?::It is infrastructure that provides communication services to distributed applications.
What is an RFC?::A Request for Comments document that specifies or records Internet protocols, standards, and related engineering decisions.
What is the IETF?::The Internet Engineering Task Force, the open standards organization that develops many Internet protocols.
What is a message in networking?::Structured information exchanged by protocols between communicating entities.
What does protocol layering do?::It splits network functionality into layers, where each layer provides services to the layer above and uses services from the layer below.
What is a layer?::A functional level in a network architecture that groups related responsibilities behind a service interface.
What is a service model?::A description of what a layer offers to the layer above without exposing all internal implementation details.
Why is layering useful?::It reduces complexity, supports modular design, and allows one layer to change while preserving its interface to other layers.
What is the main downside of layering?::Layer boundaries can duplicate work, hide useful information, or make some optimizations harder.
What are the layers of the Internet protocol stack from top to bottom?::Application, transport, network, link, and physical.
What does the application layer do?::It supports network applications and defines application-level message exchange.
What does the transport layer do?::It provides logical communication between application processes running on different hosts.
What does the network layer do?::It moves packets from a source host to a destination host across networks.
What does the link layer do?::It moves frames between neighboring nodes over a single link.
What does the physical layer do?::It transmits raw bits over the physical medium.
What two layers appear in the OSI model but not as separate Internet stack layers?::Presentation and session.
What is encapsulation?::The process of wrapping data with the header information needed by each lower layer.
What is a segment?::A transport-layer packet created by adding a transport header to application data.
What is a datagram?::A network-layer packet, especially an IP packet.
What is a frame?::A link-layer packet that carries a network-layer datagram across one link.
What is the encapsulation order from application data to the link?::Application message, transport segment, network datagram, link frame.
What is a router?::A packet switch that forwards network-layer datagrams toward their destinations.
What is a network edge?::The hosts and access networks where users and applications connect to the Internet.
What is an access network?::The network that connects an end system to the first router on the path into the wider Internet.
What is the network core?::The mesh of interconnected routers and links that carries traffic across the Internet.
What is an ISP?::An Internet Service Provider that connects customers, organizations, or other networks to the Internet.
What is an IXP?::An Internet Exchange Point where networks interconnect and exchange traffic.
What is peering?::A direct interconnection between networks that exchange traffic, often to reduce cost or improve performance.
What is a tier-1 ISP?::A large backbone ISP that can reach the entire Internet without paying another provider for transit.
What is a content provider network?::A private network operated by a content provider to place services closer to users and reduce reliance on transit ISPs.
Why is the Internet described as a network of networks?::Because many independently operated networks interconnect through customer-provider relationships, peering, IXPs, and private links.
Why does a full mesh of direct ISP connections not scale?::The number of required interconnections grows quadratically as the number of networks grows.
What is forwarding?::The local router action of moving an arriving packet from an input link to the correct output link.
What is routing?::The network-wide process of computing the paths packets should follow from source to destination.
How do forwarding and routing differ?::Forwarding is a per-router data-plane action, while routing is a control-plane path-selection process.
What is packet switching?::A communication method where data is divided into packets that share network links and are forwarded independently.
What is store-and-forward transmission?::A switching behavior where a router must receive the whole packet before it can transmit that packet onto the next link.
What is transmission delay?::The time needed to push all bits of a packet onto a link.
What is the formula for transmission delay?::Packet length divided by link transmission rate.
What is propagation delay?::The time for a bit to travel across the physical link from one end to the other.
What is the formula for propagation delay?::Link distance divided by signal propagation speed.
What is processing delay?::The time a router or host spends checking headers, detecting errors, and deciding where to send a packet.
What is queueing delay?::The time a packet waits in a buffer before it can be transmitted.
What is nodal delay?::The total delay at one node, made up of processing, queueing, transmission, and propagation delays.
What is traffic intensity?::A measure of offered load on a link, commonly expressed as packet arrival rate times packet length divided by transmission rate.
What happens as traffic intensity approaches one?::Queueing delay grows rapidly because the link is nearly fully loaded.
Why does packet loss occur?::Packets can be dropped when buffers fill and there is no room for additional arrivals.
What does ping measure?::Round-trip time between a source host and a destination host using probe messages and replies.
What does traceroute show?::The sequence of routers along a path and round-trip timing information for those hops.
What is throughput?::The rate at which useful data is delivered from sender to receiver.
What is a bottleneck link?::The link on an end-to-end path whose rate limits the achievable throughput.
How is throughput limited on a simple path with one sender access link and one receiver access link?::It is limited by the slower of the sender and receiver access links.
How can a shared core link affect multiple flows?::The core link's capacity must be shared, so each flow may receive less throughput than its access links could otherwise support.
What is a packet switch?::A device that receives packets and forwards them toward their destinations, such as a router or link-layer switch.
What is a switch in the introductory Internet model?::A packet-switching device that forwards frames within a local network at the link layer.
What is the exact formula for nodal delay?::Nodal delay equals processing delay plus queueing delay plus transmission delay plus propagation delay.
What does the formula La/R measure?::Traffic intensity, where arrival rate times packet length is compared with link transmission rate.
Why can a network have high link rates but still low throughput?::The end-to-end throughput is constrained by the bottleneck link and any shared capacity on the path.
Why does store-and-forward add delay at each packet switch?::The switch must receive the full packet before beginning transmission on the next link.
Why are ping and traceroute diagnostic tools rather than transport protocols?::They probe reachability and timing, but they do not provide application data transport services.
What is the difference between a message, segment, datagram, and frame?::They are the protocol data units at application, transport, network, and link layers respectively.
What does the physical layer contribute to the Internet stack?::It defines how individual bits are represented and transmitted over physical media.
Why do routers usually not examine application-layer messages?::Routers forward based on lower-layer headers, mainly network-layer information, not application content.

## Application Layer

#flashcards/CSC3001F-networks/Application-Layer

What is a process in the application layer?::A running program on a host that communicates with other processes.
What is a client process?::A process that initiates communication with another process.
What is a server process?::A process that waits to be contacted and provides a service to clients.
What is client-server architecture?::An application architecture where always-on servers provide services to intermittently connected clients.
What is peer-to-peer architecture?::An application architecture where hosts communicate directly and can act as both clients and servers.
What is the main scaling advantage of peer-to-peer systems?::Peers contribute resources, so capacity can grow as more peers join.
What is a socket?::The interface between an application process and the transport layer.
What information identifies a receiving process on the Internet?::The destination host's IP address and the destination process's port number.
What is an IP address?::A network-layer identifier for a host or router interface.
What is a port number?::A transport-layer identifier used to select the receiving process on a host.
What is a data integrity requirement?::An application's need for data to arrive correctly and without loss.
What is a timing requirement?::An application's need for data to arrive within a time bound.
What is a throughput requirement?::An application's need for at least some minimum data delivery rate.
What is an elastic application?::An application that can still function across a wide range of available throughput.
What does TCP provide to applications?::Reliable byte-stream delivery, flow control, congestion control, and connection-oriented communication.
What does UDP provide to applications?::Connectionless, best-effort message delivery with minimal transport-layer service.
Why might an application choose UDP?::To avoid connection setup and transport reliability overhead, or to control timing and recovery itself.
What is an application-layer protocol?::A protocol that defines how application processes exchange messages.
What does an application-layer protocol specify?::Message types, syntax, semantics, and rules for when messages are sent and acted on.
What is an open protocol?::A protocol whose specification is publicly available and can be implemented by anyone.
What is a proprietary protocol?::A protocol controlled by an organization and not necessarily publicly specified.
What is HTTP?::The Web's application-layer protocol for transferring web objects between clients and servers.
What is a web object?::A file or resource that can be addressed by a URL, such as HTML, an image, or a script.
What is a URL?::A Uniform Resource Locator that identifies a resource by protocol, host, and path.
What does it mean that HTTP is stateless?::The server does not retain protocol-level information about previous client requests.
What is RTT?::Round-trip time, the time for a small packet to travel from client to server and back.
<!--SR:!2026-06-03,3,250-->
What is non-persistent HTTP?::HTTP where each object is transferred over a separate TCP connection.
What is persistent HTTP?::HTTP where multiple objects can be transferred over the same TCP connection.
Why is persistent HTTP generally more efficient than non-persistent HTTP?::It avoids repeated TCP connection setup and can transfer multiple objects over an existing connection.
What is the basic response-time cost for a non-persistent HTTP object?::Two RTTs plus the object's transmission time.
What is the purpose of the HTTP GET method?::To request a resource from a server.
What is the purpose of the HTTP POST method?::To send form data or other data to a server for processing.
What is the purpose of the HTTP HEAD method?::To request headers for a resource without requesting the full object body.
What is the purpose of the HTTP PUT method?::To upload or replace a resource at a specified location.
What does a successful HTTP response status indicate?::The server understood and successfully handled the request.
What does an HTTP redirection response indicate?::The requested resource is available at another location.
What does an HTTP client error response indicate?::The request was invalid or the requested resource could not be provided because of a client-side issue.
What does an HTTP server/version error response indicate?::The server cannot handle the request or does not support the required HTTP behavior.
What is a cookie?::State information stored at the client and sent with requests so a server can recognize a user or session.
What are the main components of cookie-based state?::A response header, a request header, a client-side cookie file, and a server-side database entry.
Why are cookies useful?::They support sessions, authentication, shopping carts, personalization, and tracking across otherwise stateless HTTP.
What privacy issue do cookies create?::They can allow user activity to be tracked across requests or sites.
What is a web cache?::An intermediary that stores copies of web objects and can satisfy later client requests.
What is a proxy server in web caching?::A server that receives client requests and either serves cached content or forwards the request to the origin server.
How can web caching reduce response time?::By serving objects from a nearby cache instead of repeatedly fetching them from the origin server.
How can web caching reduce network load?::By reducing repeated transfers across access links and upstream networks.
What is a conditional GET?::An HTTP request that asks for an object only if the cached version is stale.
What HTTP header is used for a conditional GET timestamp check?::The If-Modified-Since header.
What response does a server send when a cached object is still valid?::A not-modified response without resending the full object.
What is DNS?::The Domain Name System, a distributed service that maps names to values such as IP addresses.
What services does DNS provide?::Hostname-to-IP translation, host aliasing, mail server aliasing, and load distribution.
Why is DNS distributed instead of centralized?::A centralized design would create a single point of failure, heavy traffic concentration, high latency for distant users, and maintenance problems.
What is a root DNS server?::A top-level DNS server that directs queries toward the appropriate top-level domain servers.
What is a TLD server?::A DNS server responsible for a top-level domain such as a generic or country-code domain.
What is an authoritative DNS server?::A DNS server that holds the official resource records for a domain.
What is a local DNS server?::A resolver contacted by a host that performs DNS lookup work and caches results.
What is an iterated DNS query?::A query pattern where each DNS server replies with the next server to contact.
What is a recursive DNS query?::A query pattern where the contacted DNS server is responsible for obtaining the final answer.
What is DNS caching?::The temporary storage of DNS replies so later queries can be answered faster.
What is a DNS resource record?::A typed DNS entry containing a name, value, type, and time-to-live.
What does an A record do?::It maps a hostname to an IPv4 address.
What does an NS record do?::It identifies an authoritative name server for a domain.
What does a CNAME record do?::It maps an alias name to a canonical hostname.
What does an MX record do?::It identifies a mail server for a domain.
What is TTL in DNS?::The time-to-live value that limits how long a DNS record may be cached.
What fields are found in a DNS message?::Header fields, question fields, answer records, authority records, and additional information.
What does UDP socket programming require the sender to include with each datagram?::The destination IP address and destination port.
What information does a UDP receiver extract from an arriving datagram?::The message plus the sender's IP address and sender port so a reply can be addressed.
What is the basic UDP server pattern?::Bind a UDP socket to a port, wait for datagrams, read each message and client address, then send replies to that client address.
What is the basic UDP client pattern?::Create a UDP socket, build a datagram addressed to the server IP and port, send it, read any reply, then close the socket.
How does TCP socket programming differ from UDP socket programming?::TCP first establishes a connection and then exchanges a reliable byte stream, while UDP sends independent datagrams without setup.
What is a TCP welcoming socket?::A server socket that listens for new TCP connection requests on a known port.
What is a TCP connection socket?::A socket created by the server for one accepted client connection.
Why can a TCP server handle multiple clients at once?::Each accepted client gets a separate connection socket identified by its connection endpoints.
Why does TCP not preserve application message boundaries?::TCP provides a byte stream, so applications must define their own message framing if needed.
What is the structure of an HTTP request message?::A request line, headers, a blank line, and optionally a message body.
What is the structure of an HTTP response message?::A status line, headers, a blank line, and optionally object data.
What does the HTTP Host header identify?::The server hostname for the requested resource, which is needed when multiple sites may share an IP address.
What does the HTTP User-Agent header describe?::The client software making the request.
What does the HTTP Accept header describe?::The content types the client is willing to receive.
What does the HTTP Connection header influence?::Whether the TCP connection should be kept alive or closed after the response.
What does HTTP status 200 OK mean?::The request succeeded.
What does HTTP status 301 Moved Permanently mean?::The requested object has moved and the response gives a new location.
What does HTTP status 400 Bad Request mean?::The server could not understand the request.
What does HTTP status 404 Not Found mean?::The requested object was not found.
What does HTTP status 505 HTTP Version Not Supported mean?::The server does not support the HTTP version used by the request.
What does the Set-Cookie header do?::It asks the browser to store cookie state provided by the server.
What does the Cookie header do?::It sends previously stored cookie state back to the server on later requests.
What are common uses of cookies?::Authorization, shopping carts, recommendations, and session state.
What is the web-cache miss path?::The cache forwards the request to the origin server, stores the returned object, and returns it to the client.
What does a fresh cache hit avoid?::It avoids contacting the origin server and avoids transferring the object across upstream links again.
What is the web-cache access-link utilization formula?::Cache miss rate times original data rate divided by access-link rate.
What does a conditional GET response of 304 Not Modified mean?::The cached object is still valid and the server does not send the full object body.
What does a conditional GET response of 200 OK mean in this context?::The object changed, so the server sends the updated object data.
What is the DNS hierarchy?::Root servers point to TLD servers, which point to authoritative servers for domains.
What role does the local DNS server play outside the strict DNS hierarchy?::It is the host's resolver, answering from cache or resolving names through the hierarchy.
What is the usual DNS resolution path for an uncached hostname?::The resolver queries root, then TLD, then authoritative DNS servers to obtain the final record.
How does DNS support load distribution?::A name can map to multiple replicated server IP addresses.
What is the DNS resource-record format?::A name, value, type, and time-to-live.
What fields identify counts in DNS query and reply messages?::Question count, answer resource-record count, authority resource-record count, and additional resource-record count.
Why is DNS considered an application-layer protocol?::It runs as a network application even though other applications depend on it for naming.

## Transport Layer

#flashcards/CSC3001F-networks/Transport-Layer

What is the transport layer?::The layer that provides logical communication between application processes on different hosts.
What is logical communication?::The illusion that processes communicate directly, even though data passes through many network devices.
What is a transport-layer segment?::An application message plus a transport-layer header.
What is TCP?::A connection-oriented transport protocol that provides reliable byte-stream delivery, flow control, and congestion control.
What is UDP?::A connectionless transport protocol that provides best-effort datagram delivery with minimal overhead.
What services do TCP and UDP both provide?::Process-to-process delivery using port numbers and basic error detection through checksums.
What services does UDP not provide?::Reliability, ordering, flow control, congestion control, and connection setup.
What is multiplexing at the transport layer?::Collecting data from multiple application sockets and adding header information so segments can be delivered through the network.
What is demultiplexing at the transport layer?::Using header fields in received segments to deliver data to the correct application socket.
What is the role of port numbers in multiplexing and demultiplexing?::They identify the sending and receiving application processes on hosts.
How is a UDP socket identified for demultiplexing?::By destination IP address and destination port number.
How is a TCP socket identified for demultiplexing?::By source IP address, source port, destination IP address, and destination port.
Why does TCP need more socket-identifying information than UDP?::TCP must distinguish separate connections, even when they target the same server port.
What is reliable data transfer?::A transport service that delivers data correctly, in order, and without loss or duplication despite an unreliable underlying channel.
What is a checksum?::A value computed over data to help detect bit errors.
What is a NAK?::A negative acknowledgement indicating that data was received incorrectly.
What is an ACK?::An acknowledgement indicating that data was received correctly.
What is a sequence number?::A number attached to data so receivers and senders can detect loss, duplication, and ordering.
What is stop-and-wait?::A protocol pattern where the sender transmits one packet and waits for its acknowledgement before sending the next.
What is the utilization formula for stop-and-wait?::Transmission time divided by round-trip time plus transmission time.
Why is stop-and-wait inefficient on long-delay or high-rate paths?::The sender spends most of its time waiting rather than transmitting.
What is pipelining?::Allowing multiple packets to be in flight before acknowledgements return.
What protocol mechanisms are needed for pipelining?::A larger sequence number space, buffering, and sender/receiver rules for handling multiple outstanding packets.
What is Go-Back-N?::A pipelined reliable data transfer protocol where the sender may have several unacknowledged packets but retransmits from the oldest missing packet after a loss.
What is a cumulative ACK?::An acknowledgement that confirms receipt of all packets up to a given sequence number.
How does the Go-Back-N receiver handle out-of-order packets?::It discards them and repeats the acknowledgement for the highest in-order packet received.
What is Selective Repeat?::A reliable data transfer protocol where the receiver individually acknowledges correctly received packets and the sender retransmits only missing packets.
How does Selective Repeat differ from Go-Back-N?::Selective Repeat buffers out-of-order packets and retransmits only lost packets, while Go-Back-N discards out-of-order packets and may retransmit many packets.
What is MSS?::Maximum Segment Size, the largest amount of application data TCP places in one segment.
What is a TCP timeout?::The timer expiration that causes TCP to retransmit a segment that has not been acknowledged in time.
What is SampleRTT?::A measured round-trip time for a TCP segment and its acknowledgement.
What is EstimatedRTT?::A smoothed estimate of round-trip time based on recent SampleRTT values.
What is DevRTT?::An estimate of how much SampleRTT varies around EstimatedRTT.
What is the TCP TimeoutInterval?::EstimatedRTT plus a safety margin based on RTT variation.
Why does TCP estimate RTT instead of using one fixed timeout?::Network delay changes over time, so a fixed timeout could retransmit too early or wait too long.
What is fast retransmit?::A TCP mechanism that retransmits a segment before timeout after duplicate acknowledgements suggest loss.
What does a TCP SYN segment do?::It starts connection setup and synchronizes sequence numbers.
What does a TCP FIN segment do?::It starts graceful connection termination.
What is the TCP three-way handshake?::The connection setup exchange where the client sends SYN, the server replies with SYN-ACK, and the client replies with ACK.
Why does TCP use a handshake before data transfer?::To establish connection state and initial sequence numbers at both endpoints.
What is TCP flow control?::A mechanism that prevents the sender from overwhelming the receiver's buffer.
What is the receive window?::The amount of buffer space the receiver advertises as available for incoming data.
What condition does TCP flow control enforce?::Unacknowledged data in flight must not exceed the receiver's advertised window.
What is congestion?::A network condition where too much traffic is offered for available resources, causing delay and loss.
What is congestion control?::A mechanism that adjusts sender behavior to avoid or respond to congestion in the network.
How does congestion differ from flow-control pressure?::Congestion concerns overloaded network paths, while flow control concerns receiver buffer capacity.
What is cwnd?::TCP's congestion window, which limits how much unacknowledged data the sender may have in flight due to congestion control.
How does TCP estimate its sending rate from cwnd?::The approximate sending rate is congestion window divided by round-trip time.
What is AIMD?::Additive Increase Multiplicative Decrease, where TCP gradually increases sending rate and sharply reduces it after congestion.
What is slow start?::A TCP phase where the congestion window grows rapidly from a small initial value until a threshold or loss event is reached.
Why is TCP congestion control considered end-to-end?::The sender infers congestion from loss and acknowledgements instead of relying on explicit router feedback.
What is network-assisted congestion control?::Congestion control where routers provide explicit feedback about congestion to endpoints.
What are the costs of congestion?::Higher delay, packet loss, retransmissions, wasted transmission work, and reduced useful throughput.
What does rdt_send represent in reliable data transfer models?::The call from the application or upper layer requesting that data be sent reliably.
What does udt_send represent in reliable data transfer models?::The call that sends a packet over the unreliable lower-layer channel.
What does rdt_rcv represent in reliable data transfer models?::The event where a packet arrives from the unreliable lower-layer channel.
What does deliver_data represent in reliable data transfer models?::The delivery of correctly received data to the receiving application or upper layer.
What assumption does rdt1.0 make?::The underlying channel is perfectly reliable.
What problem does rdt2.0 address?::Bit errors in packets.
What problem remains in rdt2.0?::ACK or NAK messages themselves can be corrupted.
What does rdt2.1 add to handle corrupted acknowledgements?::Sequence numbers and retransmission rules that let duplicates be detected.
What does rdt2.2 remove compared with rdt2.1?::NAKs, using duplicate ACKs instead.
What problem does rdt3.0 address?::Packet loss, using timers and retransmissions.
What unreliable-channel problems can reliable data transfer have to hide?::Corruption, loss, duplication, and reordering.
Why does the sender not directly know the receiver's state in RDT?::It only learns receiver state through returned messages such as ACKs.
How does rdt3.0 handle data-packet loss?::The sender times out and retransmits the packet.
How does rdt3.0 handle ACK loss?::The sender may retransmit, and the receiver uses sequence numbers to detect and discard duplicates.
How does rdt3.0 handle a premature timeout?::A duplicate packet may arrive, so the receiver discards the duplicate and re-ACKs the data.
What does a Go-Back-N sender keep in its window?::Up to N consecutive transmitted but unacknowledged packets.
What timer does Go-Back-N maintain?::A timer for the oldest in-flight packet.
What does a Go-Back-N sender retransmit after timeout?::The timed-out packet and all later packets currently in the window.
What state does a simple Go-Back-N receiver need to remember?::The base or next expected in-order packet.
What does Selective Repeat require at the receiver?::Buffering of out-of-order packets until missing earlier packets arrive.
What does Selective Repeat require at the sender?::Individual tracking and timers for unacknowledged packets.
Why is Selective Repeat usually more efficient than Go-Back-N when loss occurs?::It retransmits only missing packets instead of retransmitting correctly received later packets.
What does the TCP sequence number in a segment identify?::The byte-stream number of the first data byte in that segment.
What does a TCP acknowledgement number identify?::The next byte expected from the other side.
Which TCP fields support multiplexing and demultiplexing?::Source port and destination port.
Which TCP field supports flow control?::The receive window field.
Which TCP field supports error detection?::The checksum field.
Which TCP flags are used for connection management?::SYN, FIN, and RST.
What does the TCP ACK bit indicate?::That the acknowledgement field is valid.
What are TCP CWR and ECE related to?::Explicit congestion notification.
What is the TCP header length field used for?::It tells how large the TCP header is.
What are TCP options used for?::Optional TCP features beyond the fixed header fields.
What is the exact EstimatedRTT update formula?::EstimatedRTT equals one minus alpha times the previous EstimatedRTT plus alpha times SampleRTT.
What is the exact DevRTT update formula?::DevRTT equals one minus beta times previous DevRTT plus beta times the absolute difference between SampleRTT and EstimatedRTT.
What is the exact TCP TimeoutInterval formula?::TimeoutInterval equals EstimatedRTT plus four times DevRTT.
Why are retransmitted segments ignored in SampleRTT measurement?::The sender cannot reliably tell whether the ACK corresponds to the original transmission or the retransmission.
What does a TCP sender do when application data arrives?::It creates a segment with a sequence number and starts the timer if needed.
What does a TCP sender do on timeout?::It retransmits the segment associated with the timeout and restarts the timer.
What does a TCP sender do when an ACK acknowledges new data?::It advances the send base and restarts the timer if unacknowledged data remains.
When does a TCP receiver send a duplicate ACK?::When an out-of-order segment arrives above the next expected byte.
What does a TCP receiver do when a segment fills a gap?::It sends an ACK immediately.
Why can a two-way handshake fail for TCP connection setup?::Old, delayed, reordered, or retransmitted messages can create half-open state or duplicate data acceptance.
What are the three TCP handshake steps?::Client sends SYN, server replies with SYN-ACK, and client replies with ACK.
How does TCP closing work at a high level?::Each direction closes independently using FIN and ACK exchanges.
Why can an ACK for a FIN be combined with another FIN?::A receiver may acknowledge the peer's close while also closing its own sending direction.
What causes receiver-buffer overflow risk in TCP?::TCP may deliver data into the socket buffer faster than the application reads it.
How does a receiver advertise flow-control capacity?::It places its available receive-buffer space in the TCP receive window field.
What is the exact TCP flow-control condition?::LastByteSent minus LastByteAcked must be less than or equal to rwnd.
What is the difference between flow control and congestion control?::Flow control protects the receiver buffer, while congestion control protects routers and links in the network.
What are the main costs of congestion?::Queueing delay, packet loss, retransmissions, unnecessary duplicates, wasted upstream work, and lower effective throughput.
What is end-to-end congestion control feedback based on?::Endpoint observations such as loss, delay, duplicate ACKs, or timeouts.
What is network-assisted congestion control feedback based on?::Explicit congestion information supplied by routers or network devices.
What is TCP additive increase?::Raising the sending rate gradually, roughly by one MSS per RTT, until congestion is detected.
What is TCP multiplicative decrease?::Cutting the sending rate sharply, commonly by about half, after congestion is detected.
How does slow start grow cwnd?::It increases cwnd for each ACK, causing cwnd to roughly double every RTT.
When does slow start stop?::When a loss event occurs or a configured threshold is reached.

## Network Layer Data Plane

#flashcards/CSC3001F-networks/Network-Layer-Data-Plane

What is the network layer?::The layer responsible for moving packets from sending hosts to receiving hosts across networks.
What is best-effort service?::A service model that makes no guarantees about delivery, order, timing, or bandwidth.
What is QoS?::Quality of Service, a set of guarantees or controls over performance properties such as delay, loss, or bandwidth.
What is the data plane?::The per-packet forwarding function that moves packets through routers.
What is the control plane?::The routing and management logic that determines how packets should be forwarded.
What is per-router control plane?::A design where each router participates in routing and computes its own forwarding table.
What is SDN control plane?::A design where a logically centralized controller computes or installs forwarding behavior for network devices.
What is destination-based forwarding?::Forwarding that selects an output link based on the packet's destination address.
What is longest prefix matching?::Choosing the forwarding-table entry with the most specific matching address prefix.
Why is longest prefix matching necessary?::More-specific routes must override broader aggregate routes when both match a destination.
What is an IPv4 address?::A 32-bit identifier assigned to a host or router interface.
What is a network interface?::The attachment point between a host or router and a network link.
What is a subnet?::A set of interfaces that can reach each other without passing through a router.
What is a subnet mask or prefix length?::The part of an IP address that identifies the network portion shared by a subnet.
What is CIDR?::Classless Inter-Domain Routing, which represents address blocks using arbitrary-length prefixes.
What is route aggregation?::Combining several smaller, contiguous network prefixes into one larger prefix that can be advertised as a single summary route.
How does CIDR support route aggregation?::A single prefix can represent many addresses or smaller subnets, reducing routing-table size.
What is hierarchical addressing?::Assigning addresses so that larger prefixes can summarize groups of more-specific networks.
What is DHCP?::Dynamic Host Configuration Protocol, which automatically gives hosts network configuration information.
What are the main DHCP exchange steps?::Discover, offer, request, and acknowledgement.
What configuration information can DHCP provide?::An IP address, subnet mask, default gateway, and DNS server information.
What is NAT?::Network Address Translation, which rewrites packet addresses or ports between a private network and the public Internet.
What is a private IP address space?::Address ranges intended for internal networks and not globally routed on the public Internet.
What is a NAT translation table?::State maintained by a NAT device that maps internal address-port pairs to external address-port pairs.
Why is NAT useful?::It allows many internal hosts to share fewer public addresses and hides internal addressing details.
What is a common criticism of NAT?::It breaks the clean end-to-end addressing model and can complicate peer-to-peer or inbound connections.
What is IPv6?::A newer Internet Protocol version with larger addresses and simplified header design compared with IPv4.
Why was IPv6 introduced?::Primarily to expand the address space and improve aspects of IP header handling.
What is the IPv6 flow label?::A field intended to identify packets that should receive special handling as part of a flow.
What is the IPv6 hop limit?::The field that limits how many routers a packet may traverse, replacing IPv4's TTL role.
What IPv4 header features were removed or changed in IPv6?::Header checksum, fragmentation by routers, and options in the fixed header were removed or redesigned.
What is tunneling in IPv6 transition?::Carrying IPv6 packets inside IPv4 packets so they can cross IPv4-only parts of the network.
What is generalized forwarding?::Forwarding based on matching multiple packet-header fields and applying specified actions.
What is a flow table?::A table of match-action rules used by a switch or router for generalized forwarding.
What is OpenFlow?::A protocol and model for controlling match-action forwarding tables in SDN-capable devices.
What kinds of actions can generalized forwarding apply?::Forward, drop, modify, or send packets to a controller.
What packet fields can generalized forwarding match on?::Fields across link, network, and transport headers, depending on device capabilities.
How does a router use a forwarding table?::It looks up packet header information and selects the appropriate outgoing interface or action.
Why does the network layer sit above the link layer?::It provides end-to-end packet delivery across multiple links, while the link layer handles one-hop delivery.
Why does the network layer sit below the transport layer?::It provides host-to-host packet delivery that transport protocols use to provide process-to-process service.
What does the IPv4 version field identify?::The IP protocol version used by the datagram.
What does the IPv4 header length field identify?::The size of the IPv4 header.
What does the IPv4 type-of-service field support?::Differentiated services and explicit congestion notification bits.
What does the IPv4 total length field identify?::The total datagram length in bytes.
Which IPv4 fields support fragmentation and reassembly?::Identifier, flags, and fragment offset.
What does the IPv4 TTL field do?::It limits the number of remaining router hops and is decremented by routers.
What does the IPv4 upper-layer protocol field identify?::The payload protocol, such as TCP or UDP.
What does the IPv4 header checksum detect?::Errors in the IPv4 header.
What do the IPv4 source and destination address fields identify?::The sender and destination interfaces at the network layer.
What is the IPv4 payload usually?::A transport-layer segment such as TCP or UDP data.
What are the two parts of a structured IP address?::The subnet prefix in the high-order bits and the host/interface part in the low-order bits.
Why should you say an IP address belongs to an interface rather than a host?::A host or router can have multiple interfaces, each with its own IP address.
What does CIDR notation a.b.c.d/x mean?::The first x bits are the network prefix for the address block.
What is the CIDR block-count rule when splitting from prefix /a to /b?::The number of equal smaller blocks is two to the power of b minus a.
How does a more-specific route interact with an aggregate route?::Longest prefix matching sends matching traffic to the more-specific route.
What organization manages global IP address allocation and the DNS root zone?::ICANN coordinates those global Internet resources.
Why did IPv4 address exhaustion motivate NAT and IPv6?::The finite IPv4 address space could not support indefinite growth in globally unique public addresses.
How can DHCP support mobile users?::It can assign configuration dynamically when a host joins a network and release or renew leases over time.
What are the four DHCP messages in order?::Discover, Offer, Request, and ACK.
What does NAT rewrite on outbound traffic?::The private source IP and source port are replaced with the NAT public IP and a new source port.
What does NAT store for outbound traffic?::A translation-table mapping between the public address-port pair and the original private address-port pair.
How does NAT handle an inbound reply?::It looks up the public destination address-port pair, rewrites it to the private destination, and forwards it into the LAN.
What NAT advantage supports changing ISPs?::Internal private addresses can remain unchanged even if the external public address changes.
What NAT controversy is a layer violation?::NAT devices edit transport-layer port numbers even though routers are normally expected to operate at layer 3.
What NAT controversy affects inbound connections?::External clients may struggle to initiate connections to hosts hidden behind NAT without traversal mechanisms.
What are the main motivations for IPv6?::Larger address space, faster forwarding with a simpler fixed header, and support for different treatment of flows.
How are IPv6 addresses written?::As eight groups of 16-bit hexadecimal values.
How does IPv6 zero compression work conceptually?::Leading zeroes in groups may be omitted, and one run of consecutive all-zero groups may be compressed once.
Why can IPv6 double-colon shorthand be used only once?::Using it more than once would make the number of omitted zero groups ambiguous.
What did IPv6 remove from the main router fast path?::Header checksum, router fragmentation, and fixed-header options.
How does IPv6 handle options compared with IPv4?::IPv6 moves optional information into next-header mechanisms rather than the main fixed header.
Why does tunneling help IPv6 deployment?::IPv6 packets can cross IPv4-only network regions inside IPv4 packets.
In IPv6 tunneling, which addresses belong to the outer packet?::The IPv4 addresses of the tunnel endpoints.
In IPv6 tunneling, what remains inside the tunneled packet?::The original IPv6 datagram with its original IPv6 source and destination.
What fields are stored in a generalized forwarding flow-table entry?::Match pattern, action, priority, and counters.
What link-layer fields can OpenFlow match?::Ingress port, source MAC, destination MAC, Ethernet type, and VLAN ID.
What network-layer fields can OpenFlow match?::IP source, IP destination, IP protocol, and IP type-of-service fields.
What transport-layer fields can OpenFlow match?::TCP or UDP source and destination ports.
How can generalized forwarding express firewall behavior?::It can match addresses and ports, then permit or deny by forwarding or dropping.
How can generalized forwarding express NAT-like behavior?::It can match address-port fields and modify header values.

## Network Layer Control Plane

#flashcards/CSC3001F-networks/Network-Layer-Control-Plane

What is the control plane in routing?::The logic that computes, distributes, and updates the forwarding information used by routers.
What is a routing protocol?::A protocol that lets routers exchange information and compute paths through a network.
What is a path in routing?::A sequence of routers and links from a source to a destination.
What is a graph in routing?::An abstraction where nodes represent routers and edges represent links.
What is link cost?::A weight assigned to a link, often representing distance, delay, congestion, or administrative preference.
What is a global routing algorithm?::An algorithm that computes routes using complete network topology and link-cost information.
What is a decentralized routing algorithm?::An algorithm where routers compute routes using information exchanged with neighbors.
What is static routing?::Routing where paths are manually configured and change slowly or only by administrative action.
What is dynamic routing?::Routing where paths are computed and updated automatically in response to topology or cost changes.
What is a link-state algorithm?::A routing approach where routers learn the network topology and compute shortest paths.
What is Dijkstra's algorithm used for in routing?::Computing shortest paths from one source to all destinations given link costs.
What does N' mean in Dijkstra's algorithm?::The set of nodes whose least-cost paths from the source are known.
What does D(v) mean in Dijkstra's algorithm?::The current least-cost estimate from the source to node v.
What does p(v) mean in Dijkstra's algorithm?::The predecessor node before v on the current least-cost path from the source.
<!--SR:!2026-06-03,3,250-->
What are the main steps of Dijkstra's algorithm?::Initialize costs, repeatedly add the lowest-cost unknown node, and update costs through that node.
<!--SR:!2026-06-04,4,270-->
What is a distance-vector algorithm?::A routing approach where each router maintains cost estimates to destinations and exchanges them with neighbors.
What is the Bellman-Ford equation used for?::Computing the least cost to a destination as the minimum over neighbor cost plus neighbor's advertised distance.
What information does a distance-vector router exchange?::Its current distance estimates to destinations, sent to neighboring routers.
Why can distance-vector routing converge slowly?::Routers only have neighbor information, so bad news can propagate gradually.
What is an autonomous system?::A group of routers under one administrative control using a common routing policy.
What is a gateway router?::A router in an autonomous system that connects to routers in other autonomous systems.
What is intra-AS routing?::Routing within one autonomous system.
What is inter-AS routing?::Routing between autonomous systems.
<!--SR:!2026-06-04,4,270-->
What is OSPF?::Open Shortest Path First, a link-state intra-AS routing protocol.
What does OSPF flood through an AS?::Link-state information used by routers to compute shortest paths.
What is hierarchical OSPF?::An OSPF design that divides an AS into areas with a backbone to improve scalability.
<!--SR:!2026-06-04,4,270-->
Why does hierarchical OSPF improve scalability?::It limits how much topology detail routers must store and flood across the entire AS.
What is BGP?::Border Gateway Protocol, the inter-AS routing protocol used to exchange reachability information between autonomous systems.
What is a path-vector protocol?::A routing protocol that advertises entire AS-level paths rather than only distances.
What is eBGP?::BGP communication between routers in different autonomous systems.
What is iBGP?::BGP communication between routers within the same autonomous system.
<!--SR:!2026-06-04,4,270-->
What is a prefix in BGP?::An address block that an autonomous system advertises as reachable.
What is AS-PATH?::A BGP attribute listing the autonomous systems a route advertisement has traversed.
What is NEXT-HOP?::A BGP attribute identifying the router interface to use as the next hop toward a prefix.
What is policy-based routing?::Route selection or advertisement based on business, security, or administrative policy rather than only technical path cost.
What is hot potato routing?::Choosing the route that gets traffic out of the local autonomous system as quickly as possible.
What is a route leak?::The accidental or improper advertisement of routes beyond their intended scope.
Why do intra-AS and inter-AS routing use different protocols?::Intra-AS routing emphasizes performance and internal control, while inter-AS routing must handle scale and policy between organizations.
<!--SR:!2026-06-04,4,270-->
What is a BGP route advertisement?::A message that tells other routers a prefix is reachable through a given AS path and next hop.
What happens when a BGP router receives multiple routes to a prefix?::It applies route-selection rules and policy to choose one best route.
What is the typical high-level BGP route selection order?::Apply local preference and policy, prefer shorter AS paths, consider next-hop cost, then use tie-breakers.
Why is AS-PATH useful for loop prevention?::A router can reject a route advertisement that already contains its own autonomous system.
Why does BGP care about business relationships?::Networks often choose and export routes based on customer, provider, and peer agreements.
What is the role of forwarding tables after routing protocols run?::They store the next-hop or output-interface decisions used by the data plane.
What is the graph notation used for routing?::A graph G equals N and E, where N is the set of router nodes and E is the set of links.
What does Dijkstra relaxation do?::It updates a neighbor's current cost estimate if going through the newly finalized node gives a lower cost.
What is the Dijkstra relaxation formula in words?::The estimate to v becomes the smaller of its current estimate and the cost to w plus the cost from w to v.
What does the Bellman-Ford equation say in words?::A router's best cost to a destination is the minimum neighbor-link cost plus that neighbor's advertised cost to the destination.
What is the main information difference between link-state and distance-vector routing?::Link-state uses complete topology information, while distance-vector uses estimates exchanged with neighbors.
What does a link-state router flood?::Information about its local links and link costs.
Why does Dijkstra require complete topology knowledge?::It computes shortest paths by comparing costs across the full graph.
What does a distance-vector router initially know?::Its own cost to directly connected neighbors.
Why can distance-vector routing suffer from slow bad-news propagation?::Routers learn indirectly through neighbors, so stale optimistic estimates can persist.
Why does Internet routing need autonomous systems?::They make routing scalable and allow separate organizations to apply their own policies.
What problem would flat global routing create?::Huge routing tables and excessive update traffic across the whole Internet.
What does an OSPF area contain?::A subset of routers that share detailed link-state information locally.
What is the role of the OSPF backbone?::It connects OSPF areas and carries summarized routing information between them.
What does eBGP learn?::Reachability information from neighboring autonomous systems.
What does iBGP distribute?::Externally learned BGP reachability information within the same autonomous system.
What does a BGP route advertisement carry?::A reachable prefix plus attributes such as AS-PATH and NEXT-HOP.
What does local preference represent in BGP selection?::An administrative policy preference for one route over another.
Why can BGP policy override technical shortest paths?::Business and administrative rules are applied before or alongside path-length considerations.
What does closest NEXT-HOP mean in BGP route selection?::Choosing the route whose next-hop gateway has the lowest intra-AS cost from the selecting router.
How does hot potato routing relate to closest NEXT-HOP?::It sends traffic to the nearest exit gateway, minimizing cost inside the local AS.
Why is AS-PATH not the same as a router-by-router path?::It lists autonomous systems, not every internal router hop.
What does a route leak risk doing at Internet scale?::It can attract or redirect traffic along unintended AS paths.
Why does iBGP still depend on intra-AS routing?::iBGP tells routers which gateway reaches a prefix, but internal routing determines how to reach that gateway.

## Link Layer

#flashcards/CSC3001F-networks/Link-Layer

What is the link layer?::The layer that transfers frames between neighboring nodes over a single communication link.
What is a node in the link layer?::A host, router, switch, or other device connected to links.
What is a link?::A communication channel connecting adjacent nodes.
<!--SR:!2026-06-04,4,270-->
What is a frame?::A link-layer packet that encapsulates a network-layer datagram.
What is framing?::Adding link-layer headers and trailers so data can be sent across a link as a frame.
What is link access?::The rules for using a link, especially when multiple devices share the same medium.
What is error correction?::A technique that lets a receiver recover from certain bit errors without retransmission.
What is full duplex?::Communication where both ends can transmit at the same time.
What is half duplex?::Communication where devices share a medium and cannot transmit simultaneously without conflict.
What is a NIC?::A Network Interface Card or adapter that implements link-layer and physical-layer functions.
Where is the link layer commonly implemented?::In the network adapter or NIC, with support from device drivers and operating-system software.
What is error detection?::A method for detecting whether bits were corrupted during transmission.
What is EDC?::Error Detection and Correction bits added to data to help detect or correct transmission errors.
What is a parity bit?::A simple error-detection bit chosen to make the number of one bits even or odd.
<!--SR:!2026-06-04,4,270-->
What can one-dimensional parity detect?::Single-bit errors, but not all multi-bit errors.
What is two-dimensional parity?::A parity scheme that adds parity across rows and columns to improve error detection and locate some errors.
What is a point-to-point link?::A link with one sender and one receiver at its ends.
What is a broadcast link?::A shared link where transmissions can be heard by multiple attached nodes.
What is a multiple access protocol?::A protocol that coordinates transmissions by multiple nodes sharing a broadcast channel.
<!--SR:!2026-06-04,4,270-->
What is a MAC protocol?::A medium access control protocol that decides when nodes may transmit on a shared medium.
What is a collision?::A situation where two or more nodes transmit at the same time on a shared medium and interfere.
What are the main classes of MAC protocols?::Channel partitioning, random access, and taking turns.
What is channel partitioning in MAC protocols?::Dividing channel resources by time, frequency, or code so nodes avoid collisions.
What is random access in MAC protocols?::Allowing nodes to transmit when needed and recover if collisions occur.
What is a taking-turns MAC protocol?::A protocol where nodes coordinate transmission opportunities to avoid uncontrolled collisions.
What is a MAC address?::A link-layer address used to identify an adapter on a local network.
How do MAC addresses differ from IP addresses?::MAC addresses are used for local link delivery, while IP addresses are used for network-layer routing across networks.
What is ARP?::Address Resolution Protocol, which maps an IP address on a local network to a MAC address.
What is an ARP table?::A cache of IP-to-MAC address mappings.
What is the broadcast MAC address used for?::Sending a frame to all adapters on the local network.
How does ARP find a MAC address?::A host broadcasts an ARP query, and the owner of the target IP replies with its MAC address.
When sending to another subnet, whose MAC address does a host need first?::The MAC address of the default gateway router's local interface.
What remains stable and what changes hop by hop during routed delivery?::The IP source and destination identify endpoints, while link-layer MAC addresses change on each hop.
What is Ethernet?::A dominant wired link-layer technology that defines framing and medium access behavior.
What is a collision domain?::A part of a network where simultaneous transmissions can collide.
How did switched Ethernet reduce collisions compared with shared bus Ethernet?::Switches create separate links so simultaneous transmissions can occur on different ports.
What is an Ethernet switch?::A link-layer device that forwards frames based on MAC addresses.
What is a switch table?::A table mapping MAC addresses to switch interfaces and aging information.
What is self-learning in a switch?::The switch records the source MAC address and incoming interface of frames it receives.
What is flooding in a switch?::Forwarding a frame out all ports except the incoming port when the destination is unknown or broadcast.
How does a switch decide whether to forward or filter a frame?::It checks whether the destination MAC is known and whether the output port differs from the input port.
Why are switches transparent to hosts?::Hosts send ordinary Ethernet frames without needing to know the switch exists.
How do switches differ from routers?::Switches forward frames using MAC addresses within a local network, while routers forward datagrams using IP addresses between networks.
What happens in a typical "day in the life" web access sequence?::A host gets configuration with DHCP, resolves local and remote names with ARP and DNS, opens a TCP connection, and exchanges HTTP messages.
Why is ARP needed before contacting a local router or host?::The sender needs a link-layer destination address to place in the Ethernet frame.
What are the main link-layer services?::Framing, link access, MAC addressing, reliable delivery, flow control, error detection, error correction, and duplex handling.
Why can link-level reliability be useful even when end-to-end reliability exists?::It can recover quickly on a noisy local link before losses propagate through the path.
Why is end-to-end reliability still needed if a link has reliable delivery?::Loss or corruption can still happen on other links or at later network points.
Why is error detection not perfectly reliable?::Some corruption patterns may not be caught, although stronger EDC fields reduce that risk.
How does even parity work?::The sender adds a bit so the total number of one bits is even.
<!--SR:!2026-06-04,4,270-->
How does two-dimensional parity locate a single-bit error?::One bad row parity and one bad column parity identify the flipped bit's intersection.
What are point-to-point link examples?::Host-to-switch links and point-to-point protocol links.
What are broadcast link examples?::Shared Ethernet, cable upstream links, WiFi, cellular, and satellite-style shared media.
What is TDMA?::A channel-partitioning MAC approach that divides access by time slots.
What is FDMA?::A channel-partitioning MAC approach that divides access by frequency bands.
What is CDMA?::A channel-partitioning MAC approach that divides access by code.
What is ALOHA-style random access?::A MAC approach where nodes transmit dynamically and recover from collisions.
What is CSMA-style random access?::A MAC approach where nodes listen before transmitting, with variants for collision detection or avoidance.
What is polling in taking-turns MAC?::A controller gives nodes permission to transmit in turn.
What is token passing in taking-turns MAC?::A special token grants the current holder permission to transmit.
Why is carrier sensing harder in wireless than in some wired networks?::Wireless senders may not hear all other senders or collisions because of signal range and interference issues.
What is the structure of an ARP table entry?::An IP address, a MAC address, and a time-to-live.
Why does ARP broadcast queries?::The sender does not yet know which local MAC address owns the target IP.
Why does ARP reply directly rather than by broadcast?::The responder learns the requester address from the query and can unicast the reply.
When sending to the same subnet, what destination MAC should the frame use?::The target host's MAC address.
<!--SR:!2026-06-04,4,270-->
When sending to a different subnet, what destination MAC should the first frame use?::The first-hop router's local MAC address.
What does a router do after receiving a frame for a different subnet?::It extracts the IP datagram, chooses the outgoing interface, and wraps the datagram in a new link-layer frame.
Why did switched Ethernet reduce collision domains?::Each switch port creates a separate link instead of placing all hosts on one shared bus.
<!--SR:!2026-06-04,4,270-->
Why can switches support simultaneous transmissions?::Frames on different input-output port pairs can be forwarded at the same time if output ports do not conflict.
When can two switch transmissions not both proceed at once?::When both need the same output link at the same time.
What does it mean that Ethernet switches are plug-and-play?::They learn forwarding information automatically without manual host configuration.
What does a switch record when any frame arrives?::The source MAC address, incoming interface, and timing information.
What does a switch do when the destination MAC is on the incoming interface?::It filters or drops the frame because forwarding it back is unnecessary.
What does a switch do when the destination MAC is known on another interface?::It forwards the frame only on that interface.
What does a switch do when the destination MAC is unknown?::It floods the frame out all other interfaces.
What table-building method do routers use compared with switches?::Routers use routing algorithms and protocols, while switches use self-learning from source MAC addresses.
What protocols are involved before a browser can send an HTTP request to a new web server?::DHCP for configuration, ARP for local MAC resolution, DNS for name resolution, and TCP for connection setup.

## Network Security

#flashcards/CSC3001F-networks/Network-Security

What is confidentiality?::Keeping data secret from unauthorized parties.
What is authentication?::Verifying the identity of a communicating party.
What is message integrity?::Ensuring a message was not altered in transit.
What is access and availability in security?::Ensuring authorized users can access services and resources when needed.
What is eavesdropping?::Secretly observing communication to learn information.
What is spoofing?::Pretending to be another entity by forging identity information.
What is hijacking?::Taking over an existing communication session or connection.
What is denial of service?::An attack that makes a service unavailable to legitimate users.
What is plaintext?::Original readable data before encryption.
What is ciphertext?::Encrypted data that should be unreadable without the proper key.
What is an encryption key?::A value used by an encryption algorithm to transform plaintext into ciphertext.
What is a decryption key?::A value used by a decryption algorithm to recover plaintext from ciphertext.
What is Kerckhoffs's principle?::A cryptosystem should remain secure even if the attacker knows the algorithm, as long as the key remains secret.
What is a block cipher?::An encryption algorithm that processes fixed-size blocks of data.
What is ECB mode?::A block-cipher mode where identical plaintext blocks encrypt to identical ciphertext blocks under the same key.
Why is ECB mode weak?::It reveals patterns when the same plaintext block appears more than once.
What is CBC mode?::A block-cipher mode where each plaintext block is combined with the previous ciphertext block before encryption.
What is an initialization vector?::A starting value used with modes such as CBC so identical messages do not encrypt the same way.
What is symmetric-key cryptography?::Cryptography where the sender and receiver use the same shared secret key.
What is DES?::An older symmetric block cipher that is no longer considered strong enough for modern security.
What is 3DES?::A strengthened variant of DES that applies DES multiple times but is slower and largely legacy.
What is AES?::A widely used modern symmetric block cipher.
What is public-key cryptography?::Cryptography using a public key and a private key with different roles.
What is RSA?::A public-key cryptosystem used for encryption, signatures, and key exchange in many protocols.
What is a session key?::A temporary symmetric key used to protect one communication session.
Why do protocols often use public-key cryptography to establish a symmetric session key?::Public-key operations solve key establishment, while symmetric encryption is faster for bulk data.
What is a nonce?::A value used once, often to prove freshness in authentication.
What is a replay attack?::An attack where a valid old message is resent to trick a protocol.
How does a nonce help prevent replay attacks?::It forces each authentication exchange to include fresh data that old messages cannot satisfy.
What is a digital signature?::A cryptographic value created with a private key that lets others verify origin and integrity using the public key.
What is non-repudiation?::Evidence that a sender cannot plausibly deny having created a signed message.
What is a hash function?::A function that maps input data to a fixed-size digest.
What is a message digest?::The fixed-size output of a hash function.
Why are hashes useful for signatures?::Signing a digest is more efficient and binds the signature to the message content.
What is a certificate authority?::A trusted entity that issues certificates binding identities to public keys.
What is a certificate?::A signed statement that binds an identity to a public key.
Why are certificates needed?::They let users trust that a public key belongs to the claimed entity.
What is TLS?::Transport Layer Security, a protocol that secures application traffic using encryption, authentication, and integrity protection.
What is a cipher suite?::A selected set of cryptographic algorithms used in a TLS connection.
What is Diffie-Hellman used for?::Establishing a shared secret over an insecure channel.
What does the TLS handshake establish?::Protocol parameters, authentication information, and shared keys for secure communication.
What is the benefit of TLS 1.3's streamlined handshake?::It reduces connection setup latency while improving security defaults.
What is TLS early data?::Application data sent during an abbreviated setup, with replay-risk tradeoffs.
What is a firewall?::A device or system that filters traffic according to a security policy.
Why are firewalls deployed?::To restrict unwanted traffic, enforce policy, and reduce exposure of internal systems.
What is a stateless packet filter?::A firewall that filters each packet independently using header fields and rules.
What is an ACL?::An access control list containing rules that permit or deny traffic.
What is a stateful packet filter?::A firewall that tracks connection state and filters packets based on both headers and flow context.
Why is stateful filtering more powerful than stateless filtering?::It can distinguish packets that belong to established legitimate flows from unsolicited traffic.
What is an IDS?::An Intrusion Detection System that monitors traffic or systems for suspicious activity.
What is deep packet inspection?::Examining packet payloads and higher-layer content, not just headers.
What is a DMZ?::A demilitarized network zone that exposes public-facing services while separating them from the internal network.
How do cryptography and network security mechanisms complement each other?::Cryptography protects data and identities, while mechanisms like firewalls and IDS control and monitor network access.
Why is availability considered a security goal?::A system that is confidential and correct still fails users if attackers can prevent legitimate access.
What notation describes encryption in the notes?::Applying a key to a message produces ciphertext, and applying the matching decryption key recovers the message.
What does public-key encryption to Bob use?::Bob's public key encrypts the data, and Bob's private key decrypts it.
What does a digital signature over a digest use?::The sender's private key signs the hash of the message.
Why is symmetric-key cryptography fast but operationally difficult?::It is efficient for bulk data, but the parties must already share a secret key securely.
Why is public-key cryptography useful but not usually used for all bulk data?::It solves key distribution and signatures but is slower than symmetric encryption.
How does CBC make identical plaintext blocks less revealing than ECB?::Each plaintext block is combined with the previous ciphertext block before encryption.
Why must the CBC first block use an initialization vector?::There is no previous ciphertext block for the first plaintext block.
What are the confidentiality steps in secure email?::Generate a session key, encrypt the message with it, encrypt the session key with the recipient's public key, and send both.
How does the receiver open a confidential secure email?::Use the private key to recover the session key, then use the session key to decrypt the message.
What are the integrity and authentication steps in secure email?::Hash the message, sign the digest with the sender's private key, and let the receiver verify using the sender's public key.
What three key roles appear when secure email provides confidentiality plus integrity?::The sender's private signing key, the recipient's public key for protecting the session key, and a fresh symmetric session key for the message.
What is PGP an example of?::A secure email system combining symmetric encryption, public-key encryption, hashes, and signatures.
Where is TLS placed relative to applications and transport?::It sits above transport and secures application traffic such as HTTPS.
What security properties does TLS provide?::Confidentiality, integrity, and authentication.
What TLS mechanism provides confidentiality?::Symmetric encryption after keys are established.
What TLS mechanism provides integrity?::Cryptographic hashing or authenticated encryption.
What TLS mechanism provides authentication?::Public-key certificates.
Why is SSL not the current protocol to rely on?::SSL is deprecated; modern secure deployments use TLS.
How does HTTP/3 relate to TLS?::HTTP/3 runs over QUIC on UDP, and QUIC incorporates TLS mechanisms.
What does a TLS cipher suite choose?::Algorithms for key establishment, encryption, integrity protection, and signatures.
What does a normal TLS 1.3 handshake do at a high level?::The client offers supported suites and key parameters, the server selects and authenticates, and both derive shared keys.
What is the replay risk of TLS early data?::An attacker may replay early application data, so it is safest only for idempotent requests.
What are the main firewall types in the notes?::Stateless packet filters, stateful packet filters, and application gateways.
What kinds of fields can stateless packet filters inspect?::IP addresses, TCP/UDP ports, ICMP type, and TCP SYN/ACK bits.
Why are ACL rules order-sensitive?::They are applied top to bottom, so an earlier matching rule can determine the decision before later rules are considered.
What is a common final ACL rule?::Deny all traffic not explicitly allowed earlier.
Why can stateless packet filtering admit nonsensical packets?::It does not remember whether a packet belongs to a legitimate active connection.
What connection events does a stateful firewall track?::TCP setup with SYN, teardown with FIN, active connection state, and inactivity timeouts.
What does a stateful firewall check before admitting a packet that claims to be part of a connection?::Whether the packet matches a valid active connection table entry.
What can an IDS detect beyond simple packet filtering?::Known attack payloads, patterns across sessions, port scans, network mapping, and denial-of-service behavior.
Where might IDS sensors be placed?::At network monitoring points such as a DMZ containing public-facing servers.
