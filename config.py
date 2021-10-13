#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
C_PLAY=False
Y_PLAY=False
STREAM=os.environ.get("STREAM_URL", "https://t.me/tgbotsproject")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
regex_ = r"http.*"
match_ = re.match(regex_,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[-1]
elif STREAM.startswith("https://t.me/tgbotsproject"):
    try:
        msg_id=STREAM.split("/", 4)[4]
        finalurl=int(msg_id)
        Y_PLAY=True
    except:
        finalurl="https://eu10.fastcast4u.com/clubfmuae"
        print("Unable to fetch youtube playlist, starting CLUB FM")
        pass
elif match_:
    finalurl=STREAM 
else:
    C_PLAY=True
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '1768739981')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '3208228'))
    CHAT = int(os.environ.get("CHAT", "-1001500995042"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001500995042")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    CPLAY=C_PLAY
    YPLAY=Y_PLAY
    SHUFFLE=bool(os.environ.get("SHUFFLE", True))
    DELETE_HISTORY=bool(os.environ.get("DELETE_HISTORY", True))
    LIMIT=int(os.environ.get("LIMIT", 1500))
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "Y")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 15))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "07d1d53a608693a6be436ca387582d8b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2043989878:AAE3kabJuFEkhOMV7URXsuV-sCOA_ISZZkw")     
    SESSION = os.environ.get("SESSION_STRING", "AgA3_O6aM1O5Jsy-kzxxV40SYg9MtQcu_OZ3ui4GVSPHTVyvdPk2PgdXEAXUfTmYIAZiRkl2mrIhjUeybrf-jR9EGVFHw5xwZoZOJx41AEfpQ6n7s1NX1PNsBAUBJnoTUtop7WKiQGyVY3P5M44jas9eBapqPO0Ams9_60djLi1H7F1LES4HVMezPiAT6a4XDCOSJVgTbzKNUTfhjMpoWCRY4x7_xER8_ihHYWF-oSs9tp0ETw4UBrdSsD7MkpcAIm8fMfk4paMkw8T-93Dld0GGhbnRb4eKQAIhlc5u14_GpeoD3iWPT-lqG2f-Jt0XLorr3HNOyn-UTcRV4TL6Ibqxd9_byAA")
    playlist=[]
    msg = {}
    CONV = {}
