import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [edgesText, setEdgesText] = useState("a b\nb c\nc a");

  const checkBackend = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/");
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      setMessage("Could not connect to backend");
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial, sans-serif", maxWidth: "700px" }}>
      <h1>Planarity Checker</h1>
      <p>Frontend is running.</p>

      <button onClick={checkBackend} style={{ marginBottom: "20px" }}>
        Check Backend
      </button>

      {message && <p>{message}</p>}

      <hr style={{ margin: "30px 0" }} />

      <h2>Enter Graph Edges</h2>
      <p>Enter one edge per line, like: <code>a b</code></p>

      <textarea
        value={edgesText}
        onChange={(e) => setEdgesText(e.target.value)}
        rows={10}
        style={{
          width: "100%",
          padding: "10px",
          fontFamily: "monospace",
          fontSize: "16px",
        }}
      />

      <h3 style={{ marginTop: "20px" }}>Current Input</h3>
      <pre
        style={{
          background: "#f4f4f4",
          padding: "15px",
          borderRadius: "8px",
          overflowX: "auto",
        }}
      >
        {edgesText}
      </pre>
    </div>
  );
}

export default App;