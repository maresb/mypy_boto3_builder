from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict, TypedDictAttribute
from mypy_boto3_builder.type_annotations.type_union import TypeUnion
from mypy_boto3_builder.utils.type_checks import (
    get_optional,
    is_type_def,
    is_typed_dict,
    is_union,
    is_literal,
    is_type_parent,
)


class TestTypeChecks:
    def test_get_optional(self):
        assert get_optional(Type.DictStrAny).render() == "Optional[Dict[str, Any]]"
        assert get_optional(TypeUnion([Type.str, Type.bool])).render() == "Union[str, bool, None]"

    def test_is_type_def(self):
        assert not is_type_def(Type.DictStrAny)
        assert not is_type_def(Type.ListAny)
        assert not is_type_def(TypeUnion([Type.str, Type.bool]))
        assert is_type_def(TypeUnion([Type.str, Type.bool], name="MyUnion"))
        assert is_type_def(
            TypeTypedDict("MyTypedDict", [TypedDictAttribute("key", Type.str, True)])
        )

    def test_is_typed_dict(self):
        assert not is_typed_dict(Type.DictStrAny)
        assert not is_typed_dict(Type.ListAny)
        assert not is_typed_dict(TypeUnion([Type.str, Type.bool]))
        assert is_typed_dict(
            TypeTypedDict("MyTypedDict", [TypedDictAttribute("key", Type.str, True)])
        )

    def test_is_union(self):
        assert not is_union(Type.DictStrAny)
        assert not is_union(Type.ListAny)
        assert is_union(TypeUnion([Type.str, Type.bool]))
        assert is_union(TypeUnion([Type.str, Type.bool], name="MyUnion"))

    def test_is_literal(self):
        assert not is_literal(Type.DictStrAny)
        assert not is_literal(Type.ListAny)
        assert is_literal(TypeLiteral("MyLiteral", ["value"]))

    def test_is_type_parent(self):
        assert not is_type_parent(Type.str)
        assert is_type_parent(Type.DictStrAny)
        assert is_type_parent(Type.ListAny)
        assert is_type_parent(TypeUnion([Type.str, Type.bool]))
        assert is_type_parent(TypeUnion([Type.str, Type.bool], name="MyUnion"))
        assert is_type_parent(
            TypeTypedDict("MyTypedDict", [TypedDictAttribute("key", Type.str, True)])
        )