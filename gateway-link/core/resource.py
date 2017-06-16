import time

# All resources are converted into life cycles
class ConnectivityResource:
    def __init__(self, msgList):
        self.life = time.time()
        self.process = []
        for msg in msgList:
            self.process.append(msg)

        #p2p requires mapping, cluster requires cluster mapping, gateway requires conversion
        self.type = "gateway, p2p, cluster"

    def consume(self, msg):
        msgCurrent = self.process.pop(0)
        if msgCurrent.require(msg) and msgCurrent.timeOut < time.time() - self.life:
            self.life = time.time()
            msgCurrent.response()
