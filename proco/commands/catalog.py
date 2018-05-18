from .abstract_command import AbstractCommand
from ..services.state import StateHolder
from ..services.state_utils import StateUtils
from ..services.console_logger import ColorPrint
from ..services.cta_utils import CTAUtils
from ..services.catalog_handler import CatalogHandler


class Catalog(AbstractCommand):

    command = "catalog"
    args = ["[<name>]"]
    args_descriptions = {"[<name>]": "Name of the repo."}
    description = "Run: 'proco project ls' or 'proco catalog' to list all available projects in repos. \n" \
                  "  Run: 'proco project ls test' or 'proco catalog test' to list only the projects from 'test' " \
                  "repository."

    def prepare_states(self):
        StateUtils.prepare("catalog")
        StateHolder.name = StateHolder.args.get('<name>')
        StateHolder.work_dir = StateHolder.base_work_dir

    def resolve_dependencies(self):
        if StateHolder.default_catalog_repository is None:
            ColorPrint.print_warning("You have not catalog yet.", lvl=-1)
            ColorPrint.exit_after_print_messages(message=CTAUtils.CTA_STRINGS['default'], msg_type="info")
        if StateHolder.name is not None and StateHolder.name not in StateHolder.catalogs.keys():
            ColorPrint.exit_after_print_messages(message="Repository with name " + StateHolder.name + " not exists.")

    def execute(self):
        CatalogHandler.print_ls()