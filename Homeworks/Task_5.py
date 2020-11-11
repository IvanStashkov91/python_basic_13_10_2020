'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class ComplexNumber:

    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        return f'{complex(self.real_part, self.imaginary_part) + complex(other.real_part, other.imaginary_part)}'

    def __mul__(self, other):
        return complex(self.real_part, self.imaginary_part) * complex(other.real_part, other.imaginary_part)

if __name__ == '__main__':
    a = ComplexNumber(-4.5, 4)
    b = ComplexNumber(5, -6)
    print(a + b)
    print(a * b)
