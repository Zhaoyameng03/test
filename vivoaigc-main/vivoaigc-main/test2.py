# encoding: utf-8
# test.py
from test3 import sync_vivogpt
#from test3 import data
def main():
    data_dict = sync_vivogpt()
    
    print(data_dict['prompt'])


if __name__ == '__main__':
    main()
