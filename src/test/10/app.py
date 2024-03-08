import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import os
import pickle

class DiffusionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diffusion App")

        # GUI öğelerini oluştur
        self.label_prompt = ttk.Label(root, text="Prompt:")
        self.entry_prompt = ttk.Entry(root, width=50)
        self.button_generate = ttk.Button(root, text="Generate Image", command=self.generate_image)
        self.image_label = ttk.Label(root)

        # GUI öğelerini düzenle
        self.label_prompt.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_prompt.grid(row=0, column=1, padx=10, pady=10)
        self.button_generate.grid(row=1, column=0, columnspan=2, pady=10)
        self.image_label.grid(row=2, column=0, columnspan=2, pady=10)

        # DiffusionPipeline'ı bir kere yükle ve bellekte tut
        model_id = "stabilityai/stable-diffusion-2-1"
        self.pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(self.pipe.scheduler.config)
        self.pipe = self.pipe.to("cuda")

    def generate_image(self):
        prompt = self.entry_prompt.get()

        # Önbellek dosyasını kontrol et
        cache_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cached_result_app.pkl")
        if os.path.exists(cache_file_path):
            # Önbellek dosyasından sonuçları yükle
            with open(cache_file_path, 'rb') as cache_file:
                images = pickle.load(cache_file)
        else:
            # DiffusionPipeline'ı kullanarak işlemi gerçekleştir
            images = self.pipe(prompt=prompt).images

            # Sonuçları önbelleğe kaydet
            with open(cache_file_path, 'wb') as cache_file:
                pickle.dump(images, cache_file)

        # İmage'ı görüntüle
        image = images[0]
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = DiffusionApp(root)
    root.mainloop()
