import os
from health import health_check


def test_health():
    os.environ['HC_CHECK_HOST'] = 'https://api.icon.community'
    health_check()
