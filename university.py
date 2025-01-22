from student import Student
from university import University
from event_queue import EventQueue

# Communication Queue instance
communication_queue = EventQueue()


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
