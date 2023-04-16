import modal
import os

model_id = "runwayml/stable-diffusion-v1-5"
cache_path = "/vol/cache"


def download_models():
    import diffusers
    import torch

    hugging_face_token = os.environ["HUGGINGFACE_TOKEN"]

    # Download scheduler configuration. Experiment with different schedulers
    # to identify one that works best for your use-case.
    scheduler = diffusers.DPMSolverMultistepScheduler.from_pretrained(
        model_id,
        subfolder="scheduler",
        use_auth_token=hugging_face_token,
        cache_dir=cache_path,
    )
    scheduler.save_pretrained(cache_path, safe_serialization=True)

    # Downloads all other models.
    pipe = diffusers.StableDiffusionPipeline.from_pretrained(
        model_id,
        use_auth_token=hugging_face_token,
        revision="fp16",
        torch_dtype=torch.float16,
        cache_dir=cache_path,
    )
    pipe.save_pretrained(cache_path, safe_serialization=True)


image = (
    modal.Image.debian_slim(python_version="3.10")
    .pip_install(
        "accelerate",
        "diffusers[torch]>=0.10",
        "ftfy",
        "torch",
        "torchvision",
        "transformers",
        "triton",
        "safetensors",
    )
    .pip_install("xformers", pre=True)
    .run_function(
        download_models,
        secrets=[modal.Secret.from_name("my-huggingface-secret")],
    )
)

config = {
    'name': 'sveltekit-modal-stablediffusion',
    'log': False,
    'stub_asgi': {
        'gpu': 'A10G',
        'image': image,
        'secret': modal.Secret.from_name("my-openai-secret"),
    }
}