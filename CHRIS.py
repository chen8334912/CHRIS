# # #-*- coding: UTF-8 -*-
# #
# #
# # #print('hello world')
# # #
# # # name = "chris"
# # #
# # # if "c"  in name:
# # #     if "cio" in name:
# # #         print('sao')
# # #     else:
# # #         print('shaabi')
# # #     print('ok')
# # # else:
# # #     print('diao')
# # #
# # #
# # # a = 123
# # # s = a.__abs__()
# # # print(s)
# # #
# # #
# # # int
# # #
# # # # str
# # #
# # #
# # #
# # # name = ' aleX'
# # # n = name.find('a')
# # # print(n)
# #
# #
# #
# # # name = 'sdfjkl  lllll lllll iooio'
# # # n = '444'.join(name)
# # # print(n)
# #
# #
# # #
# # # m = '123 123 345 89089090-8'
# # # n = str.maketrans('123', 'jsl')
# # # new_m = m.translate(n)
# # # print(new_m)
# #
# # #
# # # m = '1sdklafjkldsjf90-8'
# # # n = m.swapcase()
# # # print(n)
# #
# #
# # # m = '刘德华'
# # # n = len(m)
# # # print(n)
# #
# #
# # #
# # m='3127894789'
# #
# # # chris = 0
# # #
# # # while chris < len(m):
# # #     n = m[chris]
# # #     print(n)
# # #     chris += 1
# # # print('======')
# # #
# # #
# # # m = 1
# # # n = 0
# # # while m < 101:
# # #     n = m + n
# # #     m = m + 1
# # # print(n)
# #
# # for n in m:
# #     print(n)
#
#
#
#
#
# # chris = 'sadf1231531231'
# # for m in chris:
# #     print(m)
# #     break
#
# # chris = 'sadf1231531231'
# # for m in chris:
# #     continue
# #     print(m)
#
#
# #
# # m = 1
# # while m < 10:
# #     print(m)
# #     m = m + 1
# # print(1111111111111)
# #
# #
# # n = '123456789'
# # for ml in n:
# #     print(ml)
# # #
# #
# # v = range(1, 10,2)
# # for chris in v:
# #     print(chris)
# #
# #
# # m = 1
# # while m < 10:
# #     if m % 2 != 0:
# #         pass
# #     else:
# #         print(m)
# #     m = m + 1
# # print(1222223333456)
# #
# #
# # chris = '我想我是海'
# # fish =  chris.index('我')
# # print(fish)
#
#
#
#
# chris = input('请输入：')
# fish = len(chris)
# m = range(fish)
# for n in m:
#     print(n, chris[n])


# chris = input('请输入：')
# m1, m2 = chris.split('+')
# m1 = int(m1)
# m2 = int(m2)
# print(m1 + m2)


# n1 = 0
# n2 = 0
# chris = input('请输入：')
# for m in chris:
#     if m.isdigit():
#         n1 += 1
#     elif m.isalpha():
#         n2 += 1
# print(n1, n2)


# chris = '敬爱的{name}, 最喜欢在{where}地方干{what}'
# na = input('请输入姓名：')
# whe = input('请输入地方事情：')
# wh = input('请输入事情：')
# n = chris.format(name = na, where = whe, what = wh)
# print(n)

#
# chris = '敬爱的{}, 最喜欢在{}地方干{}'
# na = input('请输入姓名：')
# whe = input('请输入地方事情：')
# wh = input('请输入事情：')
# n = chris.format(na, whe, wh)
# print(n)
#

'''''
li = [1, 12, 9, 'cklsaj', ['df', 9, 12], True]
for chris in li:
    print(chris)

'''''
list

# li = [1, 12, 9, 'cklsaj', ['df', 9, 12], True]

# # li[2] = 11111
# # print(li)
#
# #
# # del li[3]
# # print(li)
#
# li = [1, 12, 9, 'cklsaj', ['df', 9, 12], True]
# v = li[4][2]
# print(v)


# m = [12, 1564, 11, '婆婆', 'sadf', [1, 451, 'oo']]
# l = ''
# for n in m:
#     l = l + str(n)
# print(l)


#
# li = [1,1,1,2,3,45,1,2,1]
# li.remove(1)
#     while 1 in li:
#     li.remove(1)
# print(li)


