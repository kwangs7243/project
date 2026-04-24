from src.response_builder import ResponseBuilder


class QueryService:
    """
    질문 타입을 받아서 알맞은 분석 메서드를 호출해서
    ResponseBuilder 클래스에 태운결과를 반환하는 클래스
   
    """

    def __init__(self, analyzer):
        self.analyzer = analyzer

    def handle(self, question_type: str, params: dict) -> dict:
        if question_type == "monthly_summary":
            return self._monthly_summary(params)

        return ResponseBuilder.error(
            question_type=question_type,
            message="지원하지 않는 질문 타입입니다.",
            error_code="UNKNOWN_QUESTION_TYPE"
        )

    def _monthly_summary(self, params: dict) -> dict:
        year = params.get("year")
        month = params.get("month")

        if (year is None) or (month is None):
            return ResponseBuilder.error(
                question_type="monthly_summary",
                message="year와 month가 필요합니다.",
                error_code="MISSING_PARAMS"
            )

        result = self.analyzer.summary_by_year_month(year, month)

        return ResponseBuilder.success(
            question_type="monthly_summary",
            message=f"{year}년 {month}월 소비 요약입니다.",
            data=result
        )