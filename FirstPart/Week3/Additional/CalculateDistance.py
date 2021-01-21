"""
Praticar tarefa de programação: Exercícios adicionais (opcionais)

Exercício 1 - Distância entre dois pontos
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente,
às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente,
às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto
"""
import math


def get_coordinate(coordinate_name: str, cartesian_plane: str) -> float:
    return float(input(f"Digite a coordenada {coordinate_name} para o plano cartesiano {cartesian_plane}: "))


def calculate_point(coordinate_x_point_a: float, coordinate_x_point_b: float) -> float:
    return (coordinate_x_point_a - coordinate_x_point_b) ** 2


point_a = {"coordinate_x": get_coordinate("A", "X"), "coordinate_y": get_coordinate("A", "Y")}
point_b = {"coordinate_x": get_coordinate("B", "X"), "coordinate_y": get_coordinate("B", "Y")}

distance = math.sqrt((calculate_point(point_a.get("coordinate_x"), point_b.get("coordinate_x"))
                      + calculate_point(point_a.get("coordinate_y"), point_b.get("coordinate_y"))))

result = "longe" if distance >= 10 else "perto"
print(f"\n{result}")