# tu = (11, 2323, '213', 123123)
# v = tu.index(123)
# print(v)


# l1	=	[11,22,33]
# l2	=	[22,33,44]
# a.	 获取内容相同的元素列表
# b.	 获取 l1	 中有， l2 中没有的元素列表
# c.	 获取 l2	 中有， l1 中没有的元素列表
# d.	 获取 l1	 和 l2	 中内容都不同的元素


# l1	=	[11, 22, 33]
# l2	=	[22, 33, 44]
#
# for m in l1:
#     if m in l2:
#         pass
#     else:
#         print(m)
# for n in l2:
#     if n in l1:
#         pass
#     else:
#         print(n)
#

#
# v = 0
# for n in range(1, 9):
#     for m in range(1, 9):
#         if n != m:
#             v += 1
# print(v)
# num = 0
# li = [1, 2, 3, 4, 5]
# for v in range(len(li)):
#     for w in range(len(li)):
#         if v != w:
#             num += 1
# print(num)

# for i in range(1,10):
#     string = ""
#     for j in range(1,i+1):
#         string +=str(j) + " * "+str(i) + " = " +str(i*j)+"\t"
#     print(string)
#

#
# for a in range(1, 10):
#     for b in range(1, a+1):
#         print(str(a)+ " * " +str(b)+ " = " +str(a * b)+'\t')
#
#
#
#
# if x + y + z ==100 and 5*x + 3*y + z/3 ==100
#     print(x, y, z)


# #99乘法表
#
# for i in range(1,10):
#     string = ""
#     for j in range(1,i+1):
#         string +=str(j) + " * "+str(i) + " = " +str(i*j)+"\t"
#     print(string)
#
# for m in range(1, 10):
#     num = ''
#     for n in range(1, m+1):
#         num += str(m) + '*' + str(n) + '=' + str(m*n) + '\t'
#     print(num)
#
#
# for m in range(1, 100//5):
#     for n in range(1, 100//3):
#         for l in range(1, 100):
#             if m + n + l == 100 and 5*m + 3*n + l/3 == 100:
#                 print(m,n,l)


# li = ['alex','eric','rain']
# m = '_'.join(li)
# print(type(m), m)
# n = m.replace('_','')
# s = '_'.join(n)
# print(s)


# li = [11, 22, 33, "asd", "xyz", "879", "hello"]
#
# m = str(item) for item in li:
# n = '_'.join(m)
# print(n)


# li = ['alex','eric',123]
# # m = ''
# # for i in li:
# #     m = m + str(i)
# #     n = '_'.join(m)
# # print(m)
#
# li[2] = str(li[2])
# m = '_'.join(li)
# print(m)

#
# li = ['alex','eric',123]
#
# li = map(str, li)
# print('_'.join(li))
#
# s = {[1, 2, 3], 1}
# print(s)

# s = set('hello')
# l = set(['dsf', 'wer', 'ewrwerwr'])
# print(s, l)

#
# fuchouzhe = ['zhizhuxia', 'bianfuxia', 'shandianxia']
# zhengyi = ['shenqinvxia', 'bianfuxia', 'haiwang']
#
# lianggelianmen = []
# for hero in fuchouzhe:
#     if hero in zhengyi:
#         lianggelianmen.append(hero)
# print(lianggelianmen)

# chris = {1, 2, 3, 4, 5, 6}
# fish = {2, 3, 4, 5, 7, 9}
# chris.symmetric_difference_update(fish)
# print(chris.isdisjoint(fish))

# chris = 'percent %(fish).2f' % {'fish': 98.8947598475}
# print(chris)


# print('root', 'x', '0', '0', sep = ',')


# chris = 'i am {}, age {}, {}'.format('chris', 18, 88)
# chris = 'i am {2}, age {0}, {1}'.format('chris', 18, 88)
# chris = 'i am {0[0]}, age {0[1]}, really {1[0]}'.format([1, 2, 5], [3, 4, 8])
# chris = 'i am {chris}, age {fish}, really {li}'.format(**{'chris':'chris', 'fish': '18', 'li': '88'})
# chris = 'i am {:s}, age {:s}, really {:d}'.format(*['chris', '6789', 18])
# chris = 'i am {1}, age {0}, really {2}'.format('chris', '88', 18)
# chris = 'num: {:b}, {:o}, {:d}, {:x}, {:X}, {:%}'.format(12, 12, 12, 12, 12, 12)
# print(chris)

