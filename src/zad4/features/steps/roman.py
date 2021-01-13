from behave import *

use_step_matcher("re")


@given("user inputs the number and his guess")
def step_impl(context):
    context.number = int(context.text.split(",")[0])
    context.user_guess = context.text.split(",")[1]


@given("user inputs the number and his guess with wrong type")
def step_impl(context):
    context.number = int(context.text.split(",")[0])
    context.user_guess = int(context.text.split(",")[1])

@given("user inputs the number with wrong type and his guess with wrong type")
def step_impl(context):
    context.number = context.text.split(",")[0]
    context.user_guess = int(context.text.split(",")[1])

@when("we run the converter")
def step_impl(context):
    try:
        context.res = context.roman.check_guess(context.number, context.user_guess)
    except TypeError as e:
        context.e = e 

@then("the result is True")
def step_impl(context):
    assert context.res == True
    assert "e" not in context

@then("the result is False")
def step_impl(context):
    assert context.res == False
    assert "e" not in context


@then("the app raises an error")
def step_impl(context):
    assert "res" not in context
    assert "e" in context
    assert isinstance(context.e, TypeError)
