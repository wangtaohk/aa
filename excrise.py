#! /usr/bin/env python3
# _*_ coding:utf-8 _*_

'2018-9-7'
__author__='wangtao'

##from enum import Enum,unique
##
##@unique
##class Myenum(Enum):
##    
##    Sun = 0 # Sun的value被设定为0
##    Mon = 1
##    Tue = 2
##    Wed = 3
##    Thu = 4
##    Fri = 5
##    Sat = 6
##    Sunn = 36
##Month=Enum('Month',('Jan','Feb','Mar','Apr','May'))
##def fn(self,name='liming'):
##    print(name+'nihao')


##liming=type('hello',(object,),dict(hello=fn))



##元类
##class ListMetaclass(type):
##    def __new__(cls,name,bases,attrs):
##        attrs['add']=lambda self,value:self.append(value)
##        return type.__new__(cls,name,bases,attrs)
##class MyList(list,metaclass=ListMetaclass):
##    pass


import logging
import pdb
logging.basicConfig(level=logging.WARNING)
def foo(s):
    n=int(s)
##    assert n!=0, 'n is zero'
    logging.info('n:{0}'.format(n))
##    pdb.set_trace()
    return 10//n



if __name__=='__main__':
    print(foo(0))
    
##    L=MyList()
##    L.add(1)
##    L
##    li=liming()
##    li.hello()
##    for name, member in Month.__members__.items():
##        print(name,member.value)
##    print(Month.Apr.value)
##    for name,index in Myenum.__members__.items():
##        print(name,index.value)
