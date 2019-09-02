''' Prototype Design Pattern with book example'''

import copy
from collections import OrderedDict

class Book:
    def __init__(self, name, authors, price, **rest):
        '''Examples of rest: publisher, length, tags, publication, date'''
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{} : {}'.format(i, ordered[i]))

            if i == 'price':
                mylist.append('$')

            mylist.append('\n')

        return ''.join(mylist)

class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, code, obj):
        self.objects[code] = obj

    def unregister(self, code):
        del self.objects[code]

    def clone(self, code, **attr):
        
        found = self.objects.get(code)
        if found != "":
            obj = copy.deepcopy(found)
            obj.__dict__.update(attr)
            return obj

        elif not found:
            raise ValueError(
                'Incorrect object code: {}'.format(code))
    

def main():

    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M Ritchie'), price=118, publisher='Prentice Hall',
              length=228, publication_date='1978-02-22', tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()

    code = 'identificador'

    prototype.register(code, b1)

    b2 = prototype.clone(code, name='The C# Programming Language',price=48.99, length=274, publication_date='1988-04-01', edition=2)
                         
    b3 = prototype.clone(code, name='The JAVA Programming Language',price=99.99, length=286, publication_date='2002-06-10', edition=4, tags=('Java', 'programming', 'algorithms', 'data structures'))
    
    print(b1)
    print(b2)
    print(b3)

    print("ID b1 : {} != ID b2 : {} != ID b3 : {}".format(id(b1), id(b2), id(b3)))

if __name__ == '__main__':
    main()