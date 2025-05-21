class Prescription:
    def __init__(self, id, doctorID, patientID):
        self.id = id
        self.doctorID = doctorID
        self.patientID = patientID

    def to_dict(self):
        return {
            "id": self.id,
            "doctorID": self.doctorID,
            "patientID": self.patientID,
        }
    
    @staticmethod
    def from_dict(data):
        return Prescription(
            id=str(data.get('_id')),
            doctorID=data.get('doctorID'),
            patientID=data.get('patientID')
        )
    
class PrescriptionDetails:
    def __init__(self, id, prescriptionID, medicineID, quantity):
        self.id = id
        self.prescriptionID = prescriptionID
        self.medicineID = medicineID
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "prescriptionID": self.prescriptionID,
            "medicineID": self.medicineID,
            "quantity": self.quantity
        }
    
    @staticmethod
    def from_dict(data):
        return PrescriptionDetails(
            id=str(data.get('_id')),
            prescriptionID=data.get('prescriptionID'),
            medicineID=data.get('medicineID'),
            quantity=data.get('quantity')
        )