# def test(x):
#     y = 2 * x + 1
#     return y
# print(test)
# a= test(3)
# print(a)


'''''
# def test(x, y, z):
#     print(x)
#     print(y)
#     print(z)
# test(8, 2, 3)
# test(x = 9, y = 2, z = 3)
# # 位置参数在关键字参数左边
#
# test(8, 2, z = 3)
#
'''''

# def chris(x, y = 'fish'):
#     print(type(x), x)
#     print(type(y), y)
# chris('lksjfkl','890')
# chris('hello', y = 'klsdjf')

# def test(x, *args):
#     print(x)
#     print(args)
#     print(args[0])
#     print(args[0][0])
# # test(1, 2, 3, 4, 8, 9)
# test(1, *['x', 'y' ,'z'])
# # test(1, ['x', 'y' ,'z'])
#


# def test(x, **kwargs):
#     print(x)
#     print(kwargs)
# test(1, y = 3,w = 5)


# def chris(x, *args, **kwargs):
#     print(x)
#     print(*args)
#     print(**kwargs)
# chris(1, 1, 2, 3, q=3, w=4)


# name = ['sjdlkf']
#
# def chris():
#     name.append('wer')
#     print('我的名字', name)
#
# chris()

# 全局变量大写，局部变量小写

# NAME = '海风'      #1
#
# def shazi():
#     name = '傻子'      #3
#     print(name)      #4
#     def pangzi():
#         name = '胖子'      #6
#         print(name)      #7
#         def shouzi():
#             name = '瘦子'      #10
#             print(name)      #11
#         shouzi()      #8
#     pangzi()
#     print(name)      #9
#
# shazi()      #2


# chris = 'shuai'
#
# def mic():
#     global chris
#     chris = 'ku'
#     print(chris)
# print(chris)
# mic()
# print(chris)
#
#
#
#
# name = "刚娘"
#
# def weihou():
#     name = "陈卓"
#     def weiweihou():
#         global name
#         name = "冷静"
#     weiweihou()
#     print(name)
#
# print(name)
# weihou()
# print(name)


'''''递归函数

def chris(n):
    print(n)
    if n > 0:
        chris(n-1)
    else:
        print('----------')
    print(n)

chris(3)

'''''

# person_list=['alex','wupeiqi','linhaifeng','zsc']
# def ask_way(person_list):
#     print('-'*60)
#     if len(person_list) == 0:
#         return '根本没人知道'
#     person=person_list.pop(0)
#     if person == 'linhaifeng':
#         return '%s说:我知道,老男孩就在沙河汇德商厦,下地铁就是' %person
#
#     print('hi 美男[%s],敢问路在何方' % person)
#     print('%s回答道:我不知道,但念你慧眼识猪,你等着,我帮你问问%s...' % (person, person_list))
#
#     res=ask_way(person_list)
#
#
#     print('%s问的结果是: %res' %(person,res))
#     return res
#
# res=ask_way(person_list)
# print(res)


# jishubu = ['李铁峰', '王瑞涛', '严岳','陈亮']
# def wenlu(jishubu):
#     if len(jishubu) == 0:
#         return '没有人知道'
#     ren = jishubu.pop(0)
#     if ren == '王瑞涛':
#         return '左边'
#
#     print('%s， 你知道怎么去厕所嘛' %ren)
#     print('%s说我帮你问问 %s' %(ren, jishubu))
#
#     res = wenlu(jishubu)
#     print('%s问的结果是: %res' %(ren,res))
#     return res
# res = wenlu(jishubu)
# print(res)


# name = 'chris'
# def foo():
#     if name != 'chris':
#         return 'wo shi shuaige'
#     else:
#         return 'laji'

# name = 'jdlskajf'
# def chris(name):
#     return name+'_sb'
#
# print(chris(name))


# name = 'chris'
#
# def foo():
#     name = 'fish'
#     def bar():
#         name = 'micheal'
#         def tt():
#             print(name)
#         return tt
#     return bar
# ln = foo()()()
# print(ln)


