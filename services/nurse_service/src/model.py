class Nurse:
    def __init__(self, id, username, gender, shift, department, phone, location):
        self.id = id
        self.username = username
        self.gender = gender
        self.shift = shift
        self.department = department
        self.phone = phone
        self.location = location

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "gender": self.gender,
            "shift": self.shift,
            "department": self.department,
            "phone": self.phone,
            "location": self.location
        }
    
    @staticmethod
    def from_dict(data):
        return Nurse(
            id=str(data.get('_id')),
            username=data.get('username'),
            gender=data.get('gender'),
            shift=data.get('shift'),
            department=data.get('department'),
            phone=data.get('phone'),
            location=data.get('location')
        )