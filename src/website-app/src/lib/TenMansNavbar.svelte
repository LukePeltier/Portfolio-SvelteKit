<script lang="ts">
  import Icon from '@iconify/svelte';
  import arrowLeft from '@iconify/icons-akar-icons/arrow-left';
  let navItems = [
    { title: 'Standings', url: '/ten_mans/standings' },
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
      class="font-tenmansbold bg-neutral mb-8 w-full space-x-4 text-lg lg:flex lg:items-center lg:justify-between"
    >
      <div class="flex items-center justify-between">
        <a
          href="/"
          class="text-neutral-content hover:bg-neutral-focus rounded-lg px-3 py-2 font-medium"
        >
          <Icon icon={arrowLeft} />
        </a>
        <a
          href="/ten_mans"
          class="text-neutral-content hover:bg-neutral-focus rounded-lg px-3 py-2 text-xl font-bold lg:text-2xl"
          >10 Mans Statistics</a
        >
        <!-- Mobile menu button -->
        <div on:click={toggleNavbar} on:keypress={toggleNavbar} class="flex lg:hidden">
          <button
            type="button"
            class="text-neutral-content focus:text-neutral-focus-content focus:outline-none"
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
            class="hover:bg-neutral-focus text-neutral-content rounded-lg px-3 py-2 font-medium"
            >{nav.title}</a
          >
        {/each}
      </div>
    </nav>
  </div>
</div>
