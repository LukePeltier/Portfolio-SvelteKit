<svelte:head>
<title>Welcome</title>
<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
</svelte:head>
<script lang="ts">
    import { afterNavigate } from '$app/navigation';
    import { typewriter } from '$lib/Typewriter.svelte';
    import { fade } from 'svelte/transition';

    let pageVisible = false;

    afterNavigate(() => {
        pageVisible = true;
    });
</script>
<div class="flex flex-col justify-items-center">
    {#if pageVisible}
        <h1 in:typewriter class="font-robotomono font-semibold text-9xl subpixel-antialiased text-center text-zinc-300 mb-20">Luke Peltier</h1>
        <p in:fade="{{delay: 1500}}" class="font-robotomono text-5xl subpixel-antialiased text-center text-zinc-300">Projects</p>
    {/if}
</div>
