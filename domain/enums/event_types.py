from enum import Enum


class EventTypes(Enum):
    UserLoggedIn = "user_logged_in"
    UserLoggedOut = "user_logged_out"
    UserCreated = "user_created"
    UserDeleted = "user_deleted"
    UserPasswordChanged = "user_password_changed"
    UserPasswordReset = "user_password_reset"
    UserRoleChanged = "user_role_changed"


map_event = {
    "UserLoggedIn": EventTypes.UserLoggedIn,
    "UserLoggedOut": EventTypes.UserLoggedOut,
    "UserCreated": EventTypes.UserCreated,
    "UserDeleted": EventTypes.UserDeleted,
    "UserPasswordChanged": EventTypes.UserPasswordChanged,
    "UserPasswordReset": EventTypes.UserPasswordReset,
    "UserRoleChanged": EventTypes.UserRoleChanged
}
