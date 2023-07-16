# ImportRecord

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Import Helpers](./index.md#import-helpers) /
ImportRecord

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_record](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py) module.

## ImportRecord

[Show source in import_record.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L15)

Helper for Python import strings.

#### Arguments

- `source` - Source of import.
- `name` - Import name.
- `alias` - Import local name.
- `min_version` - Minimum Python version, used for fallback.
- `fallback` - Fallback ImportRecord.

#### Signature

```python
class ImportRecord:
    def __init__(
        self: _R,
        source: ImportString,
        name: str = "",
        alias: str = "",
        min_version: tuple[int, ...] | None = (3, 8),
        fallback: _R | None = None,
    ) -> None:
        ...
```

#### See also

- [ImportString](./import_string.md#importstring)

### ImportRecord.empty

[Show source in import_record.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L50)

Whether import record is an empty string.

#### Signature

```python
@classmethod
def empty(cls: type[_R]) -> _R:
    ...
```

### ImportRecord().get_external

[Show source in import_record.py:153](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L153)

Get itself.

Overriden by `InternalImportRecord`.

#### Signature

```python
def get_external(self: _R, module_name: str) -> _R:
    ...
```

### ImportRecord().get_local_name

[Show source in import_record.py:108](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L108)

Get local import name.

#### Signature

```python
def get_local_name(self) -> str:
    ...
```

### ImportRecord().is_builtins

[Show source in import_record.py:114](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L114)

Whether import is from Python `builtins` module.

#### Signature

```python
def is_builtins(self) -> bool:
    ...
```

### ImportRecord().is_local

[Show source in import_record.py:135](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L135)

Whether import is from local module.

#### Signature

```python
def is_local(self) -> bool:
    ...
```

### ImportRecord().is_standalone

[Show source in import_record.py:161](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L161)

Whether import record should not be grouped.

#### Signature

```python
def is_standalone(self) -> bool:
    ...
```

### ImportRecord().is_third_party

[Show source in import_record.py:126](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L126)

Whether import is from 3rd party module.

#### Signature

```python
def is_third_party(self) -> bool:
    ...
```

### ImportRecord().is_type_defs

[Show source in import_record.py:120](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L120)

Whether import is from `type_defs` module.

#### Signature

```python
def is_type_defs(self) -> bool:
    ...
```

### ImportRecord().needs_sys_fallback

[Show source in import_record.py:170](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L170)

Whether ImportString requires `sys` module.

#### Signature

```python
def needs_sys_fallback(self) -> bool:
    ...
```

### ImportRecord().render

[Show source in import_record.py:57](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L57)

Get rendered string.

#### Signature

```python
def render(self) -> str:
    ...
```