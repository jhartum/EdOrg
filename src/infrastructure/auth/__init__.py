from litestar.middleware.session.server_side import (
    ServerSideSessionBackend,
    ServerSideSessionConfig,
)
from litestar.security.session_auth import SessionAuth

from src.infrastructure.auth.api import User, retrieve_user_handler

session_auth = SessionAuth[User, ServerSideSessionBackend](
    retrieve_user_handler=retrieve_user_handler,
    session_backend_config=ServerSideSessionConfig(),
    exclude=[
        "/auth/login",
        "/static",
        "/auth/login_form",
    ],
)
