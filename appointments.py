class AppointmentService:
    def __init__(self, available_slots):
        self.available_slots = set(available_slots)
        self.bookings = {}

    def book(self, slot_id, resident_name):
        if not isinstance(resident_name, str) or not resident_name.strip():
            return "Resident name is required"

        if slot_id not in self.available_slots:
            return "Slot is unavailable"

        self.bookings[slot_id] = resident_name.strip()
        self.available_slots.remove(slot_id)
        return "Booking confirmed"