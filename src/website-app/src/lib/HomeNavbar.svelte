<script lang="ts">
  let navItems = [
    { title: 'Home', url: '/' },
    { title: 'About', url: '/about' }
  ];
</script>

<div class="navbar">
  <div class="navbar-start">
    <div class="dropdown">
      <label class="btn btn-ghost rounded lg:hidden">
        <button>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            ><path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h8m-8 6h16"
            />
          </svg>
        </button>
      </label>
      <ul class="menu menu-compact dropdown-content bg-primary mt-3 w-52 rounded p-2 shadow">
        {#each navItems as nav}
          <li>
            <a
              href={nav.url}
              class="text-primary-content hover:bg-base-200 rounded-lg px-3 py-2 font-medium"
              >{nav.title}
            </a>
          </li>{/each}
      </ul>
    </div>
  </div>
  <div class="navbar-center hidden lg:flex">
    <ul class="menu menu-horizontal p-0">
      {#each navItems as nav}
        <li>
          <a
            href={nav.url}
            class="text-base-content hover:bg-base-200 rounded-lg px-3 py-2 font-medium"
            >{nav.title}
          </a>
        </li>{/each}
    </ul>
  </div>
  <div class="navbar-end" />
</div>
