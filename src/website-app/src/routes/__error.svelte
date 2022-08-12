<script context="module">
  /** @type {import('@sveltejs/kit').Load} */
  export function load({ error, status }) {
    if (error == null) {
      throw new Error(`No error found`);
    }
    return {
      props: {
        title: `${status}: ${error.message}`
      }
    };
  }
</script>

<script>
  /**
   * @type {string | string[]}
   */
  export let title;
</script>

<h1 class="text-5xl text-center">{title}</h1>

<p>Oopsie woopsie</p>
