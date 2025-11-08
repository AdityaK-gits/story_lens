from models import Scene
from llm import generate_scenes
from image_gen import generate_image

def build_story(prompt: str, num_scenes: int = 5):
    raw_scenes = generate_scenes(prompt, num_scenes)
    story = []
    for i, desc in enumerate(raw_scenes):
        img = generate_image(desc)
        scene = Scene(title=f"Scene {i+1}", description=desc, image=img)
        story.append(scene)
    return story
