from getgauge.python import *
# step, after_suite, Messages

vowels = ["a", "e", "i", "o", "u"]


def number_of_vowels(word):
    return len([elem for elem in list(word) if elem in vowels])


# --------------------------
# Gauge step implementations
# --------------------------

@given('the word {word}')
def test_given_word(context, word):
	context.word = word

@then('there are {number} vowels')
def assert_no_of_vowels_in(context, number):
    assert str(number) == str(number_of_vowels(context.word))
