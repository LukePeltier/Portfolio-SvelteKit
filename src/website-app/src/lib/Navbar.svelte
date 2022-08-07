<script lang="ts">
    let navItems = [
    {title: "Home", url: "/"},
    {title: "About", url: "/about"},
  ]
</script>


<nav class="flex sm:justify-center space-x-4 bg-zinc-800 mb-8">
    {#each navItems as nav}
        <a href={nav.url} class="rounded-lg px-3 py-2 text-zinc-300 font-medium hover:bg-zinc-900 hover:text-zinc-100">{nav.title}</a>
    {/each}
</nav>