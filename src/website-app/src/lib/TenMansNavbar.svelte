<script lang="ts">
  let navItems = [
    { title: 'Player Draft Stats', url: '/ten-mans/player-draft-stats' },
    { title: 'Leaderboards', url: '/ten-mans/leaderboards' },
    { title: 'Games', url: '/ten-mans/games' },
    { title: 'Champions', url: '/ten-mans/champions' }
  ];
</script>

<nav class="sm:justify-center space-x-4 bg-zinc-800 mb-8">
  <div class="grid grid-cols-10 py-4 text-center">
    <a
      href="/ten-mans"
      class="rounded-lg px-3 py-2 text-zinc-100 font-bold hover:bg-zinc-900 hover:text-zinc-100"
      >10 Mans Statistics</a
    >
    {#each navItems as nav}
      <a
        href={nav.url}
        class="rounded-lg px-3 py-2 text-zinc-300 font-medium hover:bg-zinc-900 hover:text-zinc-100"
        >{nav.title}</a
      >
    {/each}
    <a
      href="/"
      class="rounded-lg px-3 py-2 text-zinc-300 font-medium hover:bg-zinc-900 hover:text-zinc-100 col-end-12"
      >Return to Portfolio</a
    >
  </div>
</nav>
