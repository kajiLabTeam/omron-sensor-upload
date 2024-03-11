from datetime import datetime


class DateUtils:
    def __init__(self):
        pass

    @staticmethod
    def now_utc_str() -> str:
        """
        Get now utc.
        """
        return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")