# name = 'chris'
# sj = lambda x : name+'_shuaqi'
# print(sj(name))

'''''
def cal(x):
    return 2*x+1

print(cal(5))

'''''

# def foo(n): #n=bar
#     print(n)
#
# def bar(name):
#     print('my name is %s' %name)
#
# # foo(bar)
# # foo(bar())
# # foo(bar('alex'))


num = [1, 2, 10, 5, 3, 7]
num2 = [1, 22, 10, 5, 3, 7]

# chris = []
# for i in num:
#     chris.append(i**2)
# print(chris)

#
# def pf(shuzu):
#     chris = []
#     for i in num2:
#         chris.append(i**2)
#     return chris
#
# print(pf(num2))

# def map_test(func,array):
#     ret=[]
#     for i in num_l:
#         res=func(i) #add_one(i)
#         ret.append(res)
#     return ret
#
# print(map_test(add_one,num))


# num=[1,2,10,5,3,7]


# li = []
# # for i in num:
# #     li.append(i**2)
# # print(li)
#
# def pingfang(zhi):
#     for i in zhi:
#         li.append(i**2)
#     return li
# print(pingfang(num))
#
# print(list(map(lambda x:x**2, num)))

# peo=['alex_sb','wupeiqi_sb','linhaifeng','yuanhao_sb']

# li = []
# for i in peo:
#     if not i.endswith('sb'):
#         li.append(i)
# print(li)
#
# def chris(fangfa, zhi):
#     li = []
#     for i in zhi:
#         if not fangfa(i):
#             li.append(i)
#     return li
#
# res = chris(lambda x:x.endswith('sb'), peo)
# print(res)

#
#
# print(list(filter(lambda x:not x.endswith('sb'), peo)))


li = [1, 2, 3, 100]

#
# ret = 0
# for i in li:
#     ret += i
# print(ret)


# def chris(zhi):
#     ret = 0
#     for i in zhi:
#         ret += i
#     return ret
# print(chris(li))

# def xiangjia(x,y):
#     return x+y
#
# def chris(func, array):
#     res = 0
#     for i in array:
#         res += i
#     return res
# print(chris(xiangjia, li))
# print(reduce(lambda x,y:x+y,li))


#
#
# num_l=[1,2,3,100]
# def reduce_test(func,array,init=None):
#     if init is None:
#         res=array.pop(0)
#     else:
#         res=init
#     for num in array:
#         res=func(res,num)
#     return res
# print(reduce_test(lambda x,y:x+y,num_l))


# name='你好'
# print(bytes(name,encoding='utf-8').decode('utf-8'))


# age_dic={'alex_age':18,'wupei_age':20,'zsc_age':100,'lhf_age':30}
#
#
# print(list(max(zip(age_dic.values(),age_dic.keys()))))


# print(max(age_dic.values()))
#
# #默认比较的是字典的key
# # print(max(age_dic))
#
# for item in zip(age_dic.values(),age_dic.keys()): #[(18,'alex_age')  (20,'wupeiqi_age') () () ()]
#     print(item)
# #
# print('=======>',list(max(zip(age_dic.values(),age_dic.keys()))))

# l=[
#     (5,'e'),
#     (1,'b'),
#     (3,'a'),
#     (4,'d'),
# ]
# # l1=['a10','b12','c10',100] #不同类型之间不能进行比较
# l1=['a10','a2','a10'] #不同类型之间不能进行比较
# print(list(max(l)))
# print('--->',list(max(l1)))


# l=[1,3,100,-1,2]
# print(max(l))
# dic={'age1':18,'age2':10}
# print(max(dic)) #比较的是key
# print(max(dic.values())) #比较的是key，但是不知道是那个key对应的
#
# print(max(zip(dic.values(),dic.keys()))) #结合zip使用
#

# people=[
#     {'name':'alex','age':1000},
#     {'name':'wupei','age':10000},
#     {'name':'yuanhao','age':9000},
#     {'name':'linhaifeng','age':18},
# ]
#
# age_dic={'alex_age':18,'wupei_age':20,'zsc_age':100,'lhf_age':30}
#
# # ret = []
# # for i in people:
# #     ret.append(i['age'])
# # print(ret)
#
# print(sorted(people, key=lambda x:x['age']))


