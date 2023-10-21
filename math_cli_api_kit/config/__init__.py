"""This module defines the configuration settings for the
Math CLI API Kit.

These settings are used to customize the behavior and information of
the API and command-line tool.

For more information on how to configure and use these settings, please
refer to the project's documentation or the official GitHub repository:
https://github.com/gasparyanvazgen/math-cli-api-kit
"""

GITHUB_REPO_URL = "https://github.com/gasparyanvazgen/math-cli-api-kit"


class APIConfig:
    API_BASEPATH = "/api"
    API_SCHEMES = ["https"]
    API_VERSION = "0.1.0-beta"
    API_TITLE = "Math CLI API Kit: Algebra and Geometry Operations"
    API_DESCRIPTION = "Perform algebraic and geometric operations using this" \
                      " kit's command-line tool and API, with a set of" \
                      " math functions. Integrate with other" \
                      " applications through a RESTful API."
    API_CONTACT_NAME = "Vazgen Gasparyan"
    API_CONTACT_URL = "https://linkedin.com/in/vazgen-gasparyan/"
    API_CONTACT_EMAIL = "gvazgen@outlook.com"
    API_LICENSE_NAME = "MIT"
    API_LICENSE_URL = f"{GITHUB_REPO_URL}/blob/master/LICENSE"
