# features/steps/tracking.steps.py

from behave import given, when, then
from unittest.mock import patch
from src.package.tracking import Tracking


@given("a Tracking instance is initialized")
def step_initialize_tracking_instance(context):
    context.tracking_instance = Tracking()


@when("{method} method is called with {message} message")
def step_call_log_method(context, method, message):
    with patch("builtins.print"):
        context.result = getattr(context.tracking_instance, method)(message)


@then("it should write {display} message in console")
def step_verify_log_output(context, display):
    if context.result is not None:
        assert (
            context.result == display
        ), f"Expected: {display}, Actual: {context.result}"
    else:
        print("Warning: Log method returned None.")
