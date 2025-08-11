import os


class DatabaseSettings:
    SQLITE_FILE = os.getenv("SQLITE_FILE", "")


class StorageSettings:
    R2_STORAGE_ENDPOINT = os.getenv("R2_STORAGE_ENDPOINT")


class Settings(
    StorageSettings,
    DatabaseSettings,
):
    pass


settings = Settings()
