from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_scenes(prompt: str, num_scenes: int = 5):
    scenes = []
    for i in range(num_scenes):
        output = generator(f"Scene {i+1}: {prompt}", max_length=80, num_return_sequences=1)[0]["generated_text"]
        scenes.append(output.strip())
    return scenes
