# Lola
A  link oriented application connectivity declaration for node connections

# Terminologies
## Components of IoT
1. Node: connectable devices with protocol declaration
2. Declarator: connectivity resource holder and mapper

## Terms and components
1. AC-Proto: application connectivity protocol set
2. Message：
3. Content: a container of the message
4. Mark: a content container to hold data and marks
5. Data: a content container to hold data
6. Process: message exchange specification
7. Stage: equivalents of messages in a process
5. Filter: the pre- / post- processing of the message
6. Map: model / mark / data mapping use $id or $type

# Design rules
1. Identifiable
2. Iterable and structural
3. No circular and recursive reference

# Implementation Example (pseudo-markups)
## Implicit declaration
## Branching
## Nested declaration
## 
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