# chris = open('eop.py', 'r')
# data = chris.readlines()
# fish = open('eop.py', 'w')
# fish.write(data[0])
# chris.close()
# fish.close()

# f = open('日志文件', 'rb')
#
# for i in f:
#     offs=-3
#     n=0
#     while True:
#         f.seek(offs,2)
#         data=f.readlines()
#         if len(data) > 1:
#             print('最后一行%s' %(data[-1].decode('utf-8')))
#             break
#         offs*=2


# l=[1,3,100,-1,2]
# res = l.__iter__()
# print(res)
# print(res.__next__())
# print(next(res))
# print(next(res))


# egglist = []
# for i in range(10):
#     egglist.append('鸡蛋%s'%i)
# print(egglist)
#
# l = ['鸡蛋%s' %i for i in range(10)]   # 列表解析
# print(l)

# laomuji = ('鸡蛋%s' % i for i in range(3))   # 生成器表达式，生成器表达式比列表解析更省内存
# print(laomuji)
# print(next(laomuji))
# print(next(laomuji))
#

# print(sum(i for i in range(10)))


# def xiadan():
#     ret = []
#     for i in range(10):
#         ret.append('鸡蛋%s' %i)
#     return ret
# print(xiadan())
#
#
# x = ['鸡蛋%s' %i for i in range(100)]
# print(x)
#
# y = ('鸡蛋%s' %i for i in range(100))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

# def xiadan():
#     for i in range(10):
#         yield '鸡蛋%s' %i
# chris = xiadan()
# print(next(chris))
# print(next(chris))
# print(next(chris))
# print(next(chris))

# def chris():
#     ret = []
#     with open('renkou.py', 'w') as f:
#         for i in f:
#             ret.append(i)
#     return ret
# print(chris())


'''''

def get_popu():
    with open('renkou.py', 'r') as f:
        for i in f:
            yield i

g = get_popu()     # g是一个生成器，Python的生成器是一个返回可以迭代对象的函数
s1 = eval(g.__next__())     # eval函数就是实现list、dict、tuple与str之间的转化
print (type(s1))
print (s1['num'])
# res = 0
# for p in g:
#     p_dic = eval(p)
#     print (p_dic['num'])
#     res += p_dic['num']
# print (res)

all_pop = sum(eval(i)['num'] for i in g)
print (all_pop)


for p in g:
    print (eval)

'''''

'''''
def test():
    print('开始')
    first = yield 99
    print('第一次', first)
    second = yield 2
    print('第二次',second)
    yield 3

t = test()
res = t.__next__()
print(res)
t.send(55)
t.send(88)

'''''

'''''

import time

list = ['roubaozi', 'caibaozi', 'jiucaibaozi','niuroubaozi','23']
def ren(name):
    print('我是%s 等着吃包子' %name)
    while True:
        baozi = yield
        time.sleep(2)
        print('这个%s包子是我%s最爱吃的' %(baozi,name))
def bao():
    l1 = ren('chris')
    l2 = ren('mc')
    l1.__next__()
    l2.__next__()
    for i in list:
        l1.send(i)
        l2.send(i)
bao()

'''''

'''''

def func(start, end, a = 0, b = 0):
    if start == end:
        return a,b
    if start %3 == 0 and start %7 == 0:
        a += 1
        b += start
    ret = func(start+1, end, a, b)
    return ret
res = func(1, 300)
print(res)

'''''

'''''

def func(zifu1):
    a=0
    b=0
    c=0
    for i in zifu1:
        if i.isupper():
            a+=1
        elif i.islower():
            b+=1
        elif i.isdigit():
            c+=1
    return ({'daxie':a,'xiaoxie':b,'shuzi':c})
zifu1 = ('aaa111AAA')
print(func(zifu1))



'''''

