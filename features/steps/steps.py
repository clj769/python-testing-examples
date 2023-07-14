from behave import given, then, when
import agecalc


@given('birthdate "{birthdate:ti}" and evaldate "{evaldate:ti}"')
def step_impl(context, birthdate, evaldate):
    context.birthdate = birthdate.date()
    context.evaldate = evaldate.date()

@when('invoked')
def step_impl(context):
    try:
        context.result = agecalc.calculate(context.birthdate, context.evaldate)
    except Exception as e:
        context.e = e

@then('the result should be equal to "{expected:d}"')
def step_impl(context, expected):
    print(context.result,expected)
    assert context.result == expected

@then('it should raise ValueError')
def step_impl(context):
    assert isinstance(context.e, ValueError)
