from fastapi import APIRouter


backup_router_v1 = APIRouter(prefix="/v1/backup", tags=["v1.backup"])


@backup_router_v1.post("")
def create_backup():
    pass


@backup_router_v1.delete("")
def delete_backup():
    pass
