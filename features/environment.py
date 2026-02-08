import logging
from calculator import Calculator

def before_all(context):
    logging.basicConfig(level=logging.INFO)
    context.logger = logging.getLogger("TestRunner")

def before_scenario(context, scenario):
    context.calc = Calculator()
    context.result = None
    context.error = None

def after_scenario(context, scenario):
    if context.failed:
        print(f"--- [FAILURE] Scenario Failed: {scenario.name} ---")

def after_all(context):
    print("--- Calculator Test Suite Complete ---")
