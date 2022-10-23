<script>
  import { page } from '$app/stores';
  let errorMessage = '';
  if ($page.error !== null) {
    errorMessage = $page.error.message;
  }
</script>

<h1 class="text-center text-5xl">{$page.status} : {errorMessage}</h1>

<p>Oopsie woopsie</p>
