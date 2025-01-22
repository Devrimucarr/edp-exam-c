from event import ApplicationSentEvent

class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def apply_to_university(self, university_name, communication_queue):
        event = ApplicationSentEvent(self.name, university_name)
        communication_queue.emit(event)