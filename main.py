class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload


class ApplicationSentEvent(Event):
    def __init__(self, student_name, university_name):
        super().__init__("application_sent", {"student_name": student_name, "university_name": university_name})


class ApplicationReviewedEvent(Event):
    def __init__(self, student_name, university_name, is_accepted):
        super().__init__("application_reviewed", {
            "student_name": student_name,
            "university_name": university_name,
            "is_accepted": is_accepted
        })


class EventQueue:
    def __init__(self):
        self.queue = []
        self.handlers = {}

    def emit(self, event):
        self.queue.append(event)
        print(f"Event '{event.name}' emitted!")

    def register_handler(self, event_name, handler):
        self.handlers[event_name] = handler

    def process_events(self):
        while self.queue:
            event = self.queue.pop(0)
            if event.name in self.handlers:
                handler = self.handlers[event.name]
                handler(event)
            else:
                print(f"No handler registered for event: {event.name}")


communication_queue = EventQueue()


class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def apply_to_university(self, university_name):
        event = ApplicationSentEvent(self.name, university_name)
        communication_queue.emit(event)


class University:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def handle_application_submission(self, event):
        print(f"Processing application from {event.payload['student_name']} to {event.payload['university_name']}.")
        # For demonstration purposes, accept all applications
        is_accepted = True
        review_event = ApplicationReviewedEvent(event.payload['student_name'], event.payload['university_name'], is_accepted)
        communication_queue.emit(review_event)

    def handle_application_review(self, event):
        status = "accepted" if event.payload['is_accepted'] else "rejected"
        print(f"Application from {event.payload['student_name']} to {event.payload['university_name']} is {status}.")


# Create instances
university = University("Best University", "Ankara, Turkey")
communication_queue.register_handler("application_sent", university.handle_application_submission)
communication_queue.register_handler("application_reviewed", university.handle_application_review)

student1 = Student("Ali Veli", "ali.v@example.com")
student2 = Student("Ayse Yilmaz", "ayse.y@example.com")

# Students apply to the university
student1.apply_to_university("Best University")
student2.apply_to_university("Best University")

# Process events in the queue
communication_queue.process_events()


















