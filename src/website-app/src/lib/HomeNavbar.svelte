<script lang="ts">
  let navItems = [
    { title: 'Home', url: '/' },
    { title: 'About', url: '/about' }
  ];
</script>

<div class="navbar">
  <div class="navbar-start">
    <div class="dropdown">
      <div class="btn btn-ghost lg:hidden">
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
          /></svg
        >
      </div>
      <ul class="menu menu-compact dropdown-content bg-base-100 rounded-box mt-3 w-52 p-2 shadow">
        {#each navItems as nav}
          <li>
            <a
              href={nav.url}
              class="rounded-lg px-3 py-2 font-medium text-zinc-300 hover:bg-zinc-900 hover:text-zinc-100"
              >{nav.title}</a
            >
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
            class="rounded-lg px-3 py-2 font-medium text-zinc-300 hover:bg-zinc-900 hover:text-zinc-100"
            >{nav.title}</a
          >
        </li>{/each}
    </ul>
  </div>
  <div class="navbar-end" />
</div>
