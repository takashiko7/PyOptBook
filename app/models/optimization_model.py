#最適化問題のクラスを作成，定式化
from pulp import LpMaximize, LpProblem, LpVariable

def solve_optimization(a_coeff: float, b_coeff: float, constraint_rhs: float):
    # 最適化モデルの作成
    model = LpProblem("Simple_LP", LpMaximize)
    x = LpVariable('x', lowBound=0)
    y = LpVariable('y', lowBound=0)
    model += a_coeff * x + b_coeff * y, "Objective"
    model += x + y <= constraint_rhs, "Constraint"
    model.solve()
    return {"x_value": x.varValue, "y_value": y.varValue, "objective_value": model.objective.value()}
