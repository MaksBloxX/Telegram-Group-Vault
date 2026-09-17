# =====================================================
#  SHARED DM BUILD — copy this file as "config.py" and
#  fill in your values. NEVER upload config.py!
# =====================================================

# --- Bot tokens (get from @BotFather) ---
BOT_TOKENS = [
    "",   # Bot 1 — paste token here
]

# --- The two authorized users: you + friend ---
# Both get FULL control (all commands). Everyone else is silently
# ignored (also lock it server-side: BotFather → Access → Restrict
# bot usage → Allowed users = you + friend).
ADMIN_IDS = [
    6584528626,   # you
    0,            # friend's Telegram ID
]

# --- Databases ---
NEW_DB_NAME = "media_new.db"     # live vault (topics + bindings + aliases)
OLD_DB_NAME = ""                 # legacy drain — set "media.db" if you want migration

# --- Timers & limits ---
ALBUM_BATCH_DELAY = 3.5   # wait for album parts ONLY (single media = instant since s5)
QUEUE_COOLDOWN    = 1.0   # flood-safe gap between album chunk sends
MAX_DELETE_CHUNK  = 100

# --- Migration default ---
MIGRATE_DEFAULT = True

# --- Default settings (per bot, changeable via commands) ---
DEFAULT_SETTINGS = {
    "autodelete"     : True,   # delete original after relay ("move" mode)
    "custom_caption" : None,
    "auto_group"     : True,
    "db_check"       : True,
    "relay"          : True,   # relay + mirror into DM topics
}
