<script lang="ts">
  import { afterUpdate } from "svelte";

  afterUpdate(() => {
    globalThis.addPageListeners();
  });
</script>

<h1>Sorry! We could not find the menu you were looking for!</h1>
<p>You can try to go to another tab ;)</p>
<a href="#home">BRUH</a>