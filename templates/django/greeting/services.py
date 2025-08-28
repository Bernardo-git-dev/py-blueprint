# greeting/services.py

class GreetingService:
    def create_greeting(self, name):
        return {
            "message": f"Hello {name} from Django!",
            "greeting_type": "personalized"
        }