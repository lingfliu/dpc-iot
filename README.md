# dpc-iot
Declarative protocol connectivity of IoT

# Terminologies
## Components of IoT
1. Node: a device with application connectivity and protocol regulations
2. Gateway: a device connect the nodes, extract and handle the data in higher-lever abstraction
3. Declartor: a unit hold the protocol, map the data and process

## Components of a declarative protocol
1. Protocol: the root of the protocol
2. Message
3. Contents: binaries blocks of a message
4. Mark: content for identification and classification
5. Data: content of data
6. Process: time sequence of messages to express an interaction between the node and gateway
7. Stage: equivalents of messages in a process
5. Filter: the pre- / post- processing of the message
6. Map: a type-data mapping

# Design principles
1. Loop-less
2. No ambigous declaration
3. Structured declaration

# Implicit declaration
## Implicit message declaration
Example:
```
message
    mark value='...'
    data offset='...'
    mark value='...' offset='...'
```
## Implicit process declaration

```
process
    message model='...'
    message model='...'
```
