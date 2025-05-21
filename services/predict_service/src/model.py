class Predict:
    def __init__(self, age, gender, fever, chestPain, breath, cough, dizzy, bloodPressure, heartRate):
        self.age = self.fixAge(int(age))
        self.gender = gender
        self.fever = self.fix(fever)
        self.chestPain =self.fix(chestPain)
        self.breath = self.fix(breath)
        self.cough = self.fix(cough)
        self.dizzy = self.fix(dizzy)
        self.bloodPressure = self.fixBloodPressure(str(bloodPressure))
        self.heartRate = self.fixHeartRate(int(heartRate))

    def fix(self, str):
        return 0 if str=="Không" else 1
    
    def fixAge(self, num):
        if num>=1 and num<20: return "0-19"
        elif num>=20 and num<50: return "20-49"
        return ">=50"
    
    def fixBloodPressure(self, str): 
        systolic, diastolic = map(int, str.split('/'))
        if systolic < 90 and diastolic < 60:
            return "Thấp"
        elif systolic >= 130 or diastolic >= 80:
            return "Cao"
        else:
            return "Trung bình"
        
    def fixHeartRate(self, rate):
        if rate<=70: return "Thấp"
        elif rate>=120: return "Cao"
        return "Trung bình"
    
    def getData(self):
        lst = {
            "Tuổi": self.age,
            "Giới tính": self.gender,
            "Sốt": self.fever,
            "Đau ngực": self.chestPain,
            "Khó thở": self.breath,
            "Ho": self.cough,
            "Chóng mặt": self.dizzy,
            "Huyết áp": self.bloodPressure,
            "Nhịp tim": self.heartRate
        }
        return lst
