import random, hashlib, json, base64, hmac
from django.utils.timezone import utc
from datetime import datetime

def now():
    return datetime.utcnow().replace(tzinfo=utc)

def make_uuid(size=None):
    "Returns a unique id"
    x = random.getrandbits(256)
    u = hashlib.md5(str(x)).hexdigest()
    u = u[:size]
    return u

def encode(data, key):
    text = json.dumps(data)
    text = base64.urlsafe_b64encode(text)
    digest = hmac.new(key, text).hexdigest()
    return text, digest

def decode(text, digest, key):
    if digest != hmac.new(key, text).hexdigest():
        raise Exception("message does not match the digest")
    text = base64.urlsafe_b64decode(text)
    data = json.loads(text)
    return data

def always_true(*args, **kwargs):
    "A helper we can substitue into any conditional function call"
    return True