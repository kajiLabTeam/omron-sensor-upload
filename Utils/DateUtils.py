from datetime import datetime


class DateUtils:
    def __init__(self):
        pass

    @staticmethod
    def now_utc_str() -> str:
        """
        Get now utc.
        """
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    
    @staticmethod
    def now_utc() -> datetime:
        """
        Get now utc.
        """
        return datetime.utcnow()
    
    @staticmethod
    def now_timestamp() -> int:
        """
        Get now timestamp.
        """
        return int(datetime.utcnow().timestamp())