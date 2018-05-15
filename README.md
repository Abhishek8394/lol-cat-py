# Introduction

This is inspired from lolcat [orginally](https://github.com/busyloop/lolcat) made in ruby.
This project is available on **pypi** as a python package.

**Note:** Works on linux ,mac, cygwin and presumably on win 10+ cmd lines, outputs plain text if terminal support not found.

## Installation

```bash
pip install lolpython
```

## Usage

#### 1. From code

```python
from lolpython import lol_py 

text = "hello world"
lol_py(text)

```

#### 2. From cmd line

```bash
lolpy --inp-file "rainbow_this_file.txt"

# if want to do interactive
>> lolpy
>> lorem ipsum
>> hello world
>> [ctrl+d]
>> # rainbow version of the input typed so far
```
