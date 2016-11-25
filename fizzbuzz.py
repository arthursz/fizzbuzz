from unittest import TestCase


def fizzbuzz(numbers):
    fizzbuzz = []

    for number in numbers:
        word = ''

        if number % 3 == 0:
            word = 'fizz'

        if number % 5 == 0:
            word += 'buzz'

        fizzbuzz.append(word or number)

    return fizzbuzz

class TestFizzbuzz(TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz([15]), ['fizzbuzz'])

    def test_fizz(self):
        self.assertEqual(fizzbuzz([3]), ['fizz'])

    def test_buzz(self):
        self.assertEqual(fizzbuzz([5]), ['buzz'])

    def test_fizzbuzz_sequence(self):
        self.assertEqual(fizzbuzz([1, 3, 5, 15]), [1, 'fizz', 'buzz', 'fizzbuzz'])

    def test_number(self):
        self.assertEqual(fizzbuzz([1]), [1])
