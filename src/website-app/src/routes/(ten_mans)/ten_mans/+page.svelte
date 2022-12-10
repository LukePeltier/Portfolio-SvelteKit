<script lang="ts">
  import type { PageData } from './$types';
  import Grid from 'gridjs-svelte';
  export let data: PageData;

</script>

<svelte:head>
  <title>10 Mans Statistics</title>
</svelte:head>

<div class="m-12 flex flex-row justify-items-stretch gap-4 ">
  <div>
    <Grid data={data.gamesWon} sort columns={data.gamesColumns} className={data.gameTablesClasses} />
  </div>
  <div>
    <Grid data={data.gamesPlayed} sort columns={data.gamesColumns} className={data.gameTablesClasses} />
  </div>
</div>
