<script lang="ts">
  import { afterUpdate } from "svelte";
  import Header from "../lib/Header.svelte";
  import logo from "../assets/logo.png";

  let socket = globalThis.socket;

  afterUpdate(() => {
    globalThis.addPageListeners();
  });
</script>

<Header title="Home" subtitle="EZ Vision Home Page" />

<h3>Welcome to EZ Vision!</h3>
<p>Thank you for using EZ Vision! To get started, add a camera via the <a href="#vision">Vision</a> tab. Also, check out the <a href="https://github.com/wando-advanced-robotics/ezvision">GitHub</a> to view the source code and make changes!</p>
<img src={logo} alt="Logo">