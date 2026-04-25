from flask import Flask, request, jsonify, render_template
from src.data_analyzer import DataAnalyzer
from src.expense_analyzer import ExpenseAnalyzer
from src.query_service import QueryService
da = DataAnalyzer()
da.load_data("data/raw/realistic_expense_1000.csv")
da.preprocess_data()
ea = ExpenseAnalyzer(da.get_analysis_data())
qs = QueryService(ea)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/api/query", methods=["POST"])
def query():
    req:dict = request.get_json(silent=True) or {}

    question_type = req.get("question_type")
    params = req.get("params") or {}
    response = qs.handle(question_type, params)

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)