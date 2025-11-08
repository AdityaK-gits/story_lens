from pydantic import BaseModel

class Scene(BaseModel):
    title: str
    description: str
    image: object  # PIL.Image
