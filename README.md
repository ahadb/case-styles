# Case Styles

Naming conventions module for Python. Is somewhat experimental, but once matured will be packaged up. You can convert
strings into `pascal case`, `camel case`, `kebab case`, `css case` and more.

### Usage

```python
import cases

cases.lowercase("ZenOfPython""")
cases.uppercase("ZenOfPython")
cases.camel_case("zen.of.python")
cases.pascal_case()
cases.pascal_to_snake_case("zen-of{python")
cases.trimmed_case("        Zen Of Python")
cases.kebab_case("Zen of Python")
cases.css_camelcase_case("zen OF pYthon")
```