<script lang="ts">
  import '../../../app.css';
  import Navbar from '$lib/TenMansNavbar.svelte';
</script>

<div data-theme="dark" class="h-screen w-screen">
  <Navbar />

  <slot />
</div>
