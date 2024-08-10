"""Factory for the Litestar app."""

from jinja2 import Environment, FileSystemLoader, select_autoescape
from litestar import Litestar
from litestar.contrib.htmx.request import HTMXRequest
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.middleware.session.server_side import ServerSideSessionConfig
from litestar.plugins.flash import FlashConfig, FlashPlugin
from litestar.static_files import create_static_files_router
from litestar.template import TemplateConfig

from src.application.app import lifespan
from src.infrastucture.db.session import get_db_session
from src.infrastucture.settings import AppSettings


def create_app(app_settings: AppSettings) -> Litestar:
    """Create the Litestar app."""

    from src.application.routers.main import index_router

    template_config = TemplateConfig(
        instance=JinjaTemplateEngine.from_environment(
            Environment(
                loader=FileSystemLoader(
                    app_settings.root_dir / "infrastucture" / "templates"
                ),
                lstrip_blocks=True,
                trim_blocks=True,
                autoescape=select_autoescape(
                    enabled_extensions=("html",),
                    default_for_string=True,
                ),
            )
        )
    )
    flash_plugin = FlashPlugin(config=FlashConfig(template_config=template_config))

    return Litestar(
        route_handlers=[
            create_static_files_router(
                path="/static",
                directories=[app_settings.root_dir / "infrastucture" / "static"],
            ),
            index_router,
        ],
        template_config=template_config,
        debug=app_settings.debug,
        request_class=HTMXRequest,
        plugins=[flash_plugin],
        middleware=[ServerSideSessionConfig().middleware],
        lifespan=[lifespan.tailwind],
        dependencies={"db_session": get_db_session},
    )
