# Vrsegment

Word Segmentation Project for CSS432

## Installation

### Prerequisites

* [Python 3.6.4](https://www.python.org)


pip installation
```
python3 get-pip.py
```

Clone this repository
```
git clone https://github.com/sangrit-siit/vrsegment.git
```

Install this package
```
cd vrsegment
pip3 install .
```

## Usage
```
from vrsegment import Segmentor

Segmentor.segment(sentence) # Thai sentence as an argument, return a list of segmented words
Segmentor.check(word)       # To check whether the word is the dictionary or not
Segmentor.test()            # To show word segmentation testing by using default test set
```

## Project Members
* 5822771333 Ms.Wari Maroengsit
* 5822771366 Ms.Papsineebhorn Sukchuen	
* 5822780334 Mr.Kriddanai Roonguthai
* 5822790861 Mr.Kittikom Sangrit
