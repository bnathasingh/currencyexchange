"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Brandon Nathasingh bn243 Taerim Eom te89
Date:   09/24/19
"""
import introcs
import a1

def testA():
    """
    Test procedure for Part A
    """
    #testing before_space for string with one space
    result = a1.before_space("4.502 Euros")
    introcs.assert_equals("4.502", result)
    #testing before_space for string with two spaces
    result = a1.before_space("Brandon and Taerim")
    introcs.assert_equals("Brandon", result)
    #testing before_space for string with space at front
    result = a1.before_space(" car")
    introcs.assert_equals("", result)
    #testing before_space for string with multiple spaces together
    result = a1.before_space("Taerim   and")
    introcs.assert_equals("Taerim", result)
    #testing after_space for one space
    result = a1.after_space("4.502 Euros")
    introcs.assert_equals("Euros", result)
    #testing after_space for two spaces
    result = a1.after_space("Brandon and Taerim")
    introcs.assert_equals("and Taerim", result)
    #testing after_space for space at front
    result = a1.after_space(" car")
    introcs.assert_equals("car", result)
    #testing after_space for multiple spaces together
    result = a1.after_space("Taerim  and")
    introcs.assert_equals(" and", result)
    #testing after_space for space at end
    result = a1.after_space("Taerim ")
    introcs.assert_equals("", result)


def testB():
    """
    Test procedure for Part B
    """
    #testing first_inside_quotes for json
    result = a1.first_inside_quotes('{ "ok":true, "lhs":"2.5 United States Dollars", '
    '"rhs":"64.375 Cuban Pesos", "err":"" }')
    introcs.assert_equals('ok', result)
    #testing first_inside_quotes for no quotes
    result = a1.first_inside_quotes('Quotes "" quotes')
    introcs.assert_equals('', result)
    #testing first_inside_quotes for two quotes
    result = a1.first_inside_quotes('two "of" these "quotes"')
    introcs.assert_equals('of', result)
    #testing first_inside_quotes for one quote in a string
    result = a1.first_inside_quotes('""')
    introcs.assert_equals('', result)
    #testing first_inside_quotes for two quotes
    result = a1.first_inside_quotes(' "" "" ')
    introcs.assert_equals('', result)
    #testing first_inside_quotes for a single quote in a double quote
    result = a1.first_inside_quotes(' " '' "')
    introcs.assert_equals('  ', result)
    #testing first_inside_quotes whole quote in quotes
    result = a1.first_inside_quotes('"this entire string"')
    introcs.assert_equals('this entire string', result)
    #testing get get_lhs
    result = a1.get_lhs('{ "ok":true, "lhs":"2.5 United States Dollars", '
    '"rhs":"64.375 Cuban Pesos", "err":"" }')
    introcs.assert_equals('2.5 United States Dollars', result)
    #testing get_lhs on json with error
    result = a1.get_lhs('{ "ok":false, "lhs":"", "rhs":"", '
    '"err":"Currency amount is invalid." }')
    introcs.assert_equals('', result)
    #testing get_lhs with longer json
    result = a1.get_lhs('{ "ok":true, "lhs":"2.5 Trinidad and Tobago Dollars", '
    '"rhs":"77.304437834842 Guyanaese Dollars", "err":"" }')
    introcs.assert_equals('2.5 Trinidad and Tobago Dollars', result)
    #testing get_lhs
    result = a1.get_lhs('{ "ok":true, "lhs":"1 Bitcoin", '
    '"rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals('1 Bitcoin', result)
    #testing get_rhs with regular json
    result = a1.get_rhs('{ "ok":true, "lhs":"1 Bitcoin", '
    '"rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals('9916.0137 Euros', result)
    #testing get_rhs with json with an error
    result = a1.get_rhs('{ "ok":false, "lhs":"", "rhs":"", '
    '"err":"Currency amount is invalid." }')
    introcs.assert_equals('', result)
    #testing get_rhs with longer json
    result = a1.get_rhs('{ "ok":true, "lhs":"2.5 Trinidad and Tobago Dollars", '
    '"rhs":"77.304437834842 Guyanaese Dollars", "err":"" }')
    introcs.assert_equals('77.304437834842 Guyanaese Dollars', result)
    #testing has_error with an error
    result = a1.has_error('{ "ok":false, "lhs":"", "rhs":"", '
    '"err":"Currency amount is invalid." }')
    introcs.assert_equals(True, result)
    #testing has_error without an error
    result = a1.has_error('{ "ok":true, "lhs":"1 Bitcoin", '
    '"rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals(False, result)


def testC():
    """
    Test procedure for Part C
    """
    #testing currency_response for case we were provided
    result = a1.currency_response('USD', 'CUP', 2.5)
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 United States Dollars", '
    '"rhs":"64.375 Cuban Pesos", "err":"" }', result)
    #test currency_response for longer json
    result = a1.currency_response('TTD', 'JMD', 2.5)
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 Trinidad and Tobago Dollars", '
    '"rhs":"48.690190282653 Jamaican Dollars", "err":"" }', result)
    #testing currency_response for invalid currency code
    result = a1.currency_response('ABC', 'DEF', 2.5)
    introcs.assert_equals('{ "ok":false, "lhs":"", "rhs":"", '
    '"err":"Source currency code is invalid." }', result)
    #testing currency_response for invalid amt input
    result = a1.currency_response('TTD', 'JMD', '')
    introcs.assert_equals('{ "ok":false, "lhs":"", "rhs":"", '
    '"err":"Currency amount is invalid." }', result)

def testD():
    """
    Test procedure for Part D
    """
    #tests valid currency
    result = a1.is_currency('USD')
    introcs.assert_equals(True, result)
    #tests invalid currency
    result = a1.is_currency('CBD')
    introcs.assert_equals(False, result)
    #testing exchange
    result= a1.exchange('USD', 'CUP', 2.5)
    introcs.assert_floats_equal(64.375, result)
    #testing longer exchange
    result= a1.exchange('TTD', 'JMD', 2.5)
    introcs.assert_floats_equal(48.690190282653, result)

#implementing tests
testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
