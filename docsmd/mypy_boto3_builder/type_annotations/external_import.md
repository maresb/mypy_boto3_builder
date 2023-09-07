# ExternalImport

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
ExternalImport

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.external_import](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py) module.

## ExternalImport

[Show source in external_import.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L14)

Wrapper for type annotations imported from 3rd party libraries, like `boto3.service.Service`.

#### Arguments

- `source` - Module import string.
- `name` - Import name.
- `alias` - Import local name.
- `safe` - Whether import is wrapped in try-except.

#### Signature

```python
class ExternalImport(FakeAnnotation):
    def __init__(
        self, source: ImportString, name: str = "", alias: str = "", safe: bool = False
    ) -> None:
        ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
- [ImportString](../import_helpers/import_string.md#importstring)

### ExternalImport().copy

[Show source in external_import.py:92](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L92)

Create a copy of type annotation wrapper.

#### Signature

```python
def copy(self: _R) -> _R:
    ...
```

### ExternalImport().copy_from

[Show source in external_import.py:98](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L98)

Copy all fileds from another instance.

#### Signature

```python
def copy_from(self: _R, other: _R) -> None:
    ...
```

### ExternalImport.from_class

[Show source in external_import.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L37)

Create an instance from an imported class.

#### Arguments

- `value` - Any Class.
- `alias` - Local name.
- `safe` - Whether import is wrapped in try-except.

#### Signature

```python
@classmethod
def from_class(cls: type[_R], obj: type, alias: str = "", safe: bool = False) -> _R:
    ...
```

### ExternalImport().import_record

[Show source in external_import.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L59)

Get import record required for using type annotation.

#### Signature

```python
@property
def import_record(self) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ExternalImport().render

[Show source in external_import.py:77](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L77)

Get string with local name to use.

#### Returns

Import record local name.

#### Signature

```python
def render(self, parent_name: str = "") -> str:
    ...
```