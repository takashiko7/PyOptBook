#ここでリクエストを受取り，models/optimization_modelsの最適化関数を呼び出して結果を返す
from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from ..schemas.optimization_input import OptimizationInput
from ..models.optimization_model import solve_optimization
import os

router = APIRouter()

@router.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)): #File(...) ファイルのアップロードが必要であることを示す
    try:
        # ファイルを temp フォルダに保存
        temp_dir = "app/temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        file_location = os.path.join(temp_dir, file.filename)

        with open(file_location, "wb") as buffer:
            buffer.write(await file.read())

        # CSV ファイルを pandas データフレームとして読み込み
        df = pd.read_csv(file_location)

        # データフレームから Pydantic モデルのリストに変換
        input_data = OptimizationInput(
            a_coeff=df['a_coeff'][0],
            b_coeff=df['b_coeff'][0],
            constraint_rhs=df['constraint_rhs'][0]
        )

        # 最適化計算を実行
        result = solve_optimization(input_data)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
