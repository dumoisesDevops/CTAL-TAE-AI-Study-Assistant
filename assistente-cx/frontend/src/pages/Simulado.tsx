import { useState } from "react";
import { api } from "../api";

export default function Simulado() {
  const [topic, setTopic] = useState("");
  const [questions, setQuestions] = useState("");

  const generate = async () => {
    const res = await api.post("/simulado/create", { topic });
    setQuestions(res.data.questoes);
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Gerar Simulado</h1>
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Informe o tópico (ex: Test Automation)"
        className="border p-2 w-96 rounded"
      />
      <button onClick={generate} className="ml-3 px-4 py-2 bg-blue-600 text-white rounded">
        Gerar
      </button>

      <pre className="mt-6 bg-gray-100 p-4 rounded whitespace-pre-wrap">
        {questions}
      </pre>
    </div>
  );
}
