<script lang="ts">
  import Navbar from '$lib/HomeNavbar.svelte';
</script>

<div data-theme="black" class="h-screen">
  <Navbar />

  <slot />
</div>
