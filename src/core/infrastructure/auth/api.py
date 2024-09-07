import uuid
from typing import Any
from uuid import UUID

import msgspec
from litestar import Request, Response, Router, get, post
from litestar.contrib.htmx.response import HTMXTemplate
from litestar.exceptions import HTTPException

from src.core.infrastructure.auth.hash import hash_password, verify_password
from src.core.infrastructure.auth.setup import get_default_users


class User(msgspec.Struct):
    id: UUID
    username: str


# In-memory user store
users_by_id, users_by_name = get_default_users()


async def retrieve_user_handler(session: dict[str, Any], connection) -> User | None:
    return users_by_id.get(user_id) if (user_id := session.get("user_id")) else None


@post("/login_form")
async def login_form(request: Request) -> Response:
    form = await request.form()
    username: str = form.get("username", None)
    password: str = form.get("password", None)
    assert username and password

    user = users_by_name.get(username, None)
    if user and verify_password(password, user["password"]):
        request.session["user_id"] = user["id"]
        return Response(content="User logged in", status_code=200)

    return Response(content="Invalid credentials", status_code=401)


@post("/signup_form")
async def signup_form(request: Request) -> Response:
    form = await request.form()
    username: str = form.get("username", None)
    password: str = form.get("password", None)
    assert username and password

    if username in users_by_name:
        raise HTTPException(detail="Username already exists.", status_code=400)

    # Build new user
    hashed_password = hash_password(password)
    new_user = dict(id=str(uuid.uuid4()), username=username, password=hashed_password)

    # Save to in-memory store
    users_by_name[username] = new_user
    users_by_id[new_user["id"]] = dict(username=username, password=hashed_password)

    # Set the user as logged in
    request.session["user_id"] = new_user["id"]

    return Response(content="User registered", status_code=201)


@get("/login", name="login_page")
async def login_page() -> HTMXTemplate:
    """Log in page."""
    return HTMXTemplate(template_name="auth/login.html")


@get("/signup", name="signup_page")
async def signup_page() -> HTMXTemplate:
    """Sign up page."""
    return HTMXTemplate(template_name="auth/signup.html")


router = Router(
    route_handlers=[login_form, signup_form, login_page, signup_page],
    path="/auth",
)
