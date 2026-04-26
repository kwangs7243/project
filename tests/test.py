from src.data_analyzer import DataAnalyzer
from src.expense_analyzer import ExpenseAnalyzer
from src.query_service import QueryService
from src.result_serializer import ResultSerializer as rs
import pandas as pd
import json
da = DataAnalyzer()
da.load_data("data/raw/realistic_expense_1000.csv")
da.preprocess_data()
ea = ExpenseAnalyzer(da.get_analysis_data())
qs = QueryService(ea)
question_type = "monthly_summary"
params = {
    "year" : 2025,
    "month" : 1
}
result = rs.month_summary(ea.summary_by_month())
print(json.dumps(result,ensure_ascii=False,indent=2))
# print(ea.summary_by_month().reset_index().to_dict(orient="records"))
# print(result.dtypes if hasattr(result, "dtypes") else "No dtypes")