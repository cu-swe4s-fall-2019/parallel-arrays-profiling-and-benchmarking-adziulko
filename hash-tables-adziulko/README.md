# Hash tables
Objectives : Implement and benchmark hash functions and collision resolution strategies.


## File instruction
To test for python Pep8 style, you will need to:
1. Install pycodestyle
2. Run pycodestyle on desired file (in this case it is 'hash_tables.py')
```
pip install pycodestyle
pycodestyle hash_tables.py
```

To implement desired Hash Function Algorithm:
1. Have Python3 installed
2. In command line:
    - input the Hash Table Size
    - input desired hash method (ascii, rolling, random)
    - input collision strategy (linear probing, chained)
    - input file name
    - input key

```
python hash_tables.py --table_size 360 --hash_method h_ascii --collision_strategy ChainHashTable --file_name bananas.txt --key 3
```
