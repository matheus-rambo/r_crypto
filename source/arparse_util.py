def convert_string_to_bool(string:str):
    if string.lower() in ("yes", "y", "true", "t", "1"):
        return True
    else:
        return False