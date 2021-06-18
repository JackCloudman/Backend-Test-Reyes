from uuid import UUID


def validate_uuid(uuid):
    """
    Function that validate uuid
    Params:
        UUID: string
    Return:
        True if uuid is valid else False.
    """
    # Just trying to parse string to UUID
    try:
        UUID(uuid)
        return True
    # Not UUID valid
    except ValueError:
        return False
