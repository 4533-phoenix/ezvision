<script lang="ts">
  // Use global this to change page from within page

  import Error from "./pages/Error.svelte";
  import Blank from "./pages/Blank.svelte";
  import Home from "./pages/Home.svelte";
  import System from "./pages/System.svelte";
  import Settings from "./pages/Settings.svelte";
  import Vision from "./pages/Vision.svelte";
  import About from "./pages/About.svelte";

  import logo_name from "./assets/logo_name.png";

  import io from "socket.io-client";
  globalThis.socket = io();

  const pages = {
    "home": Home,
    "system": System,
    "settings": Settings,
    "vision": Vision,
    "about": About,
  };
  let page = window.location.hash.replace("#", "");
  let view = Blank;
  let addPageListeners = () => {
    document.querySelectorAll("a").forEach((element) => {
      element.addEventListener("click", (event) => {
        if ("href" in event.target) {
          const target = event.target as HTMLAnchorElement;
          const href = target.href;
          page = href.substring(href.indexOf("#") + 1);
          changePage();
        }
      });
    });
  };
  let changePage = () => {
    if (page in pages) {view = pages[page]}
    else {view = Error}
  }
  page = page || "home";

  let onPageLoad = () => {
    addPageListeners();
    changePage();
  }
</script>

<svelte:window on:load={onPageLoad} />

<svelte:head>
  <link rel="stylesheet" href="/css/side_menu.css" />
</svelte:head>

<main>
  <div id="layout">
    <a href="#menu" id="menuLink" class="menu-link">
      <span />
    </a>

    <div id="menu">
      <div class="pure-menu">
        <a class="pure-menu-heading" href="#company">
          <img width="100%" height="50%" src={logo_name} alt="Logo" />
        </a>

        <ul class="pure-menu-list">
          <li class="pure-menu-item">
            <a href="#home" class="pure-menu-link">Home</a>
          </li>
          <li class="pure-menu-item">
            <a href="#system" class="pure-menu-link">System</a>
          </li>
          <li class="pure-menu-item">
            <a href="#settings" class="pure-menu-link">Settings</a>
          </li>
          <li class="pure-menu-item">
            <a href="#vision" class="pure-menu-link">Vision</a>
          </li>
          <li class="pure-menu-item">
            <a href="#about" class="pure-menu-link">About</a>
          </li>
        </ul>
      </div>
    </div>
    <div id="main">
      <svelte:component this={view} />
    </div>
  </div>
</main>

<style>
  #main {
    margin: 10px;
  }
</style>