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

Segmentor.segment(sentence) # one Thai sentence as an argument, return list of segmented words

Segmentor.test()            # show testing word segmentation by using default test set
```
