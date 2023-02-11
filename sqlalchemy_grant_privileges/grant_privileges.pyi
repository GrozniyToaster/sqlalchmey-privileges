from typing import List, Union
from typing_extensions import Literal

from sqlalchemy.sql import TableClause 
from sqlalchemy.sql import ClauseElement, Executable


Privilege = Literal[
    'SELECT',
    'INSERT',
    'UPDATE',
    'DELETE',
    'TRUNCATE',
    'REFERENCES',
    'TRIGGER',
    'select',
    'insert',
    'update',
    'delete',
    'truncate',
    'references',
]

AllPrivileges = Literal['ALL', 'all', 'ALL PRIVILEGES', 'all privileges']


class GrantRevokePrivilegesBase(Executable, ClauseElement):
    inherit_cache: bool = ...

    def __init__(
            self,
            privileges: Union[Privilege, List[Privilege], AllPrivileges],
            table: TableClause,
            roles: Union[str, List[str]],
            *,
            command: Literal['GRANT', 'REVOKE']
    ) -> None:
        ...

class GrantPrivileges(GrantRevokePrivilegesBase):
    inherit_cache: bool = ...

    def __init__(
        self,
        privileges: Union[Privilege, List[Privilege], AllPrivileges],
        table: TableClause,
        roles: Union[str, List[str]],
    ) -> None:
        super(GrantPrivileges, self).__init__(
            command='GRANT',
            privileges=privileges,
            table=table,
            roles=roles,
        )


class RevokePrivileges(GrantRevokePrivilegesBase):
    inherit_cache: bool = ...

    def __init__(
        self,
        privileges: Union[Privilege, List[Privilege], AllPrivileges],
        table: TableClause,
        roles: Union[str, List[str]],
    ):
        super(RevokePrivileges, self).__init__(
            command='REVOKE',
            privileges=privileges,
            table=table,
            roles=roles,
        )