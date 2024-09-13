from __future__ import annotations

import ast
from typing import Optional

from intentions.render.dto import Describe


class AstNodeVisitor(ast.NodeVisitor):
    """
    AST node visitor implementation.
    """

    def __init__(self) -> None:
        """
        Construct the object.
        """
        self.parent_map = {}
        self.nodes = []

    def visit(self, node: ast.AST) -> None:
        """
        Visit the node.

        It travers the tree in the preorder way and collect parents. Preorder traversal is needed to collect test
        functions in the top to down manner with even class's test function be respected. Collecting parents is needed
        to have access to class names and description for further rendering.

        Arguments:
            node (ast.AST): a node to visit, typically the root node.
        """
        self.nodes.append(node)

        for child in ast.iter_child_nodes(node):
            if child not in self.parent_map:
                self.parent_map[child] = node

        self.generic_visit(node)

    def get_parent(self, node: ast.AST) -> Optional[ast.AST]:
        return self.parent_map.get(node, None)

    def get_nodes(self) -> list[ast.AST]:
        return self.nodes

    def get_describe(self, decorators: [ast.Call]) -> Optional[Describe]:
        """
        Get describe context manager description.

        Arguments:
            decorators (list): list of decorators over a function or class that potentially relate to test cases.

        Returns:
            An object and domain as `Describe`.
        """
        for decorator in decorators:
            if not isinstance(decorator, ast.Call):
                continue

            if not isinstance(decorator.func, ast.Name):
                continue

            if decorator.func.id != 'describe':
                continue

            assert decorator.keywords[0].arg == 'domain'  # noqa: S101
            assert decorator.keywords[1].arg == 'component'  # noqa: S101
            assert decorator.keywords[2].arg == 'layer'  # noqa: S101

            return Describe(
                domain=decorator.keywords[0].value.value,
                component=decorator.keywords[1].value.value,
                layer=decorator.keywords[2].value.value,
            )

        return None
