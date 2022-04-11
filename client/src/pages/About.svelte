<script lang="ts">
  import { afterUpdate } from "svelte";
  import Header from "../lib/Header.svelte";
  import * as info from "../about";

  let socket = globalThis.socket;

  function decamelize(str: String, separator: String) {
    separator = typeof separator === "undefined" ? "_" : separator;

    return str
      .replace(/([a-z\d])([A-Z])/g, "$1" + separator + "$2")
      .replace(/([A-Z]+)([A-Z][a-z\d]+)/g, "$1" + separator + "$2")
      .toLowerCase();
  }

  function toTitleCase(str: string) {
    return str.replace(/\w\S*/g, function (txt) {
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
  }

  afterUpdate(() => {
    globalThis.addPageListeners();
  });
</script>

<Header title="About" subtitle="About EZ Vision" />

<h3>Info</h3>
<table class="table">
  <tbody>
    {#each Object.entries(info) as [name, value]}
      <tr>
        <td>{toTitleCase(decamelize(name, " "))}</td>
        <td>{value}</td>
      </tr>
    {/each}
  </tbody>
</table>
