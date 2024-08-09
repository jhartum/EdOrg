"""Main router."""

from litestar import Router, get
from litestar.contrib.htmx.response import HTMXTemplate


@get("/", name="index")
async def index() -> HTMXTemplate:
    """Index page."""
    return HTMXTemplate(template_name="index.html")


main_router = Router(
    route_handlers=[
        index,
    ],
    path="/",
)
