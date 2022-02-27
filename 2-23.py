class Phone():
    def __init__(self, phone_number) :
        self.phone_number = phone_number
        self.text_messages = []

    def place_call(number_to_call):
        pass

    def place_text(number_to_text, message_to_send):
        pass

    def save_text(message_to_save):
        pass

    def get_texts():
        pass

    def get_number():
        pass



class CameraPhone(Phone):
    def __init__(self, pictures):
        self.pictures = []
        super().__init__()

    def take_picture(picture_name):
        pass

phone = Phone(18009296890,"hi")
camphone = CameraPhone("friday")

print(phone.phone_number)