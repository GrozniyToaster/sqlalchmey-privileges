# Privileges manipulation with SQLalchemy

Add `grant/revoke privileges` construct

## Usage

Examples:
```python
>>> from sqlalchemy import *
>>> from sqlalchemy_privileges import *

>>> str(GrantPrivileges('insert', Table('a', MetaData(schema='schema')), 'my.name'))
'GRANT INSERT ON schema.a TO "my.name"\n'

>>> str(RevokePrivileges(['insert', 'update'], table('a'), ['my.name', 'my.friend']))
'REVOKE INSERT, UPDATE ON a TO "my.name", "my.friend"\n'

>>> str(GrantPrivileges('all', table('a'), ['my.name', 'my.friend']))
'GRANT ALL ON a TO "my.name", "my.friend"\n'
```

## Installation

`sqlalchemy-privileges` is available on PyPI and can be installed via `pip`

```console
pip install sqlalchemy-privileges
```

## Acknowledgements
Package inspired by [sqlalchemy-views](https://pypi.org/project/sqlalchemy-views/) 

And thank you to the various [contributors](https://github.com/GrozniyToaster/sqlalchmey-privileges/pulse)!