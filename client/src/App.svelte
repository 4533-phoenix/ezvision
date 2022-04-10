<script lang="ts">
  // Use global this to change page from within page

  import {HouseFill, LaptopFill, GearFill, CameraFill, InfoCircleFill} from "svelte-bootstrap-icons";

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
    home: Home,
    system: System,
    settings: Settings,
    vision: Vision,
    about: About,
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
    if (page in pages) {
      view = pages[page];
    } else {
      view = Error;
    }
  };
  page = page || "home";

  let onPageLoad = () => {
    addPageListeners();
    changePage();
  };
</script>

<svelte:window on:load={onPageLoad} />

<svelte:head>
  <link rel="stylesheet" href="/css/sidebar.css" />
</svelte:head>

<main>
  <div class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark" style="width: 280px;">
    <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
      <img width="100%" src={logo_name} alt="Logo" />
    </a>
    <hr>
    <ul class="nav nav-pills flex-column mb-auto">
      <li class="nav-item">
        <a href="#home" class="nav-link active" aria-current="page">
          <HouseFill />
          Home
        </a>
      </li>
      <li>
        <a href="#system" class="nav-link text-white">
          <LaptopFill />
          System
        </a>
      </li>
      <li>
        <a href="#settings" class="nav-link text-white">
          <GearFill />
          Settings
        </a>
      </li>
      <li>
        <a href="#vision" class="nav-link text-white">
          <CameraFill />
          Vision
        </a>
      </li>
      <li>
        <a href="#about" class="nav-link text-white">
          <InfoCircleFill />
          About
        </a>
      </li>
    </ul>
  </div>
  <div id="content">
    <svelte:component this={view} />
  </div>
</main>

<style>
  #content {
    margin: 10px;
  }
</style>
