<script>
  import { page } from '$app/stores';
  let errorMessage = '';
  if ($page.error !== null) {
    errorMessage = $page.error.message;
  }
</script>

<h1 class="text-5xl text-center">{$page.status} : {errorMessage}</h1>

<p>Oopsie woopsie</p>
