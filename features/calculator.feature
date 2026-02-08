Feature: Basic Four-Function Calculator
    I want to test the foundational arithmetic functions (+, -, *, /) of the calculator to ensure that users can reliably perform everyday calculations without errors.

  Scenario Outline: Perform arithmetic operations
    Given the calculator is initialized
    When I perform "<operation>" with <input_a> and <input_b>
    Then the result should be "<expected_result>"

    Examples:
      | operation | input_a     | input_b     | expected_result       |
      | add       | 5           | 2.5         | 7.5                   |
      | subtract  | 100         | 0.01        | 99.99                 |
      | multiply  | -4          | 2.5         | -10.0                 |
      | divide    | 10          | 4           | 2.5                   |
      | divide    | 5           | 0           | Cannot divide by zero |
      | multiply  | 999         | 0           | 0.0                   |
      | add       | 1000000000  | 1000000000  | 2000000000.0          |

  Scenario: Chaining operations (TC-08)
    Given the calculator is initialized
    When I add 5 and 5
    And I add the result with 5
    Then the result should be "15.0"

  Scenario: Multiple Decimal Points (TC-09)
    Given the calculator is initialized
    When I enter "2.5.5"
    Then the system should return "Invalid Input"
