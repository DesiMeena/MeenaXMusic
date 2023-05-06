from MeenaX.core.bot import MeenaXBot
from MeenaX.core.dir import dirr
from MeenaX.core.git import git
from MeenaX.core.userbot import Userbot
from MeenaX.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = MeenaXBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
