from typing import Optional, List

from pydantic import BaseModel

class Message(BaseModel):
    type: str
    arguments: Optional[List[str|int]]
    body: dict


if __name__ == '__main__':
    try:
        message = {
            "type": "SomeType",
            "arguments": [10, 'lol'],
            "body": {'some': "body"},
        }
        message = Message(**message)
    except Exception as e:
        print(e)
    print(message)