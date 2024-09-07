"""Factory for the Litestar app."""

from jinja2 import Environment, FileSystemLoader, select_autoescape
from litestar import Litestar
from litestar.contrib.htmx.request import HTMXRequest
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.plugins.flash import FlashConfig, FlashPlugin
from litestar.static_files import create_static_files_router
from litestar.stores.file import FileStore
from litestar.template import TemplateConfig

from src.core.infrastructure.app import lifespan
from src.core.infrastructure.auth import session_auth
from src.core.infrastructure.settings import AppSettings


def create_app(app_settings: AppSettings) -> Litestar:
    """Create the Litestar app."""

    from src.core.application.api import index, news
    from src.core.infrastructure.auth import api as auth

    template_config = TemplateConfig(
        instance=JinjaTemplateEngine.from_environment(
            Environment(
                loader=FileSystemLoader(app_settings.templates_dir),
                lstrip_blocks=True,
                trim_blocks=True,
                autoescape=select_autoescape(
                    enabled_extensions=("html",),
                    default_for_string=True,
                ),
            )
        )
    )
    statics = [
        create_static_files_router(
            path="/static",
            directories=[
                app_settings.static_dir,
                app_settings.root_dir.parent / "node_modules",
                app_settings.db_dir / "news_article_images",
            ],
        ),
    ]

    return Litestar(
        route_handlers=[
            *statics,
            index.router,
            auth.router,
            news.router,
        ],
        on_app_init=[session_auth.on_app_init],
        template_config=template_config,
        debug=app_settings.debug,
        request_class=HTMXRequest,
        plugins=[FlashPlugin(config=FlashConfig(template_config=template_config))],
        stores={"sessions": FileStore(path=app_settings.session_store_dir)},
        lifespan=[lifespan.tailwind],
    )
