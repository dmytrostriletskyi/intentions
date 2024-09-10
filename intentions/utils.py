def is_test_function(name: str) -> bool:
    if name.startswith('test_'):
        return True

    return False
