<script lang="ts">
  import Fa from "svelte-fa";
  import manifest from "./pages/manifest";
  import io from "socket.io-client";
  import { onMount, afterUpdate } from "svelte";
  import logo_name from "./assets/logo_name.png";

  globalThis.page = window.location.hash.replace("#", "") || "home";
  globalThis.socket = io("localhost:8080");
  globalThis.addPageListeners = () => {
    let page = globalThis.page;

    document.querySelectorAll("a").forEach((element) => {
      if (
        element.classList.contains("spa-added") ||
        !element.href.includes("#")
      ) {
        return;
      }

      element.classList.add("spa-added");
      element.addEventListener("click", (event) => {
        if ("href" in event.target) {
          const target = event.target as HTMLAnchorElement;
          const href = target.href;

          globalThis.page = href.substring(href.indexOf("#") + 1);
          globalThis.changePage();
        }
      });
    });
  };
  globalThis.changePage = () => {
    if (globalThis.page in manifest) {
      view = manifest[globalThis.page].view;
    } else {
      view = manifest.error.view;
    }
  };

  let view = manifest.blank.view;

  afterUpdate(() => {
    globalThis.addPageListeners();
  });

  onMount(() => {
    globalThis.addPageListeners();
    globalThis.changePage();
  });
</script>

<svelte:head>
  <link rel="stylesheet" href="/css/sidebar.css" />
</svelte:head>

<main>
  <div
    class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark"
    style="width: 280px;"
  >
    <a
      href="/"
      class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none"
    >
      <img width="100%" src={logo_name} alt="Logo" id="logo" />
    </a>
    <hr />
    <ul class="nav nav-pills flex-column mb-auto">
      {#each Object.entries(manifest).filter((item) => {
        return item[1].menu;
      }) as [page, data]}
        <li class="nav-item">
          <a
            href="#{page}"
            class="nav-link {data.active ? 'active' : 'text-white'}"
            aria-current="page"
          >
            <Fa icon={data.icon} />
            {data.name}
          </a>
        </li>
      {/each}
    </ul>
  </div>
  <div id="content">
    <svelte:component this={view} />
  </div>
</main>

<style>
  #logo {
    image-rendering: pixelated;
  }

  #content {
    margin: 10px;
    width: 100%;
  }
</style>
