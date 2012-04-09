class Settings:
    """
    This class contains settings for the unit tests
    """
    #: This must contain the URL to your Piwik install's /piwik.php
    PIWIK_TRACKING_API_URL = '<Your Piwik tracker API URL>'

    #: This must contain the URL to your Piwik install's root
    PIWIK_ANALYTICS_API_URL = '<Your Piwik API URL>'

    #: The ID of the site you want to send the test tracking requests to
    PIWIK_SITE_ID = 1

    #: The auth token of an admin user for above site
    PIWIK_TOKEN_AUTH = '<Your Piwik auth token>'