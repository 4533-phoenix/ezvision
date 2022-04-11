<script lang="ts">
  import { afterUpdate } from "svelte";
  import Header from "../lib/Header.svelte";

  let resources = {};
  let socket = globalThis.socket;
  let reboot = () => {
    socket.emit("command", "sudo reboot now");
  };
  let run = () => {
    socket.emit("command", window.prompt("Command"));
  };
  let requestResources = () => {
    if (!document.hidden) {
      socket.emit("resources");
    }
  };

  socket.on("resources", (data: JSON) => {
    resources = data;
  });

  afterUpdate(() => {
    globalThis.addPageListeners();
  });

  setInterval(requestResources, 1000);
</script>

<Header title="System" subtitle="Control/View the System" />

<h3>Stats</h3>
<table class="table">
  <tbody>
    {#each Object.entries(resources) as [name, value]}
      <tr>
        <td>{name}</td>
        <td>{value}</td>
      </tr>
    {/each}
  </tbody>
</table>

<button type="button" class="btn btn-danger" on:click={reboot}>Reboot</button>
<button type="button" class="btn btn-danger" on:click={run}>Run</button>
