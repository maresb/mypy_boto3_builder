# {{ package.client.name }} for boto3 {{ package.service_name.class_name }} module

> [Index](../README.md) > [{{ package.service_name.class_name }}](./README.md) > {{ package.client.name }}

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.boto3_doc_link }})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

## {{ package.client.name }}

Type annotations for `boto3.client("{{ package.service_name.boto3_name }}")`

Can be used directly:

```python
from {{ package.service_name.module_name }}.client import {{ package.client.name }}

def get_{{ package.service_name.boto3_name }}_client() -> {{ package.client.name }}:
    return boto3.client("{{ package.service_name.boto3_name }}")
```

[Open boto3 documentation]({{ package.client.boto3_doc_link }})

## Exceptions

{% if package.client.exceptions_class.attributes %}
`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from {{ package.service_name.module_name }}.client import {{ package.client.exceptions_class.name }}

def handle_error(exc: {{ package.client.exceptions_class.name }}.{{ package.client.exceptions_class.attributes[0].name }}) -> None:
    ...
```
{% else %}
{{ package.client.name }} has no exceptions.
{% endif %}

Exceptions:

{% for attribute in package.client.exceptions_class.attributes -%}
- `{{ package.client.exceptions_class.name }}.{{ attribute.name }}`{{ '\n' -}}
{% endfor %}

## Methods

{% for method in package.client.own_methods %}
### {{ method.name }}

Type annotations for `boto3.client("{{ package.service_name.boto3_name }}").{{ method.name }}` method.

[Open boto3 documentation]({{ package.service_name.get_boto3_doc_link("Client", method.name) }}]

```python
{% with render_docstrings=False -%}
{% include "common/method.py.jinja2" with context -%}{{ '\n' -}}
{% endwith -%}
```
{% else %}
{{ package.client.name }} has no public methods.
{% endfor %}

{% if package.paginators %}
### get_paginator

Type annotations for `boto3.client("{{ package.service_name.boto3_name }}").get_paginator` method with overloads.

{% for paginator in package.paginators -%}
- `client.get_paginator("{{ paginator.operation_name }}")` -> [{{ paginator.name }}](./paginators.md#{{ get_anchor_link(paginator.name) }}){{ '\n' -}}
{% endfor %}
{% endif %}

{% if package.waiters %}
### get_waiter

Type annotations for `boto3.client("{{ package.service_name.boto3_name }}").get_waiter` method with overloads.

{% for waiter in package.waiters -%}
- `client.get_waiter("{{ waiter.waiter_name }}")` -> [{{ waiter.name }}](./waiters.md#{{ get_anchor_link(waiter.name) }}){{ '\n' -}}
{% endfor %}
{% endif %}