class Medicine:
    def __init__(self, id, genericName, brandName, dosageForm, strength, route):
        self.id = id
        self.genericName = genericName
        self.brandName = brandName
        self.dosageForm = dosageForm
        self.strength = strength
        self.route = route
    
    # genericName: Tên hoạt chất
    # brandName: Tên thương mại
    # dosageForm: Dạng bào chế
    # strength: Hàm lượng
    # route: Đường dùng

    def to_dict(self):
        return {
            "id": self.id,
            "genericName": self.genericName,
            "brandName": self.brandName,
            "dosageForm": self.dosageForm,
            "strength": self.strength,
            "route": self.route
        }
    
    @staticmethod
    def from_dict(data):
        return Medicine(
            id=str(data.get('_id')),
            genericName=data.get('genericName'),
            brandName=data.get('brandName'),
            dosageForm=data.get('dosageForm'),
            strength=data.get('strength'),
            route=data.get('route')
        )