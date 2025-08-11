from typing import List, Optional
from app.core.exception import BaseServiceExceptionHandler

service_code = "001"


class BaseBackupExceptionHandler(BaseServiceExceptionHandler):
    def __init__(
        self,
        message: str = "Internal server error (backup exception)",
        status_code: int = 500,
        custom_status_code: Optional[str] = None,
    ):
        super().__init__(
            service_code=service_code,
            status_code=status_code,
            message=message,
            custom_status_code=custom_status_code,
        )


backup_exceptions: List[type[BaseServiceExceptionHandler]] = [
    BaseBackupExceptionHandler,
]
