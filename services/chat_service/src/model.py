class Chat:
    def __init__(self, id, patientID, type, content, time):
        self.id = id
        self.patienID = patientID
        self.type = type
        self.content = content
        self.time = time

    def to_dict(self):
        return {
            "id": self.id,
            "patientID": self.patienID,
            "type": self.type,
            "content": self.content,
            "time": self.time
        }
    
    @staticmethod
    def from_dict(data):
        return Chat(
            id=str(data.get('_id')),
            patientID=data.get('patientID'),
            type=data.get('type'),
            content=data.get('content'),
            time=data.get('time')
        )