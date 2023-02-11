from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import ClauseElement, Executable


VALID_PRIVILEGES = {
    'select',
    'insert',
    'update',
    'delete',
    'truncate',
    'references',
    'all',
    'all privileges',
}


class GrantRevokePrivilegesBase(Executable, ClauseElement):
    inherit_cache = True

    def __init__(
        self,
        privileges,
        table,
        roles,
        *,
        command,
    ):
        self.table = table
        self.command = command

        self.roles = [roles] if isinstance(roles, str) else roles
        self.privileges = [privileges] if isinstance(privileges, str) else privileges
        
        self._validate_privileges(self.privileges)

    @classmethod
    def _validate_privileges(cls, privileges):
        not_allowed_privileges = [
            privilege 
            for privilege in privileges 
            if privilege.lower() not in VALID_PRIVILEGES
        ]
        if not_allowed_privileges:
            raise ValueError(
                'Got %s as privileges, possible privileges=%s' % 
                (not_allowed_privileges, VALID_PRIVILEGES)
            )

@compiles(GrantRevokePrivilegesBase)
def visit_grant_privileges(element: GrantRevokePrivilegesBase, compiler, **kw):
    privileges = ', '.join(privilege.upper() for privilege in element.privileges)
    roles = ', '.join(compiler.preparer.quote_identifier(role) for role in element.roles)
    table_name = compiler.process(element.table, asfrom=True, **kw)

    return '%s %s ON %s TO %s\n' % (
        element.command,
        privileges,
        table_name,
        roles
    )


class GrantPrivileges(GrantRevokePrivilegesBase):
    inherit_cache = True

    def __init__(
        self,
        privileges,
        table,
        roles,
    ):
        super(GrantPrivileges, self).__init__(
            command='GRANT',
            privileges=privileges,
            table=table,
            roles=roles,
        )

class RevokePrivileges(GrantRevokePrivilegesBase):
    inherit_cache = True

    def __init__(
        self,
        privileges,
        table,
        roles,
    ):
        super(RevokePrivileges, self).__init__(
            command='REVOKE',
            privileges=privileges,
            table=table,
            roles=roles,
        )
