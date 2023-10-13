"""
Hold data relevant for the api request
"""
TEST_EMAIL = 'HASFSAF@gmail.com'
TEST_PASSWORD = 'Bababa123@'

HEADERS = {
    'content-type': 'application/json',
    "authority": "gizmo.rakuten.tv",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*"
}

DATA = {
    "user": {
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD,
        "password_confirmation": TEST_PASSWORD,
        "username": TEST_EMAIL
    },
    "marketing_opt_in": False,
    "terms_conditions_ids": "3921,3923,3929",
    "device_identifier": "web",
    "device_metadata": {
        "app_version": "v5.3.6",
        "audio_quality": "2.0",
        "brand": "chrome",
        "firmware": "XX.XX.XX",
        "hdr": False,
        "model": "GENERIC",
        "os": "Mac OS",
        "sdk": "116.0.0",
        "serial_number": "not implemented",
        "trusted_uid": False,
        "uid": "4f90da2c-9cd6-4b17-a48d-411d4cc41fa6",
        "video_quality": "FHD",
        "year": 1970
    },
    "ifa_id": "182110ba-59e8-491d-b7d4-30191832aa21"
}
