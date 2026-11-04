# Resident Appointment Booking

SWE6301 Agile Programming - Assignment 1

## Purpose
A small Python prototype for booking appointments with a local authority.

## User story
As a resident, I want to book an available appointment so that I can access council support at a suitable time.

## Acceptance criteria
1. A resident can book an available appointment slot.
2. An already-booked slot cannot be booked again.
3. A booking with a blank resident name is rejected.
4. A rejected booking does not change existing bookings.

## Scope
The prototype will use fictional data and store bookings in memory.
It will not include a database, website or login system.

## Testing
Expected behaviour will be described using Given-When-Then scenarios
and tested using the Python behave framework.

## Installation and running tests

Tested with Python 3.13.3 and behave 1.3.3.

Open Windows Command Prompt in the project folder.

Create a virtual environment:
```cmd
py -m venv .venv
```

Activate it:
```cmd
.venv\Scripts\activate
```

Install the dependencies:
```cmd
python -m pip install -r requirements.txt
```

Run the automated tests:
```cmd
python -m behave --no-color
```

Expected result: 3 scenarios passed and 13 steps passed.

## Development evidence

The evidence folder contains test outputs recorded during development.
Earlier outputs show errors and a validation failure before the
corresponding functionality was implemented or corrected.

The final output is recorded in:
evidence/06_all_scenarios_pass.txt

Git commits document the progression from scenarios and failing tests
to working implementations.

## Limitations

Bookings are stored in memory and are lost when the service stops.
The prototype has no database, authentication or user interface.
Concurrent booking requests are not handled.
The tests cover the three documented scenarios.