import random

# Thank you ChatGPT!!
class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
    
    def generate_message(self):
        #create lists with upper and lower limits
        user_ids = list(range(1, 101))
        velocity_range = list(range(30, 55))
        temperature_range = list(range(15, 25))
        #choose a random value from the lists
        random_user_id = random.choice(user_ids)
        velocity_message = random.choice(velocity_range)
        temperature_message = random.choice(temperature_range)
        #return message
        return {
            'bus_id': random_user_id,
            'velocity': velocity_message,
            'temperature': temperature_message
        }