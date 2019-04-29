#！/usr/bin/env python3
# _*_ coding:utf-8 _*_

##class Student(object):
##    __slots__=("a","_birth")
##    @property
##    def birth(self):
##        return self._birth
##    @birth.setter
##    def birth(self,value):
##        self._birth=value
##    @property
##    def age(self): 
##        return 2018-self._birth
##def power(x,y=2,*n,city,job,**kw):
##    print(x,y,n,city,job,kw)
##    print(n[1])
##    print(kw.get("sd"))
##import functools
##
##def log(text):
##    def fun(func):
##        @functools.wraps(func)
##        def wraps(*args,**kw):
##            print('call:',func.__name__)
##            return func(*args,**kw)
##        return wraps
##    return fun
##@log('打印log')
##def pri(*s):
##    print(s)

##class MyObject(object):
##    def __init__(self):
##        self.x=9
##    def power(self):
##        return self.x*self.x
class Student(object):
    def __init__(self,name):
        self.name=name
        self.sum=0
    def __str__(self):
        return 'Student object (name:{0})'.format(self.name)
    __repr__=__str__
    def __iter__(self):
        return self
    def __next__(self):
        self.sum+=self.name
        if self.name>=101:
            raise StopIteration()
        self.name+=1
        return self.sum
    def __setitem__(self,key,value):
        print('key:',key,'value:',value)
    def __delitem__(self,key):
        print(key)
        del key
##        print(key)
    def __getitem__(self,n):
        self.sum=0
        if isinstance(n,int):
            print('调用getitem函数开始')
            for x in range(1,n+1):
                self.sum+=x
            return self.sum
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            step=n.step
            if start is None:
                    start=1
            if stop is None:
                stop=101
            self.sum=0
            if step is None:
                for x in range(start,stop):
                    self.sum+=x
                return self.sum
            else:
                st=start
                while st<stop:
                    self.sum+=st
                    st+=step
                return self.sum
                    
    def __getattr__(self,attr):
        if attr=='score':
            return '属性存在'
##        else:
##            return '属性不存在'
        if attr=='aage':
            return lambda:25

    
if __name__=='__main__':

    s=Student(50)
    print(s)
##    for x in s:
##        print(x)
    print(s[3])
    print(s.score)
    print(s.sco)
    print(s[2:20])
    print(s[2:10:2])
    print(s[2:])
    s['meinv']='nihao'
    del s['sum']
    print(s.aage())
##    s=Student()
##    s.birth=1995
##    print(s.birth)
##    print(s.age)
##    l=(1,2,3,4,5)
##    k={"sd":"sdfg","df":"dgweg"}
##    power(5,*l,city='beijing',job='student',**k)
##    pri([1,2,3,4,5,6,7,8,9,0])
##    obj=MyObject()
##    if hasattr(obj,"x"):
##        print(obj.x)
##    if not hasattr(obj,'y'):
####        setattr(obj,"y",5)
##        print(getattr(obj,'y',404))
    
