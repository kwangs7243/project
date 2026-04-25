import pandas as pd

class ResultSerializer:
    """
    분석결과를 JSON 변환 가능한 형태로 바꾸는 클래스
    """
    @staticmethod
    def monthly_summary(df:pd.DataFrame) -> dict:
        if df.empty:
            return {
                "수입" : 0,
                "지출" : 0,
                "순이익" : 0
            }
        return df.to_dict(orient="records")[0]
    @staticmethod
    def category_ratio(df:pd.DataFrame) -> list[dict]:
        if df.empty:
            return []
        df = df.reset_index()
        return df.to_dict(orient="records")