# PwGen
This is a Password generator made with python 3.9. (Also compatible with older Versions)

## Installation:
The Repository contains shell- (for linux) and batch- (for Windows) scripts, which can be added to path in order to excecute ``pwgen(.sh)`` from everywhere. <br>
It refers to the python-file, so it should stay in the same Directory.

## Usage:
```shell
$ python PwGen.py -cipuld [length]
```
### Modify output:
 ``-c`` Copies password to Clipboard <br>
 ``-i`` Disables visible output (intended to be used with ``-c``)

### Modify generator:
Enable use of ... (Default is all):<br>
  ``-p``          Symbols<br>
  ``-u``          Uppercase-letters<br>
  ``-l``          Lowercase-letters<br>
  ``-d``          Digits

