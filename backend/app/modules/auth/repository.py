from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.auth.model import User


class AuthRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> User | None:
        """
        Retrieve a user using email.
        """
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_user_by_phone(self, phone: str) -> User | None:
        """
        Retrieve a user using phone number.
        """
        return (
            self.db.query(User)
            .filter(User.phone == phone)
            .first()
        )

    def get_user_by_id(self, user_id: UUID) -> User | None:
        """
        Retrieve a user using UUID.
        """
        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def create_user(self, user: User) -> User:
        """
        Save a new user.
        """
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user: User) -> User:
        """
        Update an existing user.
        """
        self.db.commit()
        self.db.refresh(user)
        return user