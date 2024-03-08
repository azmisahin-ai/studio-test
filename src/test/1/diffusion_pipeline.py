# diffusion_pipeline.py

from diffusers import DiffusionPipeline, StableDiffusionPipeline, DPMSolverMultistepScheduler, EulerDiscreteScheduler,AutoPipelineForText2Image,LCMScheduler,StableDiffusionXLPipeline,EulerAncestralDiscreteScheduler,AutoencoderKL
import torch

class CustomDiffusionPipeline:
    _loaded_models = {}

    def __init__(self, model_id="stabilityai/stable-diffusion-2-1"):
        self.model_id = model_id
        self.load_pipeline_by_id()

    def load_pipeline_by_id(self):
        # Önceden yüklenmişse, tekrar yükleme
        if self.model_id in CustomDiffusionPipeline._loaded_models:
            self.pipe = CustomDiffusionPipeline._loaded_models[self.model_id]
        else:
            # Yüklenmemişse, modeli yükle
            if self.model_id == "stabilityai/stable-diffusion-xl-base-1.0":
                # 1
                self.pipe = DiffusionPipeline.from_pretrained(self.model_id, use_safetensors=True, variant="fp16")
            elif self.model_id == "runwayml/stable-diffusion-v1-5":
                # 2
                self.pipe = DiffusionPipeline.from_pretrained(self.model_id)
            elif self.model_id == "CompVis/stable-diffusion-v1-4":
                # 3
                self.pipe = DiffusionPipeline.from_pretrained(self.model_id)
            elif self.model_id == "stabilityai/stable-diffusion-2-1":
                # 4
                self.pipe = DiffusionPipeline.from_pretrained(self.model_id)
                self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(self.pipe.scheduler.config)
            elif self.model_id == "stabilityai/stable-diffusion-2":
                # 5
                scheduler = EulerDiscreteScheduler.from_pretrained(self.model_id, subfolder="scheduler")
                self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, scheduler=scheduler)
            elif self.model_id == "stabilityai/sdxl-turbo":
                # 6
                self.pipe = AutoPipelineForText2Image.from_pretrained(self.model_id, variant="fp16")
            elif self.model_id == "Lykon/dreamshaper-7":
                # 7
                self.pipe = AutoPipelineForText2Image.from_pretrained(self.model_id,  variant="fp16")
                self.pipe.scheduler = LCMScheduler.from_config(self.pipe.scheduler.config)
            
                # load and fuse lcm lora
                adapter_id = "latent-consistency/lcm-lora-sdv1-5"
                self.pipe.load_lora_weights(adapter_id)
                self.pipe.fuse_lora()
            elif self.model_id == "SimianLuo/LCM_Dreamshaper_v7":
                # 8
                self.pipe = DiffusionPipeline.from_pretrained(self.model_id, use_safetensors=True, variant="fp16")
            elif self.model_id == "segmind/SSD-1B":
                # 9
                self.pipe = StableDiffusionXLPipeline.from_pretrained(self.model_id,  use_safetensors=True, variant="fp16")
            elif self.model_id == "cagliostrolab/animagine-xl-3.0":
                # 10
                # Load VAE component
                vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix")
                self.pipe = StableDiffusionXLPipeline.from_pretrained(self.model_id, use_safetensors=True, vae=vae) 
                self.pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(self.pipe.scheduler.config)
            else:
                raise ValueError(f"Unsupported model_id: {self.model_id}")
            
            # To save GPU memory, torch.float16 can be used, but it may compromise image quality.
            self.pipe.to("cuda")
            # Yüklenen modelleri kaydet
            CustomDiffusionPipeline._loaded_models[self.model_id] = self.pipe
    
    def update_model_id(self, new_model_id):
        # Kullanıcıdan gelen yeni model kimliğini alarak pipeline'ı güncelle
        self.model_id = new_model_id
        self.load_pipeline_by_id()

    def process_image(self, prompt, negative_prompt, cache):
        # Implement the logic to process the image using self.pipe
        # Make sure to return the processed image path
        # Example: 
        # processed_image_path = some_processing_logic(self.pipe, prompt, negative_prompt, cache)
        # return processed_image_path
        pass
