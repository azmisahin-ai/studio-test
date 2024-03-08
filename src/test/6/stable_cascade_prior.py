import torch
from diffusers import StableCascadeDecoderPipeline, StableCascadePriorPipeline

device = "cuda"
num_images_per_prompt = 2

prior = StableCascadePriorPipeline.from_pretrained("stabilityai/stable-cascade-prior", torch_dtype=torch.bfloat16).to(device)
decoder = StableCascadeDecoderPipeline.from_pretrained("stabilityai/stable-cascade",  torch_dtype=torch.float16).to(device)

prompt = "Anthropomorphic cat dressed as a pilot"
negative_prompt = ""



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

  prior_output = prior(
      prompt=prompt,
      height=1024,
      width=1024,
      negative_prompt=negative_prompt,
      guidance_scale=4.0,
      num_images_per_prompt=num_images_per_prompt,
      num_inference_steps=20
  )
  decoder_output = decoder(
      image_embeddings=prior_output.image_embeddings.half(),
      prompt=prompt,
      negative_prompt=negative_prompt,
      guidance_scale=0.0,
      output_type="pil",
      num_inference_steps=10
  ).images

  # Resim oluştur
  print("YAPAY ZEKA İLE YENİ RESİM ***************************")
  generated_image = decoder_output

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