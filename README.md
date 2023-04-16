<img width="1676" alt="Xnapper-2023-04-15-23 13 16" src="https://user-images.githubusercontent.com/20548516/232266073-e7cbe1b1-6af1-48a9-92b7-08e8f3a80a30.png">

# sveltekit-modal-stablediffusion

An example SvelteKit project using https://github.com/semicognitive/sveltekit-modal, showing how easy it is to write Python endpoints in SvelteKit.

See the code for the [example `+server.py` route here](src/routes/api/summarize/%2Bserver.py). You'll see it largely mirrors the SvelteKit built-in [`+server.js`](https://kit.svelte.dev/docs/routing#server)!

## This example 
- Includes a frontend written in [TailwindCSS](https://tailwindcss.com)
- Has a `api/summarize` endpoint which takes a PDF upload, and summarizes it with the OpenAI Api! Written in Python with [Stable Diffusion](https://github.com/CompVis/stable-diffusion)