'''''





fun1(a,b,c) 
fun2(a=1,b=2,c=3) 
fun3(*args) 
fun4(**kargs)

四种中最常见是前两种，基本上一般点的教程都会涉及，后两种一般很少单独出现，常用在混合模式中
第一种 fun1(a,b,c)是直接将实参赋予行参，根据位置做匹配，即严格要求实参的数量与行参的数量位置相等，比较一般，大多数语言常用这种方式。

第二种 fun2(a=1,b=2,c=3)根据键值对的形式做实参与行参的匹配，通过这种式就可以忽略了参数的位置关系，直接根据关键字来进行赋值，
同时该种传参方式还有个好处就是可以在调用函数的时候作为个别选填项，不要求数量上的相等，即可以fun5(3,4)来调用fun2函数，
这里关键就是前面的3,4覆盖了原来a、b两个行参的值，但c还是不变采用原来的默认值3，这种模式相较第一种更加灵活，
不仅可以通过fun6(c=5,a=2,b=7)来打乱行参的位置，而且可以在但没有对应行参传递的时候常用定义函数时的默认值。

第三种 fun3(*args)，这传参方式是可以传入任意个参数，这些若干参数都被放到了tuple元组中赋值给行参args，之后要在函数中使用这些行参，
直接操作args这个tuple元组就可以了，这样的好处是在参数的数量上没有了限制，但是因为是tuple，其本身还是有次序的，
这就仍然存在一定的束缚，在对参数操作上也会有一些不便

第四种 fun4(**kargs)最为灵活，其是以键值对字典的形式向函数传参，含有第二种位置的灵活的同时具有第三种方式的数量上的无限制。
此外第三四种函数声明的方式前的'*',与c里面的指针声明一样，这里仅做声明标识之用
最后要强调的是四种传递方式混合使用(大多数情况是这种),fun7(a,b,*c,**d),但四种方式混用时要遵守：


  ● args = 须在args之后
  ● *args须在args=value之后
  ● **kargs须在*args之后
赋值过程为：
  1. 按顺序把传给args的实参赋值给对应的行参
  2. args = value 形式的实参赋值给行参
  3. 将多余出的即键值对行后的零 散实参打包组成一个tuple传递给*args
  4. 将多余的key=value形式的实参打包正一个dicrionary传递给**kargs
举例
定义
def test(x,y=5,*,**b): 
>>>>print x,y,a,b
调用结果
test(1) ===> 1 5 () {} 
test(1,2) ===> 1 2 () {} 
test(1,2,3) ===> 1 2 (3,) {} 
test(1,2,3,4) ===> 1 2 (3,4) 
test(x=1) ===> 1 5 () {} 
test(x=1,y=1) ===> 1 1 () {} 
test(x=1,y=1,a=1) ===> 1 1 () {'a':1} test(x=1,y=1,a=1,b=1) ===> 1 1 () {'a':1,'b':1} 
test(1,y=1) ===> 1 1 () {} 
test(1,2,y=1) ===> 出错，说y给赋了多个值
test(1,2,3,4,a=1) ===> 1 2 (3,4) {'a':1} 
test(1,2,3,4,k=1,t=2,o=3) ===> 1 2 (3,4) {'k':1,'t':2,'o':3}


'''''

'''''
#默认参数
print('\n以下是默认参数传值\n')
def stu_info(name,age,major,country = 'CN'):      # country设为了默认参数，必须放在位置参数之后,否则会出错
    print('--------学生信息-------')
    print('姓名：',name)
    print('年龄：',age)
    print('专业：',major)
    print('国籍：',country)

# stu1 = stu_info('Jack',21,'Chinese')     # 此处未传对应的值，但形参中已经定义了，所以不用担心找不家了！
# stu2 = stu_info('Frank',20,'JP')　　      # 你也是的
stu3 = stu_info('Rose',19,'Art','UK')# 既然你已经传参了，就随你了。


'''''


# def func(a):
#     return  a+100
# func = lambda a:a+200
# ret = func(10)
# print(ret)


# str = '老男孩'
# print(str.encode('utf-8'))
# print(bytes('老男孩', encoding='utf-8'))
# print(bytes('老男孩', 'utf-8'))


# def test(arg):
#     a=1
#     b=2
#     data_dict = {}
#     print(locals())
#     print(globals())
#
#
# if __name__ == '__main__':
#     test(3)


# 内置函数zip
#
# l1=['alex',1]
# l2=['alex22',1]
# l3=['alex33',1]
#
# print('_'.join(list(zip(l1,l2,l3))[0]))


