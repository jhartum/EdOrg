from src.infrastructure.auth.hash import hash_password
from src.infrastructure.settings import app_settings

SUPERUSER_MAGIC_ID = "68c754cc-7e03-4fb3-ac3c-6bb47016d375"


def get_default_users() -> tuple[dict, dict]:
    return (
        {
            SUPERUSER_MAGIC_ID: dict(
                username=app_settings.admin_username,
                password=hash_password(app_settings.admin_password),
            ),
        },
        {
            app_settings.admin_username: dict(
                id=SUPERUSER_MAGIC_ID,
                username=app_settings.admin_username,
                password=hash_password(app_settings.admin_password),
            ),
        },
    )
