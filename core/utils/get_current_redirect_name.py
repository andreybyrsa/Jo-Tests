def get_current_redirect_name(user):
    if user.role == "student":
        return "courses"

    return "tests"
