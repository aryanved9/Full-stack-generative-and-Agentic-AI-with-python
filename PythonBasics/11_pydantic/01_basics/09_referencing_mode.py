from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

#  Forward ref, rebuild is required after defining the self reference model, otherwise there will performance degration.
Comment.model_rebuild()

comment = Comment(
    id=1,
    content='first comment',
    replies=[
        Comment(id=2, content='reply 1'),
        Comment(id=3, content='reply 2', replies=[
            Comment(id=4, content='nested reply 1')
        ])
    ]
)

print(comment)
print(comment.model_dump())