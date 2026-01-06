import { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./ChatWidget.css";

export default function ChatWidget() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [loading, setLoading] = useState(false);

  // Settings
  const [showSettings, setShowSettings] = useState(false);
  const [model, setModel] = useState("gpt-4o-mini");
  const [systemPrompt, setSystemPrompt] = useState("");
  const messagesEndRef = useRef(null);

  // Auto scroll
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const sendMessage = async () => {
    if (!input.trim() || !name.trim() || !phone.trim() || loading) return;

    const userMessage = input;
    setInput("");
    setLoading(true);

    setMessages(prev => [...prev, { from: "user", text: userMessage }]);

    try {
      const res = await axios.post("http://localhost:8000/chat", {
        name,
        phone,
        model,
        system_prompt: systemPrompt || null,
        messages: [
          {
            role: "user",
            content: userMessage,
          },
        ],
      });

      setMessages(prev => [
        ...prev,
        { from: "bot", text: res.data.reply },
      ]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { from: "bot", text: "❌ שגיאה בעיבוד הבקשה" },
      ]);
    } finally {
      setLoading(false);
    }
  };

 return (
  <div className="front-wrapper">
    <div className="front-card">

    {/* Header */}
<div className="front-header">
  <div className="front-header-inner">

    <span className="tier-badge">Support Tier 1</span>
    <h3>שירות לקוחות</h3>

    <button
      className="settings-btn"
      onClick={() => setShowSettings(prev => !prev)}
      aria-label="Settings"
    >
      ⚙️
    </button>

  </div>
</div>

    {showSettings && (
  <div className="front-settings">
    <label>
      מודל:
      <select value={model} onChange={e => setModel(e.target.value)}>
        <option value="gpt-4o-mini">gpt-4o-mini</option>
        <option value="gpt-4.1">gpt-4.1</option>
        <option value="gpt-3.5-turbo">gpt-3.5-turbo</option>
      </select>
    </label>

    <label>
      System Prompt:
      <textarea
        rows={6}
        placeholder="הגדרת התנהגות הסוכן…"
        value={systemPrompt}
        onChange={e => setSystemPrompt(e.target.value)}
      />
    </label>
  </div>
)}


      {/* Meta */}
      <div className="front-meta">
        <div>
          <strong>שם:</strong> {name || "—"}
        </div>
        <div>
          <strong>טלפון:</strong> {phone || "—"}
        </div>
      </div>

      {/* Messages */}
      <div className="front-messages">
        {messages.map((m, i) => (
          <div
            key={i}
            className={`front-message ${m.from}`}
          >
            <div className="message-author">
              {m.from === "user" ? name || "לקוח" : "נציג AI"}
            </div>
            <div className="message-text">{m.text}</div>
          </div>
        ))}

        {loading && (
          <div className="front-message bot typing">
            הבוט מקליד…
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Inputs */}
      <div className="front-inputs">
        <input
          placeholder="שם"
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <input
          placeholder="טלפון"
          value={phone}
          onChange={e => setPhone(e.target.value)}
        />
        <input
          placeholder="כתוב הודעה…"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && sendMessage()}
        />
      </div>

    </div>
  </div>
);

}