import unittest


class TestCases(unittest.TestCase):
    def test_lowercase(self):
        from cases import lowercase

        self.assertEqual('zenofpython', lowercase("ZENOFPYTHON"))
        self.assertEqual('zenofpython', lowercase("zEnOFPythoN"))

    def test_uppercase(self):
        from cases import uppercase

        self.assertEqual('ZENOFPYTHON', uppercase("zenofpython"))
        self.assertEqual('ZENOFPYTHON', uppercase("zEnOFPythoN"))

    def test_camel_case(self):
        from cases import camel_case

        self.assertEqual('zenOfPython', camel_case("Zen of Python"))
        self.assertEqual('zenOfPython', camel_case("Zen-of-Python"))
        self.assertEqual('zenOfPython', camel_case("Zen.of.Python"))
        self.assertEqual('zenOfPython', camel_case("Zen_of_Python"))
        self.assertEqual('zenOfPython', camel_case("zen OF pYthon"))
        self.assertEqual('zenOfPython', camel_case("ZEN of_PYTHON"))
        self.assertEqual('zenOfPython', camel_case("zen.OF-python"))

    def test_pascal_case(self):
        from cases import pascal_case

        self.assertEqual('ZenOfPython', pascal_case("zen of python"))
        self.assertEqual('ZenOfPython', pascal_case("zen-of-python"))
        self.assertEqual('ZenOfPython', pascal_case("ZEN-OF-PYTHON"))
        self.assertEqual('ZenOfPython', pascal_case("ZEN_OF_PYTHON"))
        self.assertEqual('ZenOfPython', pascal_case("ZeN-oF.PYthon"))
        self.assertEqual('ZenOfPython', pascal_case("zen.of.python"))
        self.assertEqual('ZenOfPython', pascal_case("zen-of{python"))

    def test_kebab_case(self):
        from cases import kebab_case

        self.assertEqual('zen-of-python', kebab_case("ZenOfPython"))
        self.assertEqual('zen-of-py-thon', kebab_case("ZenOfPyThon"))

    def test_trimmed_case(self):
        from cases import trimmed_case

        self.assertEqual('Zen Of Python', trimmed_case("Zen Of Python     "))
        self.assertEqual('Zen Of Python', trimmed_case("     Zen Of Python"))

    def test_pascal_to_snake_case(self):
        from cases import pascal_to_snake_case

        self.assertEqual('zen_of_python', pascal_to_snake_case("ZenOfPython"))
        self.assertEqual('zen_of_some_really_long_pascal_case', pascal_to_snake_case("ZenOfSomeReallyLongPascalCase"))


if __name__ == '__main__':
    unittest.main()
