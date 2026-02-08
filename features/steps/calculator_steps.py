from behave import given, when, then
from calculator import Calculator
import logging

@given(u'the calculator is initialized')
def step_impl(context):
    context.calc = Calculator()
    context.result = None
    context.error = None

@when(u'I perform "{operation}" with {input_a} and {input_b}')
def step_impl(context, operation, input_a, input_b):
    val_a = float(input_a)
    val_b = float(input_b)
    try:
        if operation == "add":
            context.result = context.calc.add(val_a, val_b)
        elif operation == "subtract":
            context.result = context.calc.subtract(val_a, val_b)
        elif operation == "multiply":
            context.result = context.calc.multiply(val_a, val_b)
        elif operation == "divide":
            context.result = context.calc.divide(val_a, val_b)
    except Exception as e:
        context.error = str(e)

@when(u'I add {a} and {b}')
def step_add(context, a, b):
    context.result = context.calc.add(float(a), float(b))

@when(u'I add the result with {val}')
def step_chain(context, val):
    context.result = context.calc.add(context.result, float(val))

@when(u'I enter "{val_str}"')
def step_input_val(context, val_str):
    context.error = context.calc.validate_input(val_str)

@then(u'the result should be "{expected_result}"')
def step_impl(context, expected_result):
    if context.error:
        assert str(context.error) == str(expected_result), \
            f"Expected error '{expected_result}', but got '{context.error}'"
    else:
        assert float(context.result) == float(expected_result), \
            f"Expected {expected_result}, but got {context.result}"

@then(u'the system should return "{expected_msg}"')
def step_error_check(context, expected_msg):
    assert context.error == expected_msg
