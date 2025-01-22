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