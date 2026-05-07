import { useEffect, useState } from "react";
import { api } from "./services/api";

import {
  MapPinned,
  Route,
  Brain,
  Navigation
} from "lucide-react";

export default function App() {

  const [cities, setCities] = useState([]);

  const [origin, setOrigin] = useState("");
  const [destination, setDestination] = useState("");

  const [results, setResults] = useState(null);

  useEffect(() => {

    api.get("/cities/")
      .then(res => setCities(res.data))

  }, []);

  const solve = async () => {

    const res = await api.post("/solve/", {
      origen: origin,
      destino: destination
    });

    setResults(res.data);
  };

  return (

    <div className="min-h-screen bg-slate-950 text-white">

      <header className="border-b border-slate-800 p-5">

        <div className="flex items-center gap-3">

          <Navigation size={35} />

          <div>
            <h1 className="text-3xl font-bold">
              SmartRoad AI
            </h1>

            <p className="text-slate-400">
              Comparador de algoritmos de búsqueda
            </p>
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto p-6">

        <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800">

          <div className="grid md:grid-cols-2 gap-5">

            <div>
              <label>Origen</label>

              <select
                className="w-full mt-2 p-3 rounded-xl bg-slate-800"
                value={origin}
                onChange={(e)=>setOrigin(e.target.value)}
              >
                <option>Selecciona origen</option>

                {
                  cities.map(city => (
                    <option key={city}>
                      {city}
                    </option>
                  ))
                }
              </select>
            </div>

            <div>
              <label>Destino</label>

              <select
                className="w-full mt-2 p-3 rounded-xl bg-slate-800"
                value={destination}
                onChange={(e)=>setDestination(e.target.value)}
              >
                <option>Selecciona destino</option>

                {
                  cities.map(city => (
                    <option key={city}>
                      {city}
                    </option>
                  ))
                }
              </select>
            </div>
          </div>

          <button
            onClick={solve}
            className="mt-5 bg-indigo-600 hover:bg-indigo-500 transition px-6 py-3 rounded-xl flex items-center gap-2"
          >
            <Brain />
            Ejecutar algoritmos
          </button>
        </div>

        {
          results && (

            <div className="grid lg:grid-cols-3 gap-5 mt-8">

              {
                Object.entries(results).map(([name, data]) => (

                  <div
                    key={name}
                    className="bg-slate-900 border border-slate-800 rounded-2xl p-5"
                  >

                    <div className="flex items-center gap-2 mb-4">

                      <Route />

                      <h2 className="text-2xl font-bold uppercase">
                        {name}
                      </h2>
                    </div>

                    <div className="space-y-3">

                      <div>
                        <p className="text-slate-400">
                          Ruta encontrada
                        </p>

                        <p className="font-semibold">
                          {data?.ruta?.join(" ➜ ")}
                        </p>
                      </div>

                      <div>
                        <p className="text-slate-400">
                          Nodos visitados
                        </p>

                        <p>
                          {data?.visitados?.join(", ")}
                        </p>
                      </div>

                      {
                        data?.costo && (
                          <div>
                            <p className="text-slate-400">
                              Distancia total
                            </p>

                            <p className="text-emerald-400 font-bold">
                              {data.costo} KM
                            </p>
                          </div>
                        )
                      }

                    </div>

                  </div>

                ))
              }

            </div>
          )
        }

      </main>
    </div>
  );
}