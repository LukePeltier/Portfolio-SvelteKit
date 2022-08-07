<svelte:head>
<title>Welcome</title>
<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
</svelte:head>
<script lang="ts">
    import { afterNavigate } from '$app/navigation';

    let nameVisible = false;

    afterNavigate(() => {
        nameVisible = true;
    });

    function typewriter(node: HTMLElement, {delay = 2, speed = 1}) {
        const valid = (
            node.childNodes.length === 1 &&
            node.childNodes[0].nodeType === Node.TEXT_NODE
        );

        if (!valid) {
            throw new Error(`This transition only works on elements with a single text node child`);
        }
        const text = node.textContent;
        if (text == null) {
            throw new Error(`No text found`);
        }
	    const duration = text.length / (speed * 0.01);

        return {
            delay,
            duration,
            tick: (t: number) => {
                const i = Math.trunc(text.length * t);
                node.textContent = text.slice(0, i);
            }
        }
    }


</script>
<div class="flex flex-col justify-items-center">
    {#if nameVisible}
        <h1 in:typewriter class="font-lato font-semibold text-9xl subpixel-antialiased text-center text-zinc-300">Luke Peltier</h1>
    {/if}
</div>