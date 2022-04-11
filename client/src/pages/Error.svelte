<script lang="ts">
  import { afterUpdate } from "svelte";

  afterUpdate(() => {
    globalThis.addPageListeners();
  });
</script>

<h1>Sorry! We could not find the menu you were looking for!</h1>
<a href="#home">Home</a>
