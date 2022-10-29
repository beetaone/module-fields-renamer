"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
import os

log = getLogger("module")

names_mapping = {}

if os.getenv("RENAME_FIELDS"):
    raw_mappings = [field.strip() for field in os.getenv("RENAME_FIELDS").split(',')]
    for mapping in raw_mappings:
        old_name, new_name = mapping.split('=')
        names_mapping[old_name] = new_name

def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        if type(received_data) == list:
            processed_data = []

            for data in received_data:
                sub_data = {}
                for k, v in data.items():
                    # rename keys without changing the order
                    if k in names_mapping.keys():
                        sub_data[names_mapping[k]] = v
                    else:
                        sub_data[k] = v
                processed_data.append(sub_data)

        else:
            processed_data = {}

            for k, v in received_data.items():
                # rename keys without changing the order
                if k in names_mapping.keys():
                    processed_data[names_mapping[k]] = v
                else:
                    processed_data[k] = v

        return processed_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
