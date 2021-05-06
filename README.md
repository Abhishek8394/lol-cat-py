# Introduction

This is inspired from lolcat [orginally](https://github.com/busyloop/lolcat) made in ruby.
This project is available on **pypi** as a python package.

**Note:** Works on linux ,mac, cygwin and presumably on win 10+ cmd lines, outputs plain text if terminal support not found. Also works on Windows Terminal.

## Installation

```bash
pip install lolpython
```

## Usage

#### 1. From code

```python
from lolpython import lol_py 

text = "Lorem ipsum..."
lol_py(text)

```
![colourful output echoed](https://github.com/Abhishek8394/lol-cat-py/blob/master/screenshot.png?raw=true "output of previous command")

#### 2. From cmd line

```bash
lolpython --inp-file "rainbow_this_file.txt"

# if want to do interactive
>> lolpython
>>.. lorem ipsum
>>.. hello world
>>.. [ctrl+d]
>> # rainbow version of the input typed so far
```
