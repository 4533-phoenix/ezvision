<script lang="ts">
  import { afterUpdate } from "svelte";

  let socket = globalThis.socket;

  afterUpdate(() => {
    globalThis.addPageListeners();
  });
</script>
