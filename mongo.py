from pymongo import MongoClient

client = MongoClient()
db = client.nachosbot
censor = db.censor


def insert(word, guild_id, doneby):
    try:
        word = {
            "word" : word,
            "guild_id": guild_id,
            "added_by": doneby
        }
        censorx = censor.insert_one(word)
        print(censorx)
        return 0
    except:
        return 1
    finally:
        print(word," was added in ",guild_id)

def get_word(guild_id):
    words = []
    for x in censor.find():
        if x["guild_id"] == guild_id:
            words.append(x["word"])
        else:
            pass
    return words

def delete_word(word,guild_id):
    query = {
        "word" : word,
        "guild_id": guild_id
    }
    censor.delete_one(query)
    return 0
