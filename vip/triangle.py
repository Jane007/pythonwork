# @Project : pythonwork
# @File    : triangle.py
# @Author  : zhangjing
# @Time    : 2022/8/12 16:02
# @Software : Pycharm
# @Description :

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def ara(self):
        p = (self.a + self.b + self.c) / 2
        s = (p * (p - self.a) * (p - self.c) * (p - self.b)) ** 0.5
        return s


triangle = Triangle(5,5,5)
p = triangle.perimeter();
print(p)
area = triangle.ara()
print(area)