import { useState } from "react";
import axios from "axios";

function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await axios.post("http://127.0.0.1:8000/analyze", { text: input });
    setResponse(res.data.reply);
  };

  return (
    <div className="p-8 text-center">
      <h1 className="text-3xl font-bold mb-4">Assistente CX 🤖</h1>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Digite sua dúvida..."
        className="border p-2 rounded w-80"
      />
      <button
        onClick={sendMessage}
        className="ml-2 bg-blue-500 text-white px-4 py-2 rounded"
      >
        Enviar
      </button>
      <p className="mt-6 text-lg">{response}</p>
    </div>
  );
}

export default App;
