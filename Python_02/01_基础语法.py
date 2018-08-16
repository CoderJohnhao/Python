"""
标识符：
- 第一个字符必须是字母表中字母或者下划线'_'
- 标识符的其他部分由字母、数字、下划线组成
- 标识符对大小写敏感
"""
bsf_1 = '123'
bsf_2 = 123
bsf_3 = True

"""
python保留字
- 保留字即是关键字，关键字是不能作为标识符名称的！
"""
import keyword
print(keyword.kwlist)

"""
注释：
- Python中单行注释以（#注释）开头
- Python中多行注释以（'''注释'''）或者（""""""）括起来
"""
# zs = 2
'''zs = 1'''
"""zs = 2"""

"""
行与缩进
- python使用缩进来表示代码块，缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
"""
if (True):
    print('行与缩进')

"""
数据类型：
python中数据有四种类型：整型、长整型、浮点数、复数
- 整型：如1
- 长整型：就是比较大的整数
- 浮点数：如1.23 3E-2
- 复数：如1+2j、1.1+3.3j
"""
sjlx_1 = 1
sjlx_2 = 2e-2
sjlx_3 = 1 + 2j

"""
字符串
- python中单引号和双引号使用完全相同
- 使用三引号可以指定一个多行字符串
- 转义符'\'
- 自然字符串，通过在字符串前加r或者R。如r'this is a line with \n'则\n会显示出来，并不是换行
- python允许处理unicode字符串，加前缀u或者U，如u'this is a an unicode string'
- 字符串是不可变的
- 按字面意义级字符串，如'this' 'is ' 'sting'会被自动转换为this is string
"""

zfc = '字符串'
zfc = "字符串"