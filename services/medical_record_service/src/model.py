class MedicalRecord:
    def __init__(self, id, patientID, doctorID, nurseID, note, result):
        self.id = id
        self.patientID = patientID
        self.doctorID = doctorID
        self.nurseID = nurseID
        self.note = note
        self.result = result

    def to_dict(self):
        return {
            "id": self.id,
            "patientID": self.patientID, 
            "doctorID": self.doctorID,
            "nurseID": self.nurseID,
            "note": self.note,
            "result": self.result
        }
    
    @staticmethod
    def from_dict(data):
        return MedicalRecord(
            id=str(data.get('_id')),
            patientID=data.get('patientID'),
            doctorID=data.get('doctorID'),
            nurseID=data.get('nurseID'),
            note=data.get('note'),
            result=data.get('result')
        )