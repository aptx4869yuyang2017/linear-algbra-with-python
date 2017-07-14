# 我的 Udacity 线性代数学习笔记
* 课程要使用 Python 所以建个 repository 

## 
```python
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
```

* [zip 函数用法](https://docs.python.org/2.7/library/functions.html?highlight=zip#zip) 返回了一个 tuple 的列表
* [__eq__ 特殊方法](https://docs.python.org/2.7/reference/datamodel.html?highlight=__eq__#object.__eq__) 特别提醒当设定了 __eq__ 方法后建议一同设定  __ne__ 方法
* [format ](https://docs.python.org/2.7/library/string.html#formatspec) 作为一种格式化的方式，以前没使用过
## Inner Products
* [数学库的使用](https://docs.python.org/2/library/math.html) sqrt pi acos
* [Decimal](https://docs.python.org/2.7/library/decimal.html?highlight=decimal#) decimal 模型比 float 类型的优点
    * 提供了一种和人类计算方式相同的模式
    * 数字本身正确
    * 带入算数过程也精确
    * 保留 小数位计算的 0 的占位符
    * 使用可选参数，控制计算显示精度等
    * 性能可控  和上一条接近
    * 