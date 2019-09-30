import os
import unittest


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyze

    Raises:
        IOError: If ``filename`` does not exist

    Returns:
        A tuple containing number of lines and characters in a file
    """
    lines = 0
    chars = 0
    with open(filename, mode='rt', encoding="utf-8") as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)


class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function"""

    def setUp(self):
        """Fixture that creates a file for text methods to use"""
        self.filename = 'text_anaylysis_test_file.txt'
        with open(self.filename, mode='wt', encoding="utf-8") as f:
            f.write("I am learning python\n"
                    "I hope I implement it somewhare\n"
                    "Otherwise it will all be for nothing")

    def tearDown(self):
        """Fixture that deletes the file created for test methods"""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run"""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct"""
        self.assertEqual(analyze_text(self.filename)[0], 3)

    def test_character_count(self):
        """Check that character count is correct"""
        self.assertEqual(analyze_text(self.filename)[1], 89)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == "__main__":
    unittest.main()
