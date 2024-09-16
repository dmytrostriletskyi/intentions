import json

from intentions.main import (
    case,
    expect,
    when,
)
from intentions.render.main import create_intentions_json


class TestRender:

    def test_create_intentions_json(self, remove_intentions_json) -> None:
        with when('Tests folder with tests using intentions library exists'):
            path_to_tests_folder = './fixtures'

        with case('Create intentions JSON file'):
            create_intentions_json(directory=path_to_tests_folder)

        with open('./.intentions/intentions.json', 'r') as intentions_json:
            intentions_json = json.load(intentions_json)

        with expect('First intentions JSON keys corresponds to domains'):
            assert intentions_json['accounts'] is not None
            assert intentions_json['investments'] is not None

        with expect('Each intentions JSON domain consist of its objects'):
            assert intentions_json['accounts']['accounts']['service']
            assert intentions_json['investments']['investments']['service']

    def test_create_intentions_json_accounts_service(self, remove_intentions_json) -> None:
        with when('Tests folder with tests for accounts service exist'):
            path_to_tests_folder = './fixtures'

        with case('Create intentions JSON file'):
            create_intentions_json(directory=path_to_tests_folder)

        with open('./.intentions/intentions.json', 'r') as intentions_json:
            intentions_json = json.load(intentions_json)

        with expect('Test transfer money with insufficient balance test case is in accounts service test cases'):
            expected_test_case = {
                'file_path': 'fixtures/test_file.py',
                'class_name': 'TestAccountsService',
                'class_code_line': 10,
                'case_name': 'Transfer money with insufficient balance',
                'function_name': 'test_transfer_money_with_insufficient_balance',
                'function_code_line': 12,
                'intentions': [
                    {
                        'type': 'when',
                        'code_line': 13,
                        'description': 'Sender account has insufficient balance',
                    },
                    {
                        'type': 'case',
                        'code_line': 16,
                        'description': 'Transfer money from one sender to receiver',
                    },
                    {
                        'type': 'expect',
                        'code_line': 19,
                        'description': 'No transfers have been made',
                    }
                ]
            }

            assert expected_test_case in intentions_json['accounts']['accounts']['service']

        with expect('Test transfer money with sufficient balance test case is in accounts service test cases'):
            expected_test_case = {
                'file_path': 'fixtures/test_file.py',
                'class_name': 'TestAccountsService',
                'class_code_line': 10,
                'case_name': 'Transfer money with sufficient balance',
                'function_name': 'test_transfer_money_with_sufficient_balance',
                'function_code_line': 22,
                'intentions': [
                    {
                        'type': 'when',
                        'code_line': 23,
                        'description': 'Sender account has sufficient balance',
                    },
                    {
                        'type': 'case',
                        'code_line': 26,
                        'description': 'Transfer money from one sender to receiver',
                    },
                    {
                        'type': 'expect',
                        'code_line': 29,
                        'description': 'Sender account balance decreased on the transfer money amount',
                    }
                ]
            }

            assert expected_test_case in intentions_json['accounts']['accounts']['service']

        with expect('Test transfer money to non existing receiver account test case is in accounts service test cases'):
            expected_test_case = {
                'file_path': 'fixtures/test_file.py',
                'class_name': None,
                'class_code_line': None,
                'case_name': 'Transfer money to non existing receiver account',
                'function_name': 'test_transfer_money_to_non_existing_receiver_account',
                'function_code_line': 34,
                'intentions': [
                    {
                        'type': 'when',
                        'code_line': 35,
                        'description': 'Receiver account does not exist',
                    },
                    {
                        'type': 'case',
                        'code_line': 38,
                        'description': 'Transfer money from one sender to receiver',
                    },
                    {
                        'type': 'expect',
                        'code_line': 41,
                        'description': 'Receiver account does not exist error is raised',
                    }
                ]
            }

            assert expected_test_case in intentions_json['accounts']['accounts']['service']

    def test_create_intentions_json_investments_service(self, remove_intentions_json) -> None:
        with when('Tests folder with tests for investments service exist'):
            path_to_tests_folder = './fixtures'

        with case('Create intentions JSON file'):
            create_intentions_json(directory=path_to_tests_folder)

        with open('./.intentions/intentions.json', 'r') as intentions_json:
            intentions_json = json.load(intentions_json)

        with expect('Invest money into stocks test case is in investments service test cases'):
            expected_test_case = {
                'file_path': 'fixtures/test_file.py',
                'class_name': 'TestInvestmentsService',
                'class_code_line': 46,
                'case_name': 'Invest money into stocks',
                'function_name': 'test_invest_money_into_stocks',
                'function_code_line': 48,
                'intentions': [
                    {
                        'type': 'case',
                        'code_line': 49,
                        'description': 'Invest money into stocks',
                    },
                    {
                        'type': 'expect',
                        'code_line': 52,
                        'description': 'Stock is purchased',
                    },
                ]
            }

            assert expected_test_case in intentions_json['investments']['investments']['service']

        with expect('Invest money into crypto test case is in investments service test cases'):
            expected_test_case = {
                'file_path': 'fixtures/test_file.py',
                'class_name': 'TestInvestmentsService',
                'class_code_line': 46,
                'case_name': 'Invest money into crypto',
                'function_name': 'test_invest_money_into_crypto',
                'function_code_line': 55,
                'intentions': [
                    {
                        'type': 'case',
                        'code_line': 56,
                        'description': 'Invest money into crypto',
                    },
                    {
                        'type': 'expect',
                        'code_line': 59,
                        'description': 'Crypto is purchased',
                    },
                ]
            }

            assert expected_test_case in intentions_json['investments']['investments']['service']

        with expect('Invest money into non-existing stocks test case is in investments service test cases'):
            expected_test_case = {
                'file_path': 'fixtures/test_file.py',
                'class_name': None,
                'class_code_line': None,
                'case_name': 'Invest into non existing stocks',
                'function_name': 'test_invest_into_non_existing_stocks',
                'function_code_line': 64,
                'intentions': [
                    {
                        'type': 'when',
                        'code_line': 65,
                        'description': 'Stock to buy does not exist',
                    },
                    {
                        'type': 'case',
                        'code_line': 68,
                        'description': 'Invest money into stocks',
                    },
                    {
                        'type': 'expect',
                        'code_line': 71,
                        'description': 'Stock does not exist error is raised',
                    },
                ]
            }

            assert expected_test_case in intentions_json['investments']['investments']['service']

    def test_create_intentions_json_ignore_test_cases_without_intentions(self, remove_intentions_json) -> None:
        with when('Tests folder with described test cases without intentions'):
            path_to_tests_folder = './fixtures'

        with case('Create intentions JSON file'):
            create_intentions_json(directory=path_to_tests_folder)

        with open('./.intentions/intentions.json', 'r') as intentions_json:
            intentions_json = json.load(intentions_json)

        with expect('Described test case without intentions is not present in test cases'):
            expected_test_case = {
                'file_path': 'fixtures/test_file.py',
                'class_name': None,
                'class_code_line': None,
                'function_name': 'test_sum',
                'function_code_line': 87,
                'intentions': [],
            }

            assert expected_test_case not in intentions_json['investments']['investments']['service']
