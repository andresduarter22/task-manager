from flask_restful import abort


class CustomException(Exception):

    @staticmethod
    def abort_if_entry_doesnt_exist(id_entry, collection):
        if collection.find_one({"_id": int(id_entry)}) is None:
            abort(400, message="Entry doesn't exist")
