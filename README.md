# Vrsegment

Word Segmentation Project for CSS432

## Prerequisites
Python >=3.6.4

### Installing
Clone this repository
```
https://github.com/sangrit-siit/vrsegment.git
```
```
pip3 install .
```

### Usage
```
from vrsegment import Segmentor

Segmentor.segment(sentence) # Thai sentence as an argument, return a list of segmented words
Segmentor.check(word)       # To check whether the word is the dictionary or not
Segmentor.test()            # To show word segmentation testing by using default test set
```
