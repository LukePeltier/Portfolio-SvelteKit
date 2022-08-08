<svelte:head>
<title>Welcome</title>
</svelte:head>
<script lang="ts">
    import { afterNavigate } from '$app/navigation';
    import { typewriter } from '$lib/Typewriter.svelte';
    import { fade } from 'svelte/transition';

    let pageVisible = false;
    //test
    afterNavigate(() => {
        pageVisible = true;
    });

    function testPageLoaded() {
        if(!pageVisible){
            pageVisible = true;
        }
    }

    setTimeout(testPageLoaded, 500);

</script>
<div class="flex flex-col justify-items-center">
    {#if pageVisible}
        <h1 in:typewriter class="font-robotomono font-semibold text-9xl text-center text-zinc-300 mb-20">Luke Peltier</h1>
        <div in:fade="{{delay: 1500}}" id="fadeInDiv" class="justify-center">
            <p class="font-robotomono text-5xl text-center text-zinc-300">Projects</p>
            <div class="flex justify-center">
                <div id="projectsGrid" class="grid grid-cols-3">
                    <div id="tenMansLink" class="p-10 col-start-2">
                        <a style="display:block" href="/ten_mans">
                            <div id="tenMans" class="ring ring-oldTenMansYellow p-4 rounded-lg shadow-2xl shadow-black hover:shadow-none">
                                <p class="font-lato text-3xl text-zinc-300">LoL Ten Mans</p>
                                <p class="max-w-prose text-zinc-300 font-lato">This app is a website which will display statistics in the custom matches I conduct with my friends in the video game League of Legends.</p>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    {/if}
</div>
