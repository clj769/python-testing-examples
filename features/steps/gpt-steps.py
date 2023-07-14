# from behave import given, when, then
# from datetime import datetime
# from dateutil.relativedelta import relativedelta
#
#
# def calculate_age(birthdate: str, evaldate: str) -> int:
#     birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
#     evaldate = datetime.strptime(evaldate, '%Y-%m-%d')
#
#     if evaldate < birthdate:
#         raise ValueError("Evaldate cannot be earlier than birthdate")
#
#     return relativedelta(evaldate, birthdate).years
#
#
# @given('birthdate "{birthdate}" and evaldate "{evaldate}"')
# def step_given_birthdate_and_evaldate(context, birthdate, evaldate):
#     context.birthdate = birthdate
#     context.evaldate = evaldate
#
#
# @when('invoked')
# def step_when_invoked(context):
#     try:
#         context.age = calculate_age(context.birthdate, context.evaldate)
#         context.error = None
#     except ValueError as e:
#         context.error = e
#
#
# @then('the result should be equal to "{expected_age}"')
# def step_then_result_should_be_equal_to(context, expected_age):
#     assert context.age == int(expected_age), \
#         f'Expected {expected_age}, but got {context.age}'
#
#
# @then('it should raise ValueError')
# def step_then_it_should_raise_value_error(context):
#     assert isinstance(context.error, ValueError), \
#         'Expected ValueError, but got none'
