Next-gen `Arrange-Act-Assert` to structure test cases and force software engineers to express explicit intentions in 
`BDD` style.

[![](https://github.com/dmytrostriletskyi/intentions/actions/workflows/main.yaml/badge.svg?branch=main)](https://github.com/dmytrostriletskyi/intentions/actions/workflows/main.yaml)
[![](https://img.shields.io/github/release/dmytrostriletskyi/intentions.svg)](https://github.com/dmytrostriletskyi/intentions/releases)
[![](https://img.shields.io/pypi/v/intentions.svg)](https://pypi.python.org/pypi/intentions)

[![](https://pepy.tech/badge/intentions)](https://pepy.tech/project/intentions)
[![](https://img.shields.io/pypi/l/intentions.svg)](https://pypi.python.org/pypi/intentions/)
[![](https://img.shields.io/pypi/pyversions/intentions.svg)](https://pypi.python.org/pypi/intentions/)

![](./assets/test-example.png)

Table of content:

* [Introduction](#introduction)
* [Motivation](#motivation)
  * [Clarity and readability](#clarity-and-readability)
  * [Mental Load](#mental-load)
  * [Maintenance](#maintenance)
  * [BDD encouragement](#bdd-encouragement)
  * [Collaboration](#collaboration)
* [Getting Started](#getting-started)
  * [How to Install](#how-to-install)
  * [Usage](#Usage)
    * [When](#when)
    * [Case](#case)
    * [Expect](#expect)

## Introduction

`intentions` is a `Python` next-gen `Arrange-Act-Assert` library created to help structuring test cases and force 
software engineers to express explicit intentions in `BDD` style.

`Arrange-Act-Assert` is a pattern used to structure test cases. It provides a clear way to organize test code, making 
it easier to read and understand:

* `Arrange` block sets up the necessary objects, data, or state before the action to be tested.
* `Act` block performs the actual operation or method call that should be tested.
* `Assert` block checks the results of the action comparing the actual outcome with the expected outcome.

`Behavior-Driven Development` is an approach in testing that emphasizes the behavior of an application for business 
needs. It focuses on defining test cases in plain, simple language with use cases and user stories. It typically uses 
the `Given-When-Then` format to specify the system's expected behavior in various situations:

* `Given` a context.
* `When` an action happens.
* `Then` an expected outcome.

`intentions` aims to combine those two approaches to empower software engineers for more effective testing with `when`, 
`case`, and `expect` context managers using which they can build behavior-driven arrange-act-assert based test cases.

In the same time you are not required to use it everywhere, even in the single test you are able to define which
constructs to use and how many of them. For instance, you can skip it for unit tests and only use for integration tests.

```python
class TestAccountService:

    def test_transfer_money_with_insufficient_balance(self):
        mock_send_in_app_notification = mock('notifications.send')

        receiver_account = AccountFactory()

        with when('Sender account has insufficient balance'):
            sender_account = AccountFactory(balance=0)

        with when('Pushing in-app notifications feature flag is enabled for sender account'):
            enable_in_app_notifications(account=sender_account)

        with case('Transfer money from one account to another'):
            AccountService.transfer_money(from=sender_account, to=receiver_account, amount=100)

        with expect('No transfers have been made'):
            assert not sender_account.transfers
            assert not receiver_account.transfers

        with expect('Increase credit limit proposal is created'):
            assert Proposal.get_last(account=sender_account, type=ProposalType.INCREASE_CREDIT_LIMIT)
            
        with expect('Sender account receives insufficient balance in-app notification'):
            mock_send_in_app_notification.assert_called_with(
                account_id=sender_account.id,
                type=InAppNotificationType.INSUFFICIENT_BALANCE,
                expired_at=None,
            )
```

## Motivation

### Clarity and readability

`when`, `case` and `expect` clearly convey the purpose of each block. With them, it is easy to tell a story of what is 
being tested, making it easier for someone reading the test to understand the intention behind each part. Instead of 
limited `# Arrange`, `# Act` and `# Assert` comments in your test case, you can use as much intentions as possible 
emphasizing on every important detail of the test case.

### Mental Load

With `when`, `case` and `expect`, test cases are broken down clearly, reducing mental load.

### Maintenance

If the test fails, the `when`, `case` and `expect` make it easier to understand why the test was written in the first 
place due to its descriptive nature. As the test case evolves, it's easier to maintain because the purpose of each step 
is clear.

### BDD Encouragement

It aligns with `Behavior-Driven Development` principles, as it focuses on describing the behavior of the system under a
test case, making the tests more focused on outcomes and behavior rather than implementation details.

### Collaboration

With `when`, `case` and `expect`, you introduce a common language for communication between developers, testers, and 
business stakeholders and make collaboration easier. It also helps to minimize the learning curve for new joiners.

## Getting Started

### How to install

Install the library with the following command using `pip3`:

```bash
$ pip3 install intentions
```

### Usage

#### When

It emphasizes on setting up the necessary objects, data, or state to make the context of a test cace meaningful. 
Important to use this construct to focus exactly specific condition of the test case.

As you see on the example below, the context manager is used only on specifically a `user from the UK` that has 
`uploaded a document` for a verification:

```python
from intentions import when


class TestDocumentVerificationService:
  
  def test_verify_document_when_uploaded_and_user_from_uk(self):
      admin = UserFactory(is_admin=True)
      verification = VerificationFactory()
      
      ...
    
      with when('User is from the United Kingdom'):
          user = UserFactory(country=Country.UK)

      with when('User document is uploaded'):
          user_document = Document(
              user=user,
              verification=verification,
              status=DocumentStatus.UPLOADED,
          )

      ...
```

#### Case

It emphasizes on performing the actual operation or method call that should be tested. Important to use this context 
manager over exact execution.

As you see on the example below, the context manager is used only for the document verification method named 
`verify_document`. Besides having many other functions such as mocks, data preparation and side functions in the test 
alongside the method:

```python
from intentions import case


class TestDocumentVerificationService:
  
  def test_verify_document_when_uploaded_and_user_from_uk(self):
      ...
      
      mock_verification_api_response = prepare_verification_api_response()
      mock_document_verification_api_request = mock(
          path='api.document_verification.request',
          data=mock_verification_api_response,
      )
      
      enable_async_requests()
      create_user_kyc_profile()

      with case('Verify a document'):
          document_verification = DocumentVerificationService.verify_document(
              document=document, 
              user=user, 
              admin=admin,
          )

      ...
```

#### Expect

It emphasizes on checking the results of the action comparing the actual outcome with the expected outcome, expected 
behavior or change in the system. Important to use this context manager to emphasize different groups of expectations 
and exact outcome or behavior.

As you see on the example below, the context manager is used to distinguish 3 different outcomes: `the user's document
was reviewed by external API`, was `additionally reviewed by admin` as user is from the UK and the 
`document verification happened without errors`:

```python
from intentions import expect


class TestDocumentVerificationService:
  
  def test_verify_document_when_uploaded_and_user_from_uk(self):
      ...
      
      with expect('Document was verified by external API'):
          mock_document_verification_api_request.assert_called()
          assert document.is_verified_by_provider
  
      with expect('Document was additionally verified by admin as user is from the UK'):
          assert document.admin == admin
          assert document.is_verified_by_admin

      with expect('Document verification happened without errors'):
          assert not document_verification.errors
```
