from src.response_builder import ResponseBuilder
from src.result_serializer import ResultSerializer as rs
from src.expense_analyzer import ExpenseAnalyzer
class QueryService:
    """
    질문 타입을 받아서 알맞은 분석 메서드를 호출해서
    ResponseBuilder 클래스에 태운결과를 반환하는 클래스
   
    """

    def __init__(self, analyzer:ExpenseAnalyzer):
        self.analyzer = analyzer

    def handle(self, question_type: str, params: dict) -> dict:
        
        if question_type == "total_summary":
            return self._total_summary(params)
        if question_type == "monthly_summary_list":
            return self._monthly_summary_list(params)
        if question_type == "monthly_summary":
            return self._monthly_summary(params)
        if question_type == "category_ratio":
            return self._category_ratio(params)

        return ResponseBuilder.error(
            question_type=question_type,
            message="지원하지 않는 질문 타입입니다.",
            error_code="UNKNOWN_QUESTION_TYPE"
        )
    def _total_summary(self, params: dict) -> dict:
        result = self.analyzer.summary_total()
        data = rs.total_summary(result)
        return ResponseBuilder.success(
            question_type="total_summary",
            message="전체 요약입니다.",
            data=data
        )
    
    def _monthly_summary_list(self, params: dict) -> dict:
        result = self.analyzer.summary_by_month()
        data = rs.monthly_summary_list(result)
        return ResponseBuilder.success(
            question_type="month_summary",
            message="월별 요약입니다.",
            data=data
        )
    
    def _monthly_summary(self, params: dict) -> dict:
        year = params.get("year")
        month = params.get("month")
        if (year is None) or (year == "") or (month == "") or (month is None):
            return ResponseBuilder.error(
                question_type="monthly_summary",
                message="연이나 월이 입력되지 않았습니다.",
                error_code="MISSING_PARAMS"
            )
        try:
            year = int(year)
            month = int(month)
        except(ValueError, TypeError):
            return ResponseBuilder.error(
                question_type= "monthly_summary",
                message= "연과 월은 숫자여야 합니다.",
                error_code= "INVALID_TYPE"
            )
        if not ( 1 <= month <= 12 ):
            return ResponseBuilder.error(
                question_type="monthly_summary",
                message= "월은 1~12사이여야 합니다",
                error_code= "INVALID_RANGE"
            )


        result = self.analyzer.summary_by_year_month(year, month)
        data = rs.monthly_summary(result)

        return ResponseBuilder.success(
            question_type="monthly_summary",
            message=f"{year}년 {month}월 소비 요약입니다.",
            data=data
        )
    def _category_ratio(self, params:dict) -> dict:
        result = self.analyzer.summary_category_expense_ratio()
        data = rs.category_ratio(result)
        return ResponseBuilder.success(
            question_type="category_ratio",
            message="카테고리별 지출 비중입니다",
            data=data
        )