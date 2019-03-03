import json


class Response:
    @staticmethod
    def failure(message: str, status: int = 400):
        return json.dumps({
            "status": status,
            "error": message
        })

    @staticmethod
    def success(data: any, status: int = 200):
        return json.dumps({
            "status": status,
            "data": str(data)
        })
