<script lang="ts">
  import Icon from '@iconify/svelte';
  import { afterNavigate } from '$app/navigation';
  import { typewriter } from '$lib/Typewriter.svelte';
  import { fly } from 'svelte/transition';
  import { backOut } from 'svelte/easing';
  import arrowRight from '@iconify/icons-akar-icons/arrow-right';

  let pageVisible = false;
  //test
  afterNavigate(() => {
    pageVisible = true;
  });

  function testPageLoaded() {
    if (!pageVisible) {
      pageVisible = true;
    }
  }

  setTimeout(testPageLoaded, 500);
</script>

<svelte:head>
  <title>Welcome</title>
</svelte:head>
<div class="flex flex-col justify-items-center">
  {#if pageVisible}
    <h1
      in:typewriter={{}}
      class="font-robotomono text-neutral-content mb-20 text-center text-9xl font-semibold"
    >
      Luke Peltier
    </h1>
    <div
      in:fly={{ delay: 1500, y: 500, duration: 2000, easing: backOut }}
      id="fadeInDiv"
      class="justify-center"
    >
      <p class="font-robotomono text-neutral-content text-center text-5xl">Projects</p>
      <div class="flex justify-center">
        <div
          class="card-bordered border-oldTenMansYellow text-oldTenMansYellow-content mt-10 w-96 rounded-lg"
        >
          <div class="card-body">
            <h2 class="card-title">LoL Ten Mans</h2>
            <p>
              This app is a website which will display statistics in the custom matches I conduct
              with my friends in the video game League of Legends.
            </p>
            <div class="card-actions justify-end">
              <a href="/ten_mans"><button class="btn"><Icon icon={arrowRight} /></button></a>
            </div>
          </div>
        </div>
        <!-- </div> -->
      </div>
    </div>
  {/if}
</div>
