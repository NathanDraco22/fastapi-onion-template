from pathlib import Path
from onion.mediators import Mediator
from onion.utils.string_utils import (
    get_mongo_collection_filename,
    get_entity_name_variations,
)
from onion.templates.mongo_collection_template import (
    get_mongo_collection_class_template,
)
from onion.utils.file_utils import gen_init

from .create_mongo_service import create_mongo_service


def create_mongo_collection(input_name: str, version: int) -> None:
    name = get_entity_name_variations(input_name).single_name

    # check "app" folder
    app_folder = Path("app")
    if not app_folder.exists():
        app_folder.mkdir()

    # check "app/services" folder
    service_folder = app_folder / "services"
    if not service_folder.exists():
        service_folder.mkdir()

    # check "app/services/mongo_service.py" file
    mongo_service_file = service_folder / "mongo_service.py"
    if not mongo_service_file.exists():
        create_mongo_service()

    mongo_collection_folder = service_folder / "mongo_collections"
    if not mongo_collection_folder.exists():
        mongo_collection_folder.mkdir()

    # check "app/services/mongo_collections/v{version}" folder
    version_folder = mongo_collection_folder / f"v{version}"
    if not version_folder.exists():
        version_folder.mkdir()

    # check "app/services/mongo_collection.py"
    mongo_collection_file = version_folder / get_mongo_collection_filename(name)
    if not mongo_collection_file.exists():
        mongo_collection_file.touch()

    mongo_collection_file.write_text(get_mongo_collection_class_template(name))

    gen_init(version_folder)

    Mediator().output_folders.append(
        f"app/services/mongo_collections/v{version}/{name}.py",
    )
