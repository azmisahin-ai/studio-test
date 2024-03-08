def generate(pipe,prompt):
    images = pipe(prompt).images  
    images[0].save(f"/data/images/{word}.png")