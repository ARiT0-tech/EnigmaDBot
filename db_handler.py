from class_db import DataMsg
import db_session


def db_create():
    db_session.global_init("db_msg.db")


def create_msg(id_s, id_m, name, i, end):
    db_sess = db_session.create_session()
    msgs = list()
    for msg in db_sess.query(DataMsg).filter((DataMsg.srv_id == id_s) | (DataMsg.msg_id == id_m)):
        msgs.append(msg)
    if len(msgs) != 0:
        for msg in db_sess.query(DataMsg).filter((DataMsg.srv_id == id_s) | (DataMsg.msg_id == id_m)):
            msg.i, msg.end, msg.name = i, end, name
        db_sess.commit()
    else:
        msg = DataMsg()
        msg.srv_id = id_s
        msg.msg_id = id_m
        msg.i = i
        msg.end = end
        msg.name = name
        db_sess.add(msg)
        db_sess.commit()
