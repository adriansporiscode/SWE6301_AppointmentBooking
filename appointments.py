class AppointmentService:
    def __init__(self, available_slots):
        self.available_slots = set(available_slots)
        self.bookings = {}

    def book(self, slot_id, resident_name):
        raise NotImplementedError("Booking is not implemented yet")