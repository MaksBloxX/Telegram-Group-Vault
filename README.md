# Shared DM Bot — build `s1`

Two people, one bot. You and your friend each DM the bot; whatever either of
you sends into a topic is **mirrored into the other person's DM** — clean,
anonymous, duplicate-checked.

```
You ──DM──▶ BOT ◀──DM── Friend
```

> A Telegram DM only exists between one user and the bot, so the two of you
> are never in the same chat. The bot copies everything to both sides.

## Behavior

| You send… | What happens |
|---|---|
| Media in a topic | Clean copy back into **your** topic (original deleted), plus a tagged copy into your **friend's** matching topic |
| Text in a topic | Mirrored into friend's matching topic with your alias tag (your original stays) |
| Text in General (no topic) | Mirrored into friend's General with your alias tag *(since s2)* |
| Media in All-Messages | Picker buttons → chosen topic → sent to both DMs |
| Media from a `/bind`-ed chat | Relayed into the bound topic in **both** DMs |

- **Anonymous identities** — copies never show real names. Each user gets a
  persistent identity like `🦊: Outsider 🍀` (unique emoji + mystery name),
  shown in its own block **above** the caption *(since s4)*.
- **Duplicate vault** — same file never gets mirrored twice (`/dbdel` to re-share).
- **Both users have full commands** (shared command set; separate sets planned later).
- Topics are created per-DM: `/use math` makes `#math` in both DMs; missing
  partner topics are created automatically on first mirror.
- Bot's own posts never re-trigger the relay (admin filter), so no loops.

## Setup

1. `cp example_config.py config.py` → fill in token + **both** `ADMIN_IDS`.
2. **BotFather → your bot → Access → Restrict bot usage → Allowed users** = you + friend.
3. BotFather → **Bot Settings → Threads Settings → Threaded Mode ON**.
4. **Both users**: `/start` the bot → in the DM, tap the bot name on top →
   enable the **Topics** toggle. (Friend must do this or mirrors can't land.)
5. Run: `python bot.py`

## Quick test

1. You: `/use math` → topic appears in both DMs
2. You send a PDF into `#math` → clean copy for you + alias-tagged copy for friend
3. Friend sends text into `#math` → you receive `🦊: Outsider 🍀` style tag + text
4. Friend re-sends the same PDF → `🗑️ Duplicate — skipped.`

## Commands (both users)

`/help` (button menu) • `/relay` • `/use <t>` • `/topics` • `/tdel <t>` •
`/trename <old> <new>` • `/bind <t>` • `/unbind` • `/gp` • `/autodelete` •
`/db` • `/dbstats` • `/dbfind` • `/dbdel` • `/dbclear` • `/addcaption` •
`/removecaption` • `/migrate` • `/settings`

## Notes

- Re-sharing an old file to bypass the duplicate check: `/dbdel` its hash, then re-send.
- **Speed (s5):** single media relays instantly (the `ALBUM_BATCH_DELAY` wait applies
  to multi-item albums only); mirror copies are sent in parallel; all sends stay
  flood-safe with cooldowns + automatic RetryAfter handling.
- **Mirror hardening (s6):** text mirror survives partner bot-reinstalls — stale
  topic threads are auto-recreated on failure, unknown topics fall back to the
  partner's General, retry cooldowns are per-DM, and every step is logged.
- **Sticky routing (s7):** if a partner's app sends messages WITHOUT topic IDs
  (happens after bot reinstalls / older clients), they send `/use <topic>` once
  and all their General text + media is routed into that topic automatically.
- **Auto-sync + self-healing (s9):** `/start` validates every topic thread in the
  user's DM, recreates dead ones and creates missing ones. All media/text sends
  detect stale threads, recreate the topic once and retry.
- **s12 fixes:** command/status replies (incl. the one-time "Your share alias"
  notice) now land in the SAME topic the command/message came from (sticky
  fallback, then General); stickers mirror instantly like text with dup-vault
  hash check; media captions auto-truncate to Telegram's 1024-unit limit
  (entities past the cut are dropped safely); text + sticker mirrors retry
  after FloodWait instead of failing.
- **s11 fixes:** GP-ON `1+2` now merges into one group of 3 (queue flush is held
  while an album is still landing); captions with links/custom-emoji no longer
  fail to send (entities keep their `url`/`custom_emoji_id` and are shifted in
  Telegram's UTF-16 units, so emoji-heavy identity blocks can't corrupt offsets).
- Folder `Solo Topic Bot/` = single-user variant (feature-frozen).
- Never commit `config.py`, `*.db*`, `*.log`, `vault_bot.lock`, `__pycache__/`
  (see `.gitignore`).
