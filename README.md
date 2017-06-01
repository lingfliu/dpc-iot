# Deplexio
DEclarative Protocol LEXIOlogy for internet of things

# Terminologies
## Components of IoT
1. Node: a device with application connectivity and protocol regulations
2. Gateway: a device connect the nodes, extract and handle the data in higher-lever abstraction
3. Declarator: a unit hold the protocol, map the data and process

## Components of a declarative protocol
1. Protocol: 
2. Message：
3. Contents: blocks of a message
4. Mark: 
5. Data: 
6. Process: message exchange specification
7. Stage: equivalents of messages in a process
5. Filter: the pre- / post- processing of the message
6. Map: a type-data mapping

# Design principles
1. No ambigous declaration
2. Structured declaration
3. Tree-structure, loop-free

# Implementation Example (pseudo-markups)
## Implicit declaration
### Message and process
```
model id='msg-model'
    head 
        mark name='prefix' value='\0xAA\0xDD\0xAA\0xDD'
        mark name='version' model='%uint' value='1' length='2byte'
        data name='id' length='16byte'
        data name='msg-type' model='%uint' length='4byte'
        data name='payload-length' model='%uint' length='4byte' range='[0,)'
    payload length='var'
        data name='list-length' length='2byte'
        list name='status-list' length='var' max-length='500byte'
            data name='item' model='%float' length='4byte'        
            
model id='msg-ack' model='msg-model'    
    payload length='4byte'
        data name='ack' length='4byte'

message model='%msg-model'
    payload
        data name='time-recv' model='%date' length='8byte'

model id='process-model'
    message model='msg-model' require='id msg-type payload'
    message model='msg-model' require='ack'
process id='login'
    message model='msg-model' require='id key'
    message model='msg-model' require='ack' timeout='5second'
```

### Implicit message declaration
Example:
```
message
    mark value='...'
    data offset='...'
    mark value='...'
    data offset='...'
```
### Implicit process declaration

```
process
    message model='...' require='key id'
    message model='...' require='token'    
```

### Nested declaration
```
message
    data model='msg-model' length='var' max-length='256byte'    
```
