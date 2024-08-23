import React, { useState } from 'react';
import './App.css';
function App() {

  const [assistantResponse, setAssistantResponse] = useState("");

  const activateVoiceAssistant = async () => {
    try {
      const response = await fetch("http://localhost:5000/activate", {
        method: "POST"
      });
      const data = await response.json();
      setAssistantResponse(data.response || data.error);
    } catch (error) {
      setAssistantResponse("Error activating assistant: " + error);
    }
  };

  const handleTextToSpeech = async (text) => {
    try {
      const response = await fetch("http://localhost:5000/synthesize", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
      });
      const audioBlob = await response.blob();
      const audioUrl = URL.createObjectURL(audioBlob);
      const audio = new Audio(audioUrl);
      audio.play();
    } catch (error) {
      console.error("Error with text-to-speech:", error);
    }
  };




  
  return (
    <div className="App">
    <h1>Voice Assistant</h1>
    <button onClick={activateVoiceAssistant}>Activate Assistant</button>
    <button onClick={() => handleTextToSpeech("Hello, welcome to the AWS Polly demo!")}>Speak</button>
    <p>{assistantResponse}</p>
  </div>

  );

}

export default App;
