import Error from "./Error.svelte";
import Blank from "./Blank.svelte";
import Home from "./Home.svelte";
import System from "./System.svelte";
import Settings from "./Settings.svelte";
import Vision from "./Vision.svelte";
import About from "./About.svelte";

export default {
  home: {
    view: Home,
    menu: true,
    active: true,
    name: "Home",
    icon: "house"
  },
  system: {
    view: System,
    menu: true,
    active: false,
    name: "System",
    icon: "laptop"
  },
  settings: {
    view: Settings,
    menu: true,
    active: false,
    name: "Settings",
    icon: "gear"
  },
  vision: {
    view: Vision,
    menu: true,
    active: false,
    name: "Vision",
    icon: "camera"
  },
  about: {
    view: About,
    menu: true,
    active: false,
    name: "About",
    icon: "circle-info"
  },
  error: {
    view: Error,
    menu: false,
    active: false,
    name: "Error",
    icon: ""
  },
  blank: {
    view: Blank,
    menu: false,
    active: false,
    name: "Blank",
    icon: ""
  }
};