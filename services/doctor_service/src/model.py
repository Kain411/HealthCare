class Doctor:
    def __init__(self, id, username, gender, specialties, licenseNumber, phone, location):
        self.id = id
        self.username = username
        self.gender = gender
        self.specialties = specialties
        self.licenseNumber = licenseNumber
        self.phone = phone
        self.location = location

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "gender": self.gender,
            "specialties": self.specialties,
            "licenseNumber": self.licenseNumber,
            "phone": self.phone,
            "location": self.location
        }
    
    @staticmethod
    def from_dict(data):
        return Doctor(
            id=str(data.get('_id')),
            username=data.get('username'),
            gender=data.get('gender'),
            specialties=data.get('specialties'),
            licenseNumber=data.get('licenseNumber'),
            phone=data.get('phone'),
            location=data.get('location')
        )