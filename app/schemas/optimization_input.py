#optinization_modelへの入力データ形式に間違いが無いようにする
from pydantic import BaseModel

class OptimizationInput(BaseModel):
    a_coeff: float
    b_coeff: float
    constraint_rhs: float
