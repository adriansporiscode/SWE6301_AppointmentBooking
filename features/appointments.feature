Feature: Resident appointment booking
  As a resident
  I want to book an available council appointment
  So that I can access council support

  Scenario: Book an available appointment
    Given appointment slot "SLOT-001" is available
    When resident "Alex Smith" books slot "SLOT-001"
    Then the booking should be confirmed
    And slot "SLOT-001" should be booked by "Alex Smith"


  Scenario: Reject booking an occupied slot
    Given appointment slot "SLOT-001" is booked by "Alex Smith"
    When resident "Jamie Brown" books slot "SLOT-001"
    Then the booking should be rejected with "Slot is unavailable"
    And slot "SLOT-001" should be booked by "Alex Smith"