import re
from utils import is_string


def uppercase(string):
    """
    Return a string in uppercase

    :param string:

    :return string:

    Examples::

    >>> uppercase("zenofpython")
    >>> ZENOFPYTHON
    """

    is_string(string)

    return string.upper()


def lowercase(string):
    """
    Return a string in lowercase

    :param string:

    :return string:

    Examples::

    >>> lowercase("ZENOFPYTHON")
    >>> zenofpython
    """

    is_string(string)

    return string.lower()


def camel_case(string):
    # this is called lower camel case and upper case by some as well
    """
    Return a string to camelCase

    :param string:

    :return string:

    Examples::

    >>> camel_case("Zen of Python")
    >>> camel_case("Zen-of-Python")
    >>> camel_case("Zen.of.Python")
    >>> camel_case("zen OF pYthon")
    >>> camel_case("ZEN of_PYTHON")
    >>> camel_case("zen.OF-python")

    >>> zenOfPython # for all above use cases
    """

    is_string(string)

    camel_cased_regex = re.compile("[^A-Za-z]+")
    camel_cased_str = camel_cased_regex.split(string)

    return "".join(w.lower() if i is 0 else w.title() for i, w in enumerate(camel_cased_str))


def pascal_case(string):
    """
    Return a string to PascalCase

    :param string:

    :return string:

    Examples::

    >>> pascal_case("zen of python")
    >>> pascal_case("zen-of-python")
    >>> pascal_case("ZEN-OF-PYTHON")
    >>> pascal_case("ZEN_OF_PYTHON")
    >>> pascal_case("ZeN-oF.PYthon")
    >>> pascal_case("zen.of.python")
    >>> pascal_case("zen-of{python")

    >>> ZenOfPython # for all above use cases
    """

    is_string(string)

    return "".join(a.capitalize() for a in re.split('([^a-zA-Z0-9])', string)
                   if a.isalnum())


def pascal_to_snake_case(string):
    """
    Return a CamelCase to snake_case

    :param string:

    :return string:

    Examples::

    >>> camel_to_snake_case("ZenOfPython")
    >>> camel_to_snake_case("ZenOfJavascript")

    >>> zen_of_python
    >>> zen_of_javascript
    """

    is_string(string)

    snake_case_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_case_str).lower()


def trimmed_case(string):
    """
    Return a trimmed string

    :param string:

    :return string:

    Examples::

    >>> trimmed_case("Zen Of Python       ")
    >>> trimmed_case("        Zen Of Python")

    >>> Zen Of Python  # for both use cases
    """

    is_string(string)

    return string.strip()


def kebab_case(string):
    """
    Return a string to kebab-case

    :param string:

    :return string:

    Examples::
    >>> kebab_case("Zen of Python")
    """

    is_string(string)

    return ''.join(['-' + i.lower() if i.isupper()
                    else i for i in string]).lstrip('-')


def css_camelcase_case(string):
    """
    Return a string to .cssCase -

    :param string:

    :return string:

    Examples::
    >>> css_camecase_case("Zen of Python")
    >>> css_camecase_case("Zen-of-Python")
    >>> css_camecase_case("Zen.of.Python")
    >>> css_camecase_case("zen OF pYthon")
    >>> css_camecase_case("ZEN of_PYTHON")
    >>> css_camecase_case("zen.OF-python")

    >>> .zenOfPython # for all above use cases
    """

    is_string(string)
    dot = "."

    return dot + camel_case(string)

