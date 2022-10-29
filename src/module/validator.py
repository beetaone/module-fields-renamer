"""
Validates whether the incoming data has an acceptable type and structure.

Edit this file to verify data expected by you module.
"""

import os
from logging import getLogger

log = getLogger("validator")

__OLD_NAMES__ = []
if os.getenv("RENAME_FIELDS"):
    raw_mappings = [field.strip() for field in os.getenv("RENAME_FIELDS").split(',')]
    for mapping in raw_mappings:
        old_name, _ = mapping.split('=')
        __OLD_NAMES__.append(old_name)

def data_validation(data: any) -> str:
    """
    Validate incoming data i.e. by checking if it is of type dict or list.
    Function description should not be modified.

    Args:
        data (any): Data to validate.

    Returns:
        str: Error message if error is encountered. Otherwise returns None.

    """

    log.debug("Validating ...")

    try:
        allowed_data_types = [dict, list]

        if not type(data) in allowed_data_types:
            return f"Detected type: {type(data)} | Supported types: {allowed_data_types} | invalid!"

        if type(data) == list:
            for d in data:
                unmatched_names = []
                for name in __OLD_NAMES__:
                    if not name in d.keys():
                        unmatched_names.append(name)
                if unmatched_names:
                    return f"Labels to rename {unmatched_names} are not present in received data labels: {list(d.keys())}."
        else:
            unmatched_names = []
            for name in __OLD_NAMES__:
                if not name in data.keys():
                    unmatched_names.append(name)
            if unmatched_names:
                return f"Labels to rename {unmatched_names} are not present in received data labels: {list(data.keys())}."

        return None

    except Exception as e:
        return f"Exception when validating module input data: {e}"
