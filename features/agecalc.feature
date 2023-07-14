Feature: Calculate age given birthdate and evaldate

  Scenario: Exact month day
    Given birthdate "2000-01-01" and evaldate "2010-01-01"
     When invoked
     Then the result should be equal to "10"

  Scenario: Greater month day
    Given birthdate "2000-01-01" and evaldate "2010-02-01"
     When invoked
     Then the result should be equal to "10"

  Scenario: Smaller month day
    Given birthdate "2000-01-02" and evaldate "2010-01-01"
     When invoked
     Then the result should be equal to "9"

  Scenario: Evaldate < brithdate raise ValueError
    Given birthdate "2000-01-01" and evaldate "1999-01-01"
     When invoked
     Then it should raise ValueError
