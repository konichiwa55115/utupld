import os


class Config:

    BOT_TOKEN = "6226680808:AAHvBz5Nkt7gQ6-TFL7YphMxlrAQ-VhWKHc"

    SESSION_NAME = "anything"

    API_ID = "17983098"

    API_HASH = "ee28199396e0925f1f44d945ac174f64"

    CLIENT_ID = "664256487809-21lnbeqr7cau7fng78oeli1bnqcjthvp.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = "6234365091"

    AUTH_USERS_TEXT = "6234365091"

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = "private"

    CRED_FILE = "auth_token.txt"
