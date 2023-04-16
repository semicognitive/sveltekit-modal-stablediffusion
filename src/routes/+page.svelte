<script lang="ts">
    import { enhance } from "$app/forms";

    let loading: boolean = false;
    let error: string | undefined;
    let image: string | undefined;

    // Try a good prompt like: An oil painting of a golden retriever

    /* Just an example of how to simply handle an endpoint - your endpoints act just like any other! */
    function api_prompt() {
        loading = true;
        error = undefined;
        image = undefined;

        return ({ result }: any) => {
            loading = false;
            error = result.error;
            image = result.image;
        };
    }
</script>

<main class="flex flex-col space-y-2">
    <h1 class="text-3xl font-bold underline">Stable Diffusion!</h1>
    <p>Example made wiith <a target="_blank" rel="noopener noreferrer" class="underline" href="https://github.com/semicognitive/sveltekit-modal/tree/main">sveltekit-modal</a>.</p>

    <form method="POST" action="/api/prompt" use:enhance={api_prompt} class="flex flex-col space-y-2 md:min-w-[28rem] lg:min-w-[32rem] xl:min-w-[36rem] max-w-6xl">
        {#if loading}
            <div class="flex flex-col items-center justify-center w-full aspect-square border-2 border-neutral-300 border-dashed rounded-lg cursor-pointer bg-neutral-50 text-transparent">
                <svg class="my-auto animate-spin h-6 w-6 text-black" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                </svg>
            </div>
        {:else}
            <img alt="Generated Output" src={image} class="flex flex-col items-center justify-center w-full aspect-square border-2 border-neutral-300 border-dashed rounded-lg cursor-pointer bg-neutral-50 text-transparent" />
        {/if}

        <span class="flex flex-row space-x-4">
            <input
                type="text"
                placeholder="Prompt"
                name="prompt"
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-black sm:text-sm sm:leading-6" />
            <button
                type="submit"
                class="inline-flex items-center rounded-md border border-transparent bg-neutral-800 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-black focus:outline-none focus:ring-2 focus:ring-black focus:ring-offset-2">
                Generate!
            </button>
        </span>

        <span class="flex flex-row space-x-4">
            {#if error}
                <span class="my-auto text-red-500">{error}</span>
            {/if}
        </span>
    </form>
</main>
