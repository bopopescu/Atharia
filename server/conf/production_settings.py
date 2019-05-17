"""
Settings we use for production. Some of these could eventually be moved into a settings.ini file
"""
from .base_settings import *

from decouple import config, Csv

TELNET_INTERFACES = config('TELNET_INTERFACES', default='45.33.87.194', cast=Csv())
WEBSOCKET_CLIENT_INTERFACE = config('WEBSOCKET_CLIENT_INTERFACE', default='45.33.87.194')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='.vertinext.com, .vertinext.com', cast=Csv())
WEBSERVER_PORTS = [(8000, 5001)]
WEBSOCKET_CLIENT_PORT = 8001
WEBSOCKET_CLIENT_URL = "wss://atharia.vetinext.com/ws"
SSH_PORTS = [8022]
SSL_PORTS = [4001]
AMP_PORT = 5000
SITE_HEADER = "ArxPrime Admin"
INDEX_TITLE = "ArxPrime Admin"
IDMAPPER_CACHE_MAXSIZE = 4000
CHECK_VPN = True
MAX_CHAR_LIMIT = 8000

######################################################################
# Contrib config
######################################################################
if SEND_GAME_INDEX:
    GAME_INDEX_LISTING = {
        'game_status': 'beta',
        # Optional, comment out or remove if N/A
        'game_website': 'http://atharia.vertinext.com',
        'short_description': 'A Mu* in a fantasy setting.',
        # Optional but highly recommended. Markdown is supported.
        'long_description': (
            "Atharia is a game set in a fantasy world of an original making."
            "Most fantasy type things can be used as inspiration. "
        ),
        'listing_contact': 'fatesgame@gmail.com',
        # At minimum, specify this or the web_client_url options. Both is fine, too.
        'telnet_hostname': 'atharia.vertinext.com',
        'telnet_port': 12900,
        # At minimum, specify this or the telnet_* options. Both is fine, too.
        'web_client_url': 'https://atharia.vertinext.com/webclient',
    }
