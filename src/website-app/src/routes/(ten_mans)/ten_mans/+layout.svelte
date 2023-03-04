<script lang="ts">
  import Navbar from '$lib/TenMansNavbar.svelte';
</script>

<div data-theme="dark" class="bg-base-200 flex h-screen flex-col">
  <Navbar />
  <slot />
</div>

<style>
  @import 'https://cdn.jsdelivr.net/npm/gridjs/dist/theme/mermaid.min.css';
</style>
