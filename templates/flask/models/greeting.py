# models/greeting.py
class Greeting:
    def __init__(self, message, greeting_type, recipient=None):
        self.message = message
        self.greeting_type = greeting_type
        self.recipient = recipient
    
    def to_dict(self):
        return {
            "message": self.message,
            "greeting_type": self.greeting_type,
            "recipient": self.recipient
        }