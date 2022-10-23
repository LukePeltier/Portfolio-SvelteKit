<script lang="ts">
  import Icon from '@iconify/svelte';
  import arrowLeft from '@iconify/icons-akar-icons/arrow-left';
  let navItems = [
    { title: 'Player Draft Stats', url: '/ten_mans/player-draft-stats' },
    { title: 'Leaderboards', url: '/ten_mans/leaderboards' },
    { title: 'Games', url: '/ten_mans/games' },
    { title: 'Champions', url: '/ten_mans/champions' }
  ];

  let showMenu = false;

  function toggleNavbar() {
    showMenu = !showMenu;
  }
</script>

<div>
  <div>
    <nav
      class="font-tenmansbold mb-8 w-full space-x-4 bg-zinc-800 text-lg lg:flex lg:items-center lg:justify-between"
    >
      <div class="flex items-center justify-between">
        <a
          href="/"
          class="rounded-lg px-3 py-2 font-medium text-zinc-300 hover:bg-zinc-900 hover:text-zinc-100"
        >
          <Icon icon={arrowLeft} />
        </a>
        <a
          href="/ten_mans"
          class="rounded-lg px-3 py-2 text-xl font-bold text-zinc-100 hover:bg-zinc-900 hover:text-zinc-100 lg:text-2xl"
          >10 Mans Statistics</a
        >
        <!-- Mobile menu button -->
        <div on:click={toggleNavbar} on:keypress={toggleNavbar} class="flex lg:hidden">
          <button
            type="button"
            class="text-zinc-300 hover:text-gray-400 focus:text-gray-400 focus:outline-none"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="h-6 w-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
              />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
      <div
        class="mt-8 flex-col space-y-4 pr-8 lg:mt-0 lg:flex lg:flex-row lg:items-center lg:space-y-0 lg:space-x-10 {showMenu
          ? 'flex'
          : 'hidden'}"
      >
        {#each navItems as nav}
          <a
            href={nav.url}
            class="rounded-lg px-3 py-2 font-medium text-zinc-300 hover:bg-zinc-900 hover:text-zinc-100"
            >{nav.title}</a
          >
        {/each}
      </div>
    </nav>
  </div>
</div>
