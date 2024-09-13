import ast
import json
from dataclasses import asdict
from pathlib import Path

from intentions.render.ast_ import AstNodeVisitor
from intentions.render.dto import (
    TestCase,
    TestCaseIntention,
)
from intentions.render.encoders import JsonEncoderWithEnumSupport
from intentions.render.enums import Intention
from intentions.utils import is_test_function


def collect_test_files(directory: str) -> list[Path]:
    test_files = []

    for path in Path(directory).rglob('test_*.py'):
        test_files.append(path)

    return test_files


def collect_test_cases(storage: dict, file: Path) -> None:
    file_text = file.read_text()
    file_as_ast = ast.parse(file_text)

    ast_node_visitor = AstNodeVisitor()
    ast_node_visitor.visit(file_as_ast)

    nodes = ast_node_visitor.get_nodes()

    for node in nodes:
        if not isinstance(node, ast.FunctionDef):
            continue

        function_node = node

        if not is_test_function(name=function_node.name):
            continue

        test_case_intentions = []

        for node in function_node.body:
            if not isinstance(node, ast.With):
                continue

            with_node = node

            for with_node_item in with_node.items:
                if not isinstance(with_node_item.context_expr.func, ast.Name):
                    continue

                with_node_item_name = with_node_item.context_expr.func.id

                if with_node_item_name not in ('when', 'case', 'expect'):
                    continue

                with_node_item_code_line = with_node_item.context_expr.args[0].lineno
                with_node_item_description = with_node_item.context_expr.args[0].value

                test_sase_intention = TestCaseIntention(
                    type=Intention(with_node_item_name),
                    code_line=with_node_item_code_line,
                    description=with_node_item_description,
                )

                test_case_intentions.append(test_sase_intention)

        if not test_case_intentions:
            continue

        class_name = None
        class_code_line = None

        parent_node = ast_node_visitor.get_parent(function_node)

        if isinstance(parent_node, ast.ClassDef):
            class_name = parent_node.name
            class_code_line = parent_node.lineno

        if isinstance(parent_node, ast.ClassDef):
            describe = ast_node_visitor.get_describe(decorators=parent_node.decorator_list)

        else:
            describe = ast_node_visitor.get_describe(decorators=function_node.decorator_list)

        if describe is None:
            continue

        if describe.domain not in storage:
            storage[describe.domain] = {}

        if describe.component not in storage[describe.domain]:
            storage[describe.domain][describe.component] = {}

        if describe.layer not in storage[describe.domain][describe.component]:
            storage[describe.domain][describe.component][describe.layer] = []

        test_function = TestCase(
            function_name=function_node.name,
            function_code_line=function_node.lineno,
            intentions=test_case_intentions,
            class_name=class_name,
            class_code_line=class_code_line,
            file_path=file.as_posix(),
        )

        test_case_as_dict = asdict(test_function)
        storage[describe.domain][describe.component][describe.layer].append(test_case_as_dict)


def create_intentions_json(directory: str) -> None:
    test_files = collect_test_files(directory=directory)

    storage = {}

    for test_file in test_files:
        collect_test_cases(storage=storage, file=test_file)

    intentions_folder_path = Path('./.intentions')

    if not intentions_folder_path.exists():
        intentions_folder_path.mkdir(parents=True)

    with open('./.intentions/intentions.json', 'w') as file:
        json.dump(storage, file, indent=4, cls=JsonEncoderWithEnumSupport)
