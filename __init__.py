# ----- Imports ---------------------------------------------------------------

from .dsh import dsh
from importlib.machinery import SourceFileLoader
from tinyAPI.base.config import ConfigManager
from tinyAPI.base.context import *
from tinyAPI.base.data_store.memcache import Memcache
from tinyAPI.base.data_store.exception import ColumnCannotBeNullException
from tinyAPI.base.data_store.exception import DataStoreDuplicateKeyException
from tinyAPI.base.data_store.provider import DataStoreMySQL
from tinyAPI.base.services.table_builder.mysql import Table, RefTable, View
from tinyAPI.base.services.table_builder.reference import refv

import tinyAPI.base.data_store.ConnectionManager
import os

# ----- Public Functions ------------------------------------------------------

def load_reference_definitions(ref_defs_file):
    if ref_defs_file is not None:
        # Define a trusted directory to restrict module loading
        trusted_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'reference_definitions'))
        # Resolve the absolute path of the provided file
        abs_path = os.path.abspath(ref_defs_file)
        # Ensure the file is inside the trusted directory
        if not abs_path.startswith(trusted_dir + os.sep):
            raise ValueError(f"Attempted to load reference definitions from an untrusted location: {ref_defs_file}")
        loader = SourceFileLoader('reference_definition', abs_path)
        loader.load_module('reference_definition')

# ----- Instructions ----------------------------------------------------------

load_reference_definitions(ConfigManager.value('reference definition file'))
