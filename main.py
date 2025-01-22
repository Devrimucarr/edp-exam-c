from student import Student
from university import University
from event_queue import EventQueue

# Communication Queue instance
communication_queue = EventQueue()

# Create University and register event handlers
university = University("Best University", "Ankara, Turkey")
communication_queue.register_handler("application_sent", lambda event: university.handle_application_submission(event, communication_queue))
communication_queue.register_handler("application_reviewed", university.handle_application_review)

# Create Students and make applications
student1 = Student("Ali Veli", "ali.v@example.com")
student2 = Student("Ayse Yilmaz", "ayse.y@example.com")

student1.apply_to_university("Best University", communication_queue)
student2.apply_to_university("Best University", communication_queue)

# Process events in the queue
communication_queue.process_events()


















