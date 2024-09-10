from intentions import (
    case,
    describe,
    expect,
    when,
)


@describe(object='Accounts Service', domain='accounts')
class TestAccountsService:

    def test_transfer_money_with_insufficient_balance(self):
        with when('Sender account has insufficient balance'):
            pass

        with case('Transfer money from one sender to receiver'):
            pass

        with expect('No transfers have been made'):
            pass

    def test_transfer_money_with_sufficient_balance(self):
        with when('Sender account has sufficient balance'):
            pass

        with case('Transfer money from one sender to receiver'):
            pass

        with expect('Sender account balance decreased on the transfer money amount'):
            pass


@describe(object='Accounts Service', domain='accounts')
def test_transfer_money_to_non_existing_receiver_account():
    with when('Receiver account does not exist'):
        pass

    with case('Transfer money from one sender to receiver'):
        pass

    with expect('Receiver account does not exist error is raised'):
        pass


@describe(object='Investments Service', domain='investments')
class TestInvestmentsService:

    def test_invest_money_into_stocks(self):
        with case('Invest money into stocks'):
            pass

        with expect('Stock is purchased'):
            pass

    def test_invest_money_into_crypto(self):
        with case('Invest money into crypto'):
            pass

        with expect('Crypto is purchased'):
            pass


@describe(object='Investments Service', domain='investments')
def test_invest_into_non_existing_stocks():
    with when('Stock to buy does not exist'):
        pass

    with case('Invest money into stocks'):
        pass

    with expect('Stock does not exist error is raised'):
        pass


def test_invest_into_non_existing_crypto():
    with when('Crypto to buy does not exist'):
        pass

    with case('Invest money into crypto'):
        pass

    with expect('Crypto does not exist error is raised'):
        pass


@describe(object='Investments Service', domain='investments')
def test_sum():
    assert 4 == 2 + 2
