<script lang="ts">
  import Navbar from '$lib/TenMansNavbar.svelte';
</script>

<div data-theme="dark" class="bg-base-300 flex h-full min-h-screen flex-col overflow-auto">
  <Navbar />
  <slot />
</div>
