# def unused_digits(*args):
#     num = list(map(str, range(10)))
#     res = ''
#     for arg in args:
#         arg = str(arg)
#         for i in range(len(arg)):
#             if arg[i] in num:
#                 num.remove(arg[i])
#     for n in num:
#         res += n
#     return res
#
#
# print(unused_digits(12, 34, 56, 78))

# def calc(equation):
#     res = 0
#     tmp = '00'
#     for e in equation:
#         if e != '+' and e != '-':
#             tmp += e
#         elif e == '+':
#             if tmp[0] == '-':
#                 res -= int(tmp[2:])
#                 tmp = '00'
#             else:
#                 res += int(tmp[1:])
#                 tmp = '00'
#             tmp = '+' + tmp
#         elif e == '-':
#             if tmp[0] == '-':
#                 res -= int(tmp[2:])
#                 tmp = '00'
#             else:
#                 res += int(tmp[1:])
#                 tmp = '00'
#             tmp = '-' + tmp
#     if tmp[0] == '-':
#         res -= int(tmp[2:])
#     else:
#         res += int(tmp[1:])
#     return res
# print(calc('123+2-124'))
# print(calc('-12+12-7979+9191'))
# print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))


# print(dir(list))
# print(dir(str))
# print(dir(dict))

# class Circle:
# #     pi = 3.14
# #     x = 0
# #     y = 0
# #     r = 0
# #
# #     def __init__(self, x, y, r):
# #         self.r = r
# #         self.x = x
# #         self.y = y
# #
# #     def area(self):
# #         return self.pi * self.r * self.r
# #
# #     def circumstance(self):
# #         return 2 * self.pi * self.r
# #
# #     def center(self):
# #         return (self.x, self.y)
# #
# # circle = Circle(2, 4, 3)
# # print(circle.area())
# # print(circle.circumstance())


# class Calculator:
#     count = 0
#
#     def info(self):
#         print('나는 계산기 입니다.')
#
#     @staticmethod
#     def add(a, b):
#         Calculator.count += 1
#         print(f'{a} + {b}는 {a+b}입니다.')
#
#     @classmethod
#     def history(cls):
#         print(f'총 {cls.count}번 계산했습니다.')
#
# cal = Calculator()
#


class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


