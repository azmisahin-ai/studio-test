from PIL import Image

from src.yapay_modul.stable_cascade_prior import create_image_with_ai

def test_create_image_with_ai():
  """
  create_image_with_ai fonksiyonunu test eder.
  """

  # Farklı metin açıklamaları ve parametre değerleri
  prompts = [
    "Bir orman manzarası",
    "Bir deniz manzarası",
    "Bir portre",
    "Bir soyut resim",
  ]

  parameters = [
    {
      "style": "default",
      "negative_prompt": "",
      "output_type": "pil",
      "num_inference_steps": 10,
      "guidance_scale": 0.5,
      "lcm_origin_steps": 5,
      "width": 500,
      "height": 500,
    },
    {
      "style": "realistic",
      "negative_prompt": "cartoon",
      "output_type": "png",
      "num_inference_steps": 20,
      "guidance_scale": 0.7,
      "lcm_origin_steps": 10,
      "width": 768,
      "height": 512,
    },
  ]

  # Her metin açıklaması ve parametre seti için resim oluştur
  for prompt in prompts:
    for params in parameters:
      generated_image = create_image_with_ai(prompt, **params)

      # Oluşturulan resmi göster
      Image.show(generated_image)

if __name__ == "__main__":
  test_create_image_with_ai()
