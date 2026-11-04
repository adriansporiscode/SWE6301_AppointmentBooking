from behave import given, when, then
from appointments import AppointmentService


@given('appointment slot "{slot_id}" is available')
def step_available_slot(context, slot_id):
    context.service = AppointmentService([slot_id])


@when('resident "{name}" books slot "{slot_id}"')
def step_book_slot(context, name, slot_id):
    context.result = context.service.book(slot_id, name)


@then('the booking should be confirmed')
def step_booking_confirmed(context):
    assert context.result == "Booking confirmed", (
        f"Unexpected result: {context.result}"
    )


@then('slot "{slot_id}" should be booked by "{name}"')
def step_check_booking(context, slot_id, name):
    assert context.service.bookings.get(slot_id) == name

@given('appointment slot "{slot_id}" is booked by "{name}"')
def step_occupied_slot(context, slot_id, name):
    context.service = AppointmentService([slot_id])
    context.service.book(slot_id, name)


@then('the booking should be rejected with "{message}"')
def step_booking_rejected(context, message):
    assert context.result == message, (
        f"Expected: {message}, received: {context.result}"
    )