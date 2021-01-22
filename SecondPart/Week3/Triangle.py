"""
Tarefa de programação: Lista de exercícios - 3

Exercício 1: Uma classe para triângulos
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo.

A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros e
devolve um valor inteiro correspondente ao perímetro do triângulo.

# deve atribuir uma referência para um triângulo de lados 1, 1 e 1 à variável t

Um objeto desta classe deve responder às seguintes chamadas:

t.a
# deve devolver o valor do lado a do triângulo
t.b
# deve devolver o valor do lado b do triângulo
t.c
# deve devolver o valor do lado c do triângulo

t.perimetro()
# deve devolver um inteiro correspondente ao valor do perímetro do triângulo.

-----------------------------------------------------------------------------

Exercício 2: Tipos de triângulos

Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado()
que devolve uma string dizendo se o triângulo é:

isósceles (dois lados iguais)

equilátero (todos os lados iguais)

escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não deve devolver isóceles.

Exemplos:

t = Triangulo(4, 4, 4)
t.tipo_lado()
# deve devolver 'equilátero'

u = Triangulo(3, 4, 5).tipo_lado()
# deve devolver 'escaleno'
"""


# Mudar nome da classe no envio da terefa para o mesma do exemplo, Triangulo.
class Triangle:
    SCALENE, ISOSCELES, EQUILATERAL = "escaleno", "isósceles", "equilátero"

    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    # Mudar nome da função no envio da terefa para o mesma do exemplo, perimetro().
    def perimeter(self) -> int:
        return self.a + self.b + self.c

    def get_total_sides(self) -> int:
        return len({self.a, self.b, self.c})

    # Mudar nome da função no envio da terefa para o mesma do exemplo, tipo_lado().
    def type_side(self) -> str:
        total_sides = self.get_total_sides()

        if total_sides == 3:
            return self.SCALENE

        if total_sides == 2:
            return self.ISOSCELES

        return self.EQUILATERAL
