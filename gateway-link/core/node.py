import uuid

class Node:
    def __init__(self):
        self.uid = uuid.uuid4()
        self.conn = ""

