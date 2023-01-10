# TypeLiteral

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
TypeLiteral

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_literal](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py) module.

## TypeLiteral

[Show source in type_literal.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L14)

Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`.

#### Arguments

- `name` - Literal name for non-inline.
- `children` - Literal values.
- `inline` - Render literal inline.

#### Signature

```python
class TypeLiteral(FakeAnnotation):
    def __init__(self, name: str, children: Iterable[str]) -> None:
        ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeLiteral().add_child

[Show source in type_literal.py:110](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L110)

Disabled method to avoid confusion.

#### Signature

```python
def add_child(self, child: FakeAnnotation) -> None:
    ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeLiteral().copy

[Show source in type_literal.py:98](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L98)

Create a copy of type annotation wrapper.

#### Signature

```python
def copy(self) -> "TypeLiteral":
    ...
```

### TypeLiteral().get_import_record

[Show source in type_literal.py:89](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L89)

Get import record required for using type annotation.

#### Signature

```python
def get_import_record(self) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeLiteral().get_local_types

[Show source in type_literal.py:122](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L122)

Get internal types generated by builder.

#### Signature

```python
def get_local_types(self) -> list[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeLiteral().get_sort_key

[Show source in type_literal.py:30](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L30)

Sort literals by name.

#### Signature

```python
def get_sort_key(self) -> str:
    ...
```

### TypeLiteral.get_typing_import_record

[Show source in type_literal.py:75](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L75)

Get import record required for using Literal.

Fallback to typing_extensions for py38-.

#### Signature

```python
@staticmethod
def get_typing_import_record() -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeLiteral().inline

[Show source in type_literal.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L36)

Whether Litereal should be rendered inline.

1-value literals are rendered inline.

#### Signature

```python
@property
def inline(self) -> bool:
    ...
```

### TypeLiteral().is_literal

[Show source in type_literal.py:104](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L104)

Whether type annotation is `Literal`.

#### Signature

```python
def is_literal(self) -> bool:
    ...
```

### TypeLiteral().is_same

[Show source in type_literal.py:116](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L116)

Check if literals have the same children.

#### Signature

```python
def is_same(self, other: "TypeLiteral") -> bool:
    ...
```

### TypeLiteral().render

[Show source in type_literal.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L56)

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

#### Signature

```python
def render(self, parent_name: str = "") -> str:
    ...
```

### TypeLiteral().render_children

[Show source in type_literal.py:69](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_literal.py#L69)

Render literal children to representation.

#### Signature

```python
def render_children(self) -> str:
    ...
```


