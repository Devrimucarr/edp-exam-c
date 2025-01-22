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