# a=[1,2]
# def ss():
#     a.append(456)
# ss()
# print(a)


# name = 'root'
#
# def func():
#    name = "seven"
#    def outer():
#        name = "eric"
#        def inner():
#            global name
#            name = "蒙逼了吧..."
#        print(name)
#    print(name)
#
# ret = func()
# print(ret)
# print(name)


#
# import time
#
# def shijian(func):
#     def tongji(*args, **kwargs):
#         starttime = time.time()
#         res = func(*args,**kwargs)
#         endtime = time.time()
#         print(endtime-starttime)
#         return res
#     return tongji
#
#
# # @shijian
# # def test(name, age):
# #     time.sleep(1)
# #     print('test函数运行完毕，名字是%s，年龄是%s' %(name, age))
# #     return 'test的返回值'
# # res = test('linhaifeng',18)
# # print(res)
#
#
# @shijian
# def test1(name, age, gender):
#     time.sleep(1)
#     print('test函数运行完毕，名字是%s，年龄是%s，性别%s' %(name, age, gender))
#     return 'test的返回值'
# res = test1('linhaifeng',18, 'man')
# print(res)
#
# # res = shijian(test)
# # res()

# # a,b,c = {1,2,3}
# a,b,c = 'hec'
# print(a)
# print(b)
# print(c)


#
# l = [1,2,3,4,5,6,7,8,9]    #取列表的第一个和最后一个值
# # a,d = l[0], l[-1]
# # print(a)
# # print(d)
#
# a,*_,d=l
# print(a)
# print(d)

#
# user_list=[
#     {'name':'alex','passwd':'123'},
#     {'name':'linhaifeng','passwd':'123'},
#     {'name':'wupeiqi','passwd':'123'},
#     {'name':'yuanhao','passwd':'123'},
# ]
#
# type = {'username':None, 'login':False}
#
#
#
# def auth(auth_type='filedb'):
#     def auth_func(func):
#         def wapper(*args,**kwargs):
#             print('认证类型是', auth_type)
#             if auth_type == 'filedb':
#                 if type['username'] and type['login']:
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     username = input('please input').strip()
#                     password = input('please input').strip()
#                     for use_dic in user_list:
#                         if username == use_dic['name'] and password == use_dic['passwd']:
#                             type['username'] = username
#                             type['login'] = True
#                             res = func(*args,**kwargs)
#                             return res
#                         else:
#                             print('1111111111')
#             elif auth_type == 'ldap':
#                 print('sm gui')
#         return wapper
#     return auth_func
#
#
#
# @auth(auth_type='filedb')       #auth_func = auth(auth_type='filedb')---->>>@auth_func
# def index():
#     print('welcome to home')
#
# @auth(auth_type='ldap')
# def home(name):
#     print('lets go, %s' %name)
#
# @auth(auth_type='filedb')
# def shopping_car(name):
#     print('%s , %s , %s in your shoppingcar' %(name,'macbook','iphone'))
#
# index()
# home('project manager')
# shopping_car('monkey')


def fetch(data):
    print('This is fetch')
    print('user data is', data)
    backend_data = 'backend %s' % data
    with open('haproxy.conf', 'r') as read_f:
        tag = False
        ret = []
        for read_line in read_f:
            if read_line.strip() == backend_data:
                tag = True
                continue
            if tag and read_line.startswith('backend'):
                break
            if tag:
                print(read_line,end='')
                ret.append(read_line.strip())
    return ret




def add():
    pass


def change(data):
    print('This is change')
    print('user Transmitted data is', data)
    data[0]['backend']       #文件当中的一条记录
    res = fetch(backend)
    print(res)

def delete():
    pass


if __name__ == '__main__':
    msg = '''
    1: 查询
    2: 添加
    3: 修改
    4: 删除
    5: 退出
    '''

    msg_dic = {
        '1': fetch,
        '2': add,
        '3': change,
        '4': delete,
    }

    while True:
        print(msg)
        choice = input('please iput:').strip()
        if not choice: continue
        if choice == '5': break

        data = input('please insert your data:').strip()
        if choice != 1:
            data = eval(data)
        res = msg_dic[choice](data)
        print(res)
