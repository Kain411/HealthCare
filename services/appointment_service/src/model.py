class Appointment:
    def __init__(self, id, doctorID, time, day):
        self.id = id
        self.doctorID = doctorID
        self.time = time
        self.day = day

    def to_dict(self):
        return {
            "id": self.id,
            "doctorID": self.doctorID,
            "time": self.time,
            "day": self.day
        }
    
    @staticmethod
    def from_dict(data):
        return Appointment(
            id=str(data.get('_id')),
            doctorID=data.get('doctorID'),
            time=data.get('time'),
            day=data.get('day')
        )
    
class AppointmentDetails:
    def __init__(self, id, appointmentID, patientID):
        self.id = id
        self.appointmentID = appointmentID
        self.patientID = patientID

    def to_dict(self):
        return {
            "id": self.id,
            "appointmentID": self.appointmentID,
            "patientID": self.patientID
        }
    
    @staticmethod
    def from_dict(data):
        return AppointmentDetails(
            id=str(data.get('_id')),
            appointmentID=data.get('appointmentID'),
            patientID=data.get('patientID')
        )