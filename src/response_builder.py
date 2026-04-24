class ResponseBuilder:
    """
    JSON으로 변환할 데이터를 통일해주는 클래스
    """
    @staticmethod
    def success(question_type:str, message:str, data=None, meta=None) -> dict:
        return {
            "ok" : True,
            "question_type" : question_type,
            "message" : message,
            "data" : data if data is not None else {},
            "meta" : meta if meta is not None else {}
        }
    
    @staticmethod
    def error(question_type:str, message:str, error_code:str, meta=None) -> dict:
        error_meta = {
            "error_code" : error_code
        }
        if meta is not None:
            error_meta.update(meta)
        return {
            "ok" : False,
            "question_type" : question_type,
            "message" : message,
            "data" : None,
            "meta" : error_meta
        }
