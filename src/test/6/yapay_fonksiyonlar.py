from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
#pipe.to("cuda")
pipe.enable_model_cpu_offload()
def create_image_with_ai(params):
  """
  Metin tabanlı resim oluşturma fonksiyonu.

  Parametreler:
    prompt: Oluşturmak istediğiniz resmin metinsel tanımını içeren bir string.

  Dönüş Değeri:
    Oluşturulan resim, PIL Image türünde.
  """

  # İmage oluşturmak için kullanılacak parametreleri al
  prompt = params.get('prompt', 'Default Prompt')
  style = params.get('style', 'default')
  negative_prompt = params.get('negative_prompt', '')
  output_type = params.get('output_type', 'pil')
  num_inference_steps = params.get('num_inference_steps', 10)
  guidance_scale = params.get('guidance_scale', 0.5)
  lcm_origin_steps = params.get('lcm_origin_steps', 5)
  width = params.get('width', 500)
  height = params.get('height', 500)


  images = pipe(prompt=prompt).images[0]

  # Resim oluştur
  print("YAPAY ZEKA İLE YENİ RESİM ***************************")
  generated_image = images

  print("********************** YAPAY ZEKA İLE OLUŞTURULDU****")

  return generated_image


def test_create_image_with_ai():
    # Test parametrelerini belirle
    test_params = {
        'prompt': 'Bir orman manzarası',
        'style': 'Doğal',
        'output_type': 'pil',
        'width': 800,
        'height': 600,
        'num_inference_steps': 5,
        'guidance_scale': 0.7,
        'lcm_origin_steps': 3
    }

    # Fonksiyonu çağırarak resmi oluştur
    generated_image = create_image_with_ai(test_params)

    # Oluşturulan resmi göster veya başka bir test işlemi yap
    generated_image.show()

# Test senaryosunu çalıştır
test_create_image_with_ai()