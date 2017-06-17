class Protocol:
    def __init__(self):
        self.msgSet = ()
        self.processSet = ()
        pass

    def fromXml(self, str):
        pass

    def fromXmlFile(self, file):
        pass

    def findProcess(self, entryMsg):
        pass

    def findMsg(self, msg):
        pass

class Message:
    def __init__(self):
        self.cont = []

    def append(self, content):
        self.cont.append(content)

    def construct(self, type):
        pass

class Process:
    pass
class Model:
    def __init__(self):
        pass

class Transform:
    def __init__(self, transform):
        self.transform = transform

class Mapper:
    def __init__(self):
        pass

class Content:
    pass

class Data(Content):
    pass

class Mark(Content):
    pass

class Filter(Content):
    pass

# parse message from bytebuffer or blockbuffer

def parseMessage(buffer, protocol):
    contents, msgType = buffer.matchAndPop(protocol.getMsgIdentification())
    if len(contents) > 0 and protocol.validMsg(msgType):
        return buildMsg(bytes, msgType, protocol)

def buildMsg(contents, msgType, protocol):
    msg = Message()
    cnt = 0
    for content in contents:
        msg.contents.append(content)
    msg.type = msgType
    msg.protocol = protocol
