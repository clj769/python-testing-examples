

Testing Strategy
================

## Table of Contents
1. [Developer's workflow](#workflow)
2. [Testing Styles](#testing-styles)
    1. [TDD](#tdd)
    2. [TLD](#tld)
4. [Testing Python Code](#testing-python-code)
    1. [Tools](#tools)
    2. [Gherkin](#gherkin)
    3. [Pylint Result](#pylint-result)
    4. [Examples](#examples)
        - [Pytest](#pytest)
        - [Behave](#behave)


## Developer's workflow <a id="workflow"></a>

Example workflow (using [feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)):

1. Update Master branch
2. Create a new branch for an issue
3. Write, test, and repeat
    - Write and run unit tests for any changes 
    - Run linters and fix code style before pushing
    - Push changes to central repository
4. Create a pull request
    - Code review, more tests to ensure code quality
    - Accept pull request and merge to Master

Many of these steps can be automated with CI/CD tools.

![Pipeline](https://raw.githubusercontent.com/peter-evolent/python-testing-examples/master/images/cicd-pipeline.png)


## Testing Styles <a id="testing-styles"></a>

There are many different testing styles, TDD, BDD, ATDD, TLD, etc. Whichever style you choose, just remember that testing your code is very important.

### Test-Driven Development <a id="tdd"></a>

TDD is a software development process that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the software is improved to pass the new tests, only. 

Three rules of TDD:

1. You are not allowed to write any production code unless it is to make a failing unit test pass.
2. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/peter-evolent/python-testing-examples/master/images/tdd-cycle.png">
</p>

### Test-Last Development <a id="tld"></a>

TLD is a traditional and most common approach of testing where testing is done only after implementation code has been written. 


## Testing Python code <a id="testing-python-code"></a>

For any python project, you will be using the tools below. In addition, writing scenarios with Gherkin syntax can be useful if you want describe features using natural language. Check [this](https://docs.python-guide.org/writing/tests/) document for details.

### Tools <a id="tools"></a>

- [Virtualenv](https://virtualenv.pypa.io/en/stable/): a tool to create isolated Python environments. This means that each project can have its own dependencies, regardless of what dependencies every other project has.

- [Pytest](https://docs.pytest.org/en/latest/): a test framework for python  that makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

- [Mock](https://docs.python.org/dev/library/unittest.mock.html): a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used. As of Python 3.3, it is available in the standard library.

- [Tox](https://tox.readthedocs.io/en/latest/): a tool for automating test environment management and testing against multiple interpreter configurations(Python2, Python3, ...).

- [Pylint](https://www.pylint.org/): a source-code, bug and quality checker for the Python programming language. It follows the style recommended by PEP 8, the Python style guide.

### Gherkin <a id="gherkin"></a>

Gherkin is a Business Readable, Domain Specific Language created especially for behavior descriptions. It gives you the ability to remove logic details from behavior tests.

Gherkin serves two purposes: serving as your project’s documentation and automated tests. Behat also has a bonus feature: it talks back to you using real, human language telling you what code you should write.


Example Feature
```gherkin
Feature: Google Homepage Search

Scenario: User sees the header
    Given I’m on the homepage
    Then I see the header

Scenario: User can search with “Google Search”
    Given I’m on the homepage
    When I type “random page” into the search field
    And I click the Google Search button
    Then I go to the random page search results

Scenario: User can search with “I’m Feeling Lucky”
    Given I’m on the homepage
    When I type “random page” into the search field
    And I click the I’m Feeling Lucky button
    Then I go to a random page
```

### Pylint Result <a id="pylint-result"></a>

```text
************* Module agecalc
agecalc.py:1:0: C0111: Missing module docstring (missing-docstring)
agecalc.py:18:-1: W0105: String statement has no effect (pointless-string-statement)


Report
======
7 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |8      |36.36 |8        |=          |
+----------+-------+------+---------+-----------+
|docstring |9      |40.91 |9        |=          |
+----------+-------+------+---------+-----------+
|comment   |0      |0.00  |0        |=          |
+----------+-------+------+---------+-----------+
|empty     |5      |22.73 |5        |=          |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |1      |1        |=          |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |1      |1        |=          |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+---------------------------+------------+
|message id                 |occurrences |
+===========================+============+
|pointless-string-statement |1           |
+---------------------------+------------+
|missing-docstring          |1           |
+---------------------------+------------+




------------------------------------------------------------------
Your code has been rated at 7.14/10 (previous run: 7.14/10, +0.00)
```

### Examples <a id="examples"></a>

This section will demonstrate how to to write tests for python code with different testing frameworks. For full examples, please check [this](https://github.com/peter-evolent/python-testing-examples) repository.

Consider a feature that calculate age given birthdate and evaldate, and we might write code look like this:

```python
# agecalc.py
from datetime import date


def calculate(birthdate: date, evaldate: date) -> int:
    '''Returns age given birthdate and evaldate

    Raises:
        ValueError: if evaldate < birthdate
    '''
    if evaldate < birthdate:
        raise ValueError('evaldate must be greater than or equal to birthdate')

    age = evaldate.year - birthdate.year

    ''' would add below lines to fix the failed test
    if (evaldate.month, evaldate.day) < (birthdate.month, birthdate.day):
        age -= 1
    '''

    return age
```

#### Pytest <a id="pytest"></a>

With Pytest, we can write a fucntion that covers a specific test case. For example,

```python
# test_agecalc.py
from datetime import date

import pytest
import agecalc


def test_calculate_exact_month_day():
    birthdate = date(2000, 1, 1)
    evaldate = date(2010, 1, 1)
    assert agecalc.calculate(birthdate, evaldate) == 10

def test_calculate_greater_month_day():
    birthdate = date(2000, 1, 1)
    evaldate = date(2010, 2, 1)
    assert agecalc.calculate(birthdate, evaldate) == 10

def test_calculate_smaller_month_day():
    birthdate = date(2000, 1, 2)
    evaldate = date(2010, 1, 1)
    assert agecalc.calculate(birthdate, evaldate) == 9

def test_calculate_present_date_less_than_birthdate_raises_valueerror():
    birthdate = date(2000, 1, 1)
    evaldate = date(1999, 1, 1)

    # exepct ValueError exception
    with pytest.raises(ValueError):
        agecalc.calculate(birthdate, evaldate)
```

This is a sample output that would result from the above tests.
![Pytest Result](https://raw.githubusercontent.com/peter-evolent/python-testing-examples/master/images/pytest-result.png)

#### Behave <a id="behave"></a>

With Behave, we use gherkin to define a feature and scenarios.

```gherkin
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
```

Behave parse the feature file and run corresponding step functions.
```python
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
    assert context.result == expected

@then('it should raise ValueError')
def step_impl(context):
    assert isinstance(context.e, ValueError)
```

Resuling output would be look like this:
![Behave Result](https://raw.githubusercontent.com/peter-evolent/python-testing-examples/master/images/behave-result.png)
