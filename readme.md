# Python Tips
* `python -i app.py starts` the app in interactive mode with access to all variables and methods in the file.
* `pip --version` to view installed PIP (Python Package Installer) version
* `pip install -U package_name` to update a selected package.
* `pip install package_name==package_version` install selected version, NOTE the double equals sign before package version.
* `pip uninstall package_name` to uninstall a package.
*  The list of the main pip activities looks as follows:
    * `pip help operation` – shows a brief description of pip;
    * `pip list` – shows a list of the currently installed packages;
    * `pip show package_name` – shows package_name info including the package's dependencies;
    * `pip search anystring` – searches through PyPI directories to find packages whose names contain anystring;
    * `pip install name` – installs name system-wide (expect problems when you don't have administrative rights);
    * `pip install --user name` – installs name for you only; no other platform user will be able to use it;
    * `pip install -U name` – updates a previously installed package;
    * `pip uninstall name` – uninstalls a previously installed package.
* `#!/usr/bin/env python2` shebang tells a Unix or Unix-like OS how to execute the contents of a Python file.

## String Methods

1. Some of the methods offered by strings are:
    * `capitalize()` – changes all string letters to capitals;
    * `center()` – centers the string inside the field of a known length;
    * `count()` – counts the occurrences of a given character;
    * `join()` – joins all items of a tuple/list into one string;
    * `lower()` – converts all the string's letters into lower-case letters;
    * `lstrip()` – removes the white characters from the beginning of the string;
    * `replace()` – replaces a given substring with another;
    * `rfind()` – finds a substring starting from the end of the string;
    * `rstrip()` – removes the trailing white spaces from the end of the string;
    * `split()` – splits the string into a substring using a given delimiter;
    * `strip()` – removes the leading and trailing white spaces;
    * `swapcase()` – swaps the letters' cases (lower to upper and vice versa)
    * `title()` – makes the first letter in each word upper-case;
    * `upper()` – converts all the string's letter into upper-case letters.

2. String content can be determined using the following methods (all of them return Boolean values):
    * `endswith()` – does the string end with a given substring?
    * `isalnum()` – does the string consist only of letters and digits?
    * `isalpha()` – does the string consist only of letters?
    * `islower()` – does the string consists only of lower-case letters?
    * `isspace()` – does the string consists only of white spaces?
    * `isupper()` – does the string consists only of upper-case letters?
    * `startswith()` – does the string begin with a given substring?

* The is operator checks whether two variables refer to the same object.