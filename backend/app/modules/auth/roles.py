from typing import Callable

from fastapi import Depends, HTTPException, status

from app.modules.auth.dependencies import get_current_user
from app.modules.auth.model import User
from app.shared.enums import UserRole


def require_role(*allowed_roles: UserRole) -> Callable:
    """
    Allow access only to users with one of the specified roles.
    """

    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:

        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource.",
            )

        return current_user

    return role_checker