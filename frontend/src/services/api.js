import axios from "axios";

export const api = axios.create({
  baseURL: "https://anti-runner-nil-gmbh.trycloudflare.com/api",
});
