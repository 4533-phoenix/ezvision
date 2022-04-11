import {faHouse, faLaptop, faGear, faCamera, faCircleInfo,faX} from '@fortawesome/free-solid-svg-icons';

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
    icon: faHouse
  },
  system: {
    view: System,
    menu: true,
    active: false,
    name: "System",
    icon: faLaptop
  },
  settings: {
    view: Settings,
    menu: true,
    active: false,
    name: "Settings",
    icon: faGear
  },
  vision: {
    view: Vision,
    menu: true,
    active: false,
    name: "Vision",
    icon: faCamera
  },
  about: {
    view: About,
    menu: true,
    active: false,
    name: "About",
    icon: faCircleInfo
  },
  error: {
    view: Error,
    menu: false,
    active: false,
    name: "Error",
    icon: faX
  },
  blank: {
    view: Blank,
    menu: false,
    active: false,
    name: "Blank",
    icon: faX
  }
};