from setuptools import setup

setup(
    name='vrsegment',
    version='0.0.1',
    description='Thai Word Segmentation',
    packages = ['vrsegment'],
    data_files=[
        ('vrsegment', ['src/corpus/dictionary.json','src/key/key_set.txt','src/test/test_set.txt']),
    ],
)
