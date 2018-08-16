"""
python中的变量不需要声明，每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
在python中，变量就是变量，他没有类型，我们所说的"类型"是变量所指的内存中对象的类型
python3中有六个数据类型：
- numbers（数字）
- string（字符串）
- list（列表/数组）
- tuple（元组）
- sets（集合）
- dictionaries（字典）
"""

"""
Numbers（数字）
python3支持int、float、bool、complex

注意：
- python可以同时为多个变量赋值，如a，b = 1，3
- 一个变量可以通过赋值指向不同的类型的对象
- 数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符
- 在混合计算是，python会把整数转换成浮点数
"""
a = 5
b = 2.0
c = True
d = 5 + 4j
print(type(a), type(b), type(c), type(d))

"""
String（字符串）
- python中的字符串str用单引号('')或双引号("")括起来，同时使用反斜杠(\)转义特殊字符
- 如果你不想让反斜杠发生转义，可以在字符串前面添加一个r，表示原始字符串
- 反斜杠可以作为连续符，表示下一行是上一行的延续，还可以使用('''...''')跨越多行，
也可以使用(+)运算符链接在一起，或者用(*)运算符重复。
- python中字符串有两种索引方式，第一种是从左往右，从0开始依次增加；第二种是从右往左，从-1开始依次减少。
- 对字符串进行切片，获取一段子字符串，用冒号分割连个索引，形式为变量[头下标:尾下标]，截取范围是前闭后开，并且两个索引是可以省略
注意：
- 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
- 字符串可以用+运算符连接在一起，用*运算符重复
- python中字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
- python中字符串不能改变
"""
zfc_1 = "yes, he doesn't."
print(zfc_1, type(zfc_1), len(zfc_1))
print('C:\some\name')
print(r'c:\some\name')
print('str' + 'ing', 'my'*3)
print(zfc_1[0])
print(zfc_1[-1])
print(zfc_1[2:6])

"""
List（列表/数组）
- 列表是写在方括号之间、用逗号分隔开的元素列表，列表中元素类型可以不同
注意：
- list写在方括号之间，元素用逗号隔开
- 和字符串一样，list可以被索引和切片
- list可以使用+操作符进行拼接
- list中的元素是可以改变的
"""
sz_01 = ['him', 25, 100, 'her']
print(sz_01)
sz_02 = [1, 2, 3, 4, 5]
sz_03 = sz_02 + [6, 7, 8]
print(sz_02)
print(sz_03[0])
print(sz_03[-1])
print(sz_03[1:3])


"""
Tuple（元组）
- 元组与列表类似，不同之处在于元组的元素不能修改，元组写在小括号里面，元素之间用逗号隔开
- 元组可以进行索引和切片
- 元组支持+操作符
注意：
- 与字符串一样，元组的元素不能修改
- 元组也可以被索引和切片，方法一样
- 注意构造包含0和1个元素的元组的特殊语法规则
- 元组也可以使用+操作符
"""
yz_01 = (1994, 'johnhao',  'man')
print(yz_01, type(yz_01), len(yz_01))
yz_02 = (1, 2, 3, 4, 5, 6)
print(yz_02[0], yz_02[1:4])
yz_03 = yz_01 +  yz_02
print(yz_03)

"""
Sets（集合）
- 集合是一个无序不重复元素的集
- 基本功能是进行成员关系测试和消除重复元素
- 可以使用打括号或者set()函数创建set集合
注意：
- 创建一个空集合必须使用set函数而不是{},因为{}是用来创建一个空字典
"""
jh_01 = {'tom', 'jim', 'tom', 'john', 'jack'}
print(jh_01)
jh_02 = set('absafsdlkdsfa')
jh_03 = set('uojodajkpkdfkag')
print(jh_02, jh_03)
# 差集
print(jh_02 - jh_03)
# 并集
print(jh_02 | jh_03)
# 交集
print(jh_02 & jh_03)
# 都不存在的元素
print(jh_02 ^ jh_03)

"""
Dictionaries（字典）
- 字典是一种映射类型。他是无序的键:值对集合
- 关键字必须使用不可变类型，也就是list和包含可变类型的tuple不能做关键字
- 在同一个字典中，关键字还必须互不相同
"""
zd_01 = {}
zd_02 = {'name': 'johnhao', 'age': 24, 'sex': 'man'}
print(zd_02)
print(zd_02['name'])
zd_02['age'] = 25
print(zd_02)
print(list(zd_02.keys()))
print(list(zd_02.values()))
print(sorted(zd_02.keys()))
print('name' in zd_02)
print('age' not in zd_02)
zd_03 = dict([('name', 'john'), ('age', 23)])
print(zd_03)
zd_04 = dict(name='john', age=24)
print(zd_04)