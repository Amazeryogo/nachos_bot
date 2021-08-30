from pymongo import MongoClient

client = MongoClient()
db = client.nachosbot

censor = db.censorTest


def insert_censor(word, guild_id, doneby):
    try:
        word = {
            "word" : word,
            "guild_id": guild_id,
            "added_by": doneby
        }
        censor = censor.insert_one(word)
        return 0
    except:
        return 1
    finally:
        print(word," was added in ",guild_id)


def get_words(guild_id):
    words = []
    x = censor.find({"guild_id":guild_id})
    print(x)
    words.append(x)

    return words
