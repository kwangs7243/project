import pandas as pd

class ExpenseAnalyzer:
    """
    전처리된 가계부 데이터를 조회, 요약, 순위 형태로 분석하는 클래스.
    """

    def __init__(self,data:pd.DataFrame):
        """
        분석에 사용할 데이터프레임을 저장한다.
        """
        self.df = data


#======================================조회 기능===========================================
    def _filter_by_year_month(self,data:pd.DataFrame,year:int,month:int) -> pd.DataFrame:

        return data[(data["year"]==year) & (data["month"]==month)]


    def _filter_by_date_range(self,data:pd.DataFrame, start_date:pd.Timestamp, end_date:pd.Timestamp) -> pd.DataFrame:
        
        return data[(data["date"] >= start_date) & (data["date"] <= end_date)]

    def _filter_by_type(self,data:pd.DataFrame, type_name:str) -> pd.DataFrame:
        return data[data["type"]==type_name]

    def _filter_by_category(self,data:pd.DataFrame, category_name:str) -> pd.DataFrame:
        
        return data[data["category"]==category_name]

    def _filter_by_min_amount(self,data:pd.DataFrame, min_amount:int) -> pd.DataFrame:
        
        return data[data["amount"] >= min_amount]

    def _filter_by_keyword(self,data:pd.DataFrame, keyword:str="") -> pd.DataFrame:
        
        return data[data["content"].str.contains(keyword,na=False)]

    #======================================조회 기능===========================================

    #======================================요약 기능===========================================

    def _summary_total(self,data:pd.DataFrame) -> pd.DataFrame:
        """
        데이터를 총수입,총지출,순이익 으로 요약하여 재구성
        """
        summary_data = data.pivot_table(columns="type", values="amount", aggfunc="sum", fill_value=0)
        summary_data.columns = ["총수입","총지출"]
        summary_data["순이익"] = summary_data["총수입"] - summary_data["총지출"]
        return summary_data

    def _summary_by_year_month(self,data:pd.DataFrame) -> pd.DataFrame:
        """
        데이터를 월별 수입,지출,순이익으로 요약하여 재구성
        """
        summary_data = (
            data.groupby(["year_month","type"])["amount"]
            .sum()
            .unstack(fill_value=0)
            .reindex(columns=["수입","지출"],fill_value=0)
        )
        summary_data["순이익"] = summary_data["수입"] - summary_data["지출"]
        return summary_data

    def _summary_by_category_type(self, data:pd.DataFrame, type_name:str=None) -> pd.DataFrame:
        """
        데이터를 카테고리별 수입,지출로 요약하여 재구성
        """
        summary_data = (
            data.groupby(["category","type"])["amount"]
            .sum()
            .unstack(fill_value=0)
            .reindex(columns=["수입","지출"],fill_value=0)
        )
        if type_name is not None:
            return summary_data[[type_name]]
        return summary_data

    def _summary_count_by_category(self, data:pd.DataFrame) -> pd.Series:
        """
        데이터를 카테고리별로 카운트
        """
        
        return data.groupby("category").size()

    #======================================요약 기능===========================================

    #======================================순위 기능===========================================

    def _get_top_n(self,data:pd.DataFrame, n:int) -> pd.DataFrame:
        """
        데이터를 금액이 큰 상위 n개로 재구성
        """
        return (
            data
            .sort_values(by="amount", ascending=False)
            .head(n)
        )

    #======================================순위 기능===========================================


    #======================================비교 기능===========================================

    def _compare_months(self,base_data:pd.DataFrame,target_data:pd.DataFrame) -> pd.DataFrame:
        """
        두 데이터를 나열하여 증감, 증감률을 계산
        """
        compare_data = pd.concat([base_data,target_data], axis=1)
        base_col,target_col = compare_data.columns

        compare_data["증감"] = compare_data[target_col] - compare_data[base_col]
        compare_data["증감률"] = (
            compare_data["증감"] / compare_data[base_col].replace(0, pd.NA) * 100
            ).fillna(0).round(2)

        return compare_data

    #======================================비교 기능===========================================

    #======================================통계 기능===========================================

    def _average_amount_by_category_type(self, data:pd.DataFrame, type_name:str=None) -> pd.DataFrame:
        """
        데이터를 카테고리별 수입,지출 평균값으로 요약
        """
        average_data = (
            data.groupby(["category","type"])["amount"]
            .mean()
            .unstack(fill_value=0)
            .reindex(columns=["수입","지출"], fill_value=0)
            .round(0)
            .astype(int)
            )
        if type_name is not None:
            return average_data[[type_name]]
        return average_data

    def  _average_amount_by_year_month_type(self, data:pd.DataFrame, type_name:str=None) -> pd.date_rangea:
        """
        데이터를 연월별 수입,지출 평균값으로 요약
        """
        average_data = (
            data.groupby(["year_month","type"])["amount"]
            .mean()
            .unstack(fill_value=0)
            .reindex(columns=["수입","지출"], fill_value=0)
            .round(0)
            .astype(int)
            )
        if type_name is not None:
            return average_data[[type_name]]
        return average_data
    def _calculate_ratio(self,data:pd.DataFrame,type_name:str) -> pd.DataFrame:
        """
        데이터에서 입력받은 타입에서 비중을 계산한다
        """
        ratio_data = data.copy()
        total = ratio_data[type_name].sum()

        if total == 0:
            ratio_data["비중"] = 0
            return ratio_data
        
        ratio_data["비중"] =(
            (ratio_data[type_name] / total)*100
            ).round(0).astype(int)
        return ratio_data
    def _summary_excess_amount_vs_average(self,data:pd.DataFrame):
        pass


    #======================================통계 기능===========================================
