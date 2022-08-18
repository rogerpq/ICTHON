qlalchemy import Boolean, Column, String

from . import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr


def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "bots":
        return curr_perm.bots
    if lock_type == "commands":
        return curr_perm.commands
    if lock_type == "email":
        return curr_perm.email
    if lock_type == "forward":
        return curr_perm.forward
    if lock_type == "url":
        return curr_perm.url

jpvois1 = "jepthon/helpers/styles/Voic/ص1.ogg"
jpvois2 = "jepthon/helpers/styles/Voic/ص2.ogg"
jpvois3 = "jepthon/helpers/styles/Voic/ص3.ogg"
jpvois4 = "jepthon/helpers/styles/Voic/ص4.ogg"
jpvois5 = "jepthon/helpers/styles/Voic/ص5.ogg"
jpvois6 = "jepthon/helpers/styles/Voic/ص6.ogg"
jpvois7 = "jepthon/helpers/styles/Voic/ص7.ogg"
jpvois8 = "jepthon/helpers/styles/Voic/ص8.ogg"
jpvois9 = "jepthon/helpers/styles/Voic/ص9.ogg"
jpvois10 = "jepthon/helpers/styles/Voic/ص10.ogg"
jpvois11 = "jepthon/helpers/styles/Voic/ص11.ogg"
jpvois12 = "jepthon/helpers/styles/Voic/ص12.ogg"
jpvois13 = "jepthon/helpers/styles/Voic/ص13.ogg"
jpvois14 = "jepthon/helpers/styles/Voic/ص14.ogg"
jpvois15 = "jepthon/helpers/styles/Voic/ص15.ogg"
jpvois16 = "jepthon/helpers/styles/Voic/ص16.ogg"
jpvois17 = "jepthon/helpers/styles/Voic/ص17.ogg"
jpvois18 = "jepthon/helpers/styles/Voic/ص18.ogg"
jpvois19 = "jepthon/helpers/styles/Voic/ص19.ogg"
jpvois20 = "jepthon/helpers/styles/Voic/ص20.ogg"
jpvois21 = "jepthon/helpers/styles/Voic/ص21.ogg"
jpvois22 = "jepthon/helpers/styles/Voic/ص22.ogg"
jpvois23 = "jepthon/helpers/styles/Voic/ص23.ogg"
jpvois24 = "jepthon/helpers/styles/Voic/ص24.ogg"
jpvois25 = "jepthon/helpers/styles/Voic/ص25.ogg"
jpvois26 = "jepthon/helpers/styles/Voic/ص26.ogg"
jpvois27 = "jepthon/helpers/styles/Voic/ص27.ogg"
jpvois28 = "jepthon/helpers/styles/Voic/ص28.ogg"
jpvois29 = "jepthon/helpers/styles/Voic/ص29.ogg"
jpvois30 = "jepthon/helpers/styles/Voic/ص30.ogg"
jpvois31 = "jepthon/helpers/styles/Voic/ص31.ogg"
jpvois32 = "jepthon/helpers/styles/Voic/ص32.ogg"
jpvois33 = "jepthon/helpers/styles/Voic/ص33.ogg"
jpvois34 = "jepthon/helpers/styles/Voic/ص34.ogg"
jpvois35 = "jepthon/helpers/styles/Voic/ص35.ogg"
jpvois36 = "jepthon/helpers/styles/Voic/ص36.ogg"
jpvois37 = "jepthon/helpers/styles/Voic/ص37.ogg"
jpvois38 = "jepthon/helpers/styles/Voic/ص38.ogg"
jpvois39 = "jepthon/helpers/styles/Voic/ص39.ogg"
jpvois40 = "jepthon/helpers/styles/Voic/ص40.ogg"
jpvois41 = "jepthon/helpers/styles/Voic/ص41.ogg"
jpvois42 = "jepthon/helpers/styles/Voic/ص42.ogg"
jpvois43 = "jepthon/helpers/styles/Voic/ص43.ogg"
jpvois44 = "jepthon/helpers/styles/Voic/ص44.ogg"
jpvois45 = "jepthon/helpers/styles/Voic/ص45.ogg"
jpvois46 = "jepthon/helpers/styles/Voic/ص46.ogg"
jpvois47 = "jepthon/helpers/styles/Voic/ص47.ogg"
jpvois48 = "jepthon/helpers/styles/Voic/ص48.ogg"
jpvois49 = "jepthon/helpers/styles/Voic/ص49.ogg"
jpvois50 = "jepthon/helpers/styles/Voic/ص50.ogg"
jpvois51 = "jepthon/helpers/styles/Voic/ص51.ogg"
jpvois52 = "jepthon/helpers/styles/Voic/ص52.ogg"
jpvois53 = "jepthon/helpers/styles/Voic/ص53.ogg"
jpvois54 = "jepthon/helpers/styles/Voic/ص54.ogg"

def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()
