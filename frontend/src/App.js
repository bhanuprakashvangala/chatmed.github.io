import React, { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = async () => {
    const res = await fetch("http://localhost:5000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>ChatMed: Medical Chatbot</h2>
      <textarea
        rows="4"
        cols="50"
        placeholder="Describe your symptoms..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <br />
      <button onClick={handleSend}>Send</button>
      <h3>Bot Response:</h3>
      <p>{response}</p>
    </div>
  );
}

export default App;
