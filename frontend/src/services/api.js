import axios from "axios";

export const api = axios.create({
  baseURL: "https://leavenless-natasha-isocheimenal.ngrok-free.dev/api",
});