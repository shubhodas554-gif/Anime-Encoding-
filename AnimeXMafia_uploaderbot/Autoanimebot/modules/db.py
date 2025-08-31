import json
import os

DB_FILE = "database.json"

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"animes": [], "uploads": [], "failed": [], "votes": []}, f)

async def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

async def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Anime DB
async def get_animesdb():
    db = await load_db()
    return db.get("animes", [])

async def save_animedb(anime_id, pos):
    db = await load_db()
    db["animes"].append({"id": anime_id, "pos": pos})
    await save_db(db)

async def del_anime(anime_id):
    db = await load_db()
    db["animes"] = [x for x in db["animes"] if x["id"] != anime_id]
    await save_db(db)

# Uploads
async def get_uploads():
    db = await load_db()
    return db.get("uploads", [])

async def save_uploads(anime_id, quality):
    db = await load_db()
    db["uploads"].append({"id": anime_id, "q": quality})
    await save_db(db)

async def is_uploaded(anime_id):
    db = await load_db()
    for x in db.get("uploads", []):
        if x["id"] == anime_id:
            return True
    return False

async def is_quality_uploaded(anime_id, q):
    db = await load_db()
    for x in db.get("uploads", []):
        if x["id"] == anime_id and x.get("q") == q:
            return True
    return False

# Failed
async def is_failed(anime_id):
    db = await load_db()
    return anime_id in db.get("failed", [])

async def add_to_failed(anime_id):
    db = await load_db()
    if anime_id not in db["failed"]:
        db["failed"].append(anime_id)
    await save_db(db)

# Votes
async def is_voted(msg_id, user_id):
    db = await load_db()
    for vote in db.get("votes", []):
        if vote["msg"] == msg_id and vote["user"] == user_id:
            return True
    return False

async def save_vote(msg_id, user_id):
    db = await load_db()
    db["votes"].append({"msg": msg_id, "user": user_id})
    await save_db(db)

# Channel
async def save_channel(anime_id, post, dl_id, episodes):
    db = await load_db()
    if "channels" not in db:
        db["channels"] = {}
    db["channels"][anime_id] = {"post": post, "dl_id": dl_id, "episodes": episodes}
    await save_db(db)

async def get_channel(anime_id):
    db = await load_db()
    c = db.get("channels", {}).get(anime_id, None)
    if not c:
        return 0, {}, 0
    return c.get("dl_id"), c.get("episodes"), c.get("post")
