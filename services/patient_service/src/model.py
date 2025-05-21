class Patient:
    def __init__(self, id, username, gender, insuranceNumber, bloodType, phone, location):
        self.id = id
        self.username = username
        self.gender = gender
        self.insuranceNumber = insuranceNumber
        self.bloodType = bloodType
        self.phone = phone
        self.location = location

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "gender": self.gender,
            "insuranceNumber": self.insuranceNumber,
            "bloodType": self.bloodType,
            "phone": self.phone,
            "location": self.location
        }
    
    @staticmethod
    def from_dict(data):
        return Patient(
            id=str(data.get('_id')),
            username=data.get('username'),
            gender=data.get('gender'),
            insuranceNumber=data.get('insuranceNumber'),
            bloodType=data.get('bloodType'),
            phone=data.get('phone'),
            location=data.get('location')
        )