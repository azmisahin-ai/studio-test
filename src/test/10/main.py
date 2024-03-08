import picture

def main():
    params = {
    "creator":4,
    "prompt": "Children playing video games suddenly turn into heroes helping nature. cinematic.",
    "negative_prompt":"ugly, blurry, poor quality, nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name",
    "num_inference_steps":1,
    "guidance_scale":0.0,
    "lcm_origin_steps":1,
    "output_type":"pil",
    "width":512,
    "height":512
    }

    generate(promt=params["prompt"])    
    

if __name__ == "__main__":
    main()
