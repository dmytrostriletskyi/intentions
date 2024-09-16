def is_test_function(name: str) -> bool:
    if name.startswith('test_'):
        return True

    return False


def convert_test_function_name_to_case_name(test_function_name: str) -> str:
    test_function_name = test_function_name.replace('test_', '')
    test_function_name = test_function_name.replace('_', ' ')
    test_function_name = test_function_name.capitalize()

    return test_function_name
