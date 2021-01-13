from behave import *

use_step_matcher("re")


@given("strand1 is ABB")
def step_impl(context):
    context.strand1 = "ABB"

@given("strand1 is XYZ")
def step_impl(context):
    context.strand1 = "XYZ"

@given("strand1 is ABCDEFGHRETR")
def step_impl(context):
    context.strand1 = "ABCDEFGHRETR"

@given("strand1 is ATGATA")
def step_impl(context):
    context.strand1 = "ATGATA"

@given("strand2 is ABB")
def step_impl(context):
    context.strand2 = "ABB"

@given("strand2 is ABC")
def step_impl(context):
    context.strand2 = "ABC"

@given("strand2 is ABCDEFG")
def step_impl(context):
    context.strand2 = "ABCDEFG"

@given("strand2 is AGTTTA")
def step_impl(context):
    context.strand2 = "AGTTTA"

@given("strand1 is empty")
def step_impl(context):
    context.strand1 = ""


@given("strand2 is empty")
def step_impl(context):
    context.strand2 = ""

@when("we calculate the distance")
def step_impl(context):
    try:
        context.result = context.hamming.distance(context.strand1, context.strand2)
    except ValueError as exception:
        context.exception = exception

@then("the result is 0")
def step_impl(context):
    assert context.result == 0

@then("the result is 1")
def step_impl(context):
    assert context.result == 1

@then("the result is 3")
def step_impl(context):
    assert context.result == 3


@then("the program raises an error")
def step_impl(context):
    assert isinstance(context.exception, ValueError)

