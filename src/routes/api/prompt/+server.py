import io
import base64

from fastapi import Form


async def POST(prompt: str = Form()):
    import diffusers
    import torch

    torch.backends.cuda.matmul.allow_tf32 = True

    scheduler = diffusers.DPMSolverMultistepScheduler.from_pretrained(
        "/vol/cache",
        subfolder="scheduler",
        solver_order=2,
        prediction_type="epsilon",
        thresholding=False,
        algorithm_type="dpmsolver++",
        solver_type="midpoint",
        denoise_final=True,
    )

    pipe = diffusers.StableDiffusionPipeline.from_pretrained("/vol/cache", scheduler=scheduler).to("cuda")
    pipe.enable_xformers_memory_efficient_attention()

    with torch.inference_mode(), torch.autocast("cuda"), io.BytesIO() as buf:
        image = pipe([prompt], num_inference_steps=20, guidance_scale=7.0).images[0]
        image.save(buf, format="PNG")    

        return { "image": f"data:image/png;base64,{base64.b64encode(buf.getvalue()).decode('utf-8')}" }