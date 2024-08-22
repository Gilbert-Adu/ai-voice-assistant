import './App.css';
function App() {

  const handleClick = () => {
    console.log('clicked')
  }
  return (
    <div className="App">
      <div className="container">
        <h1>Voice Assistant</h1>
        <div className="display">
            <p id="response-text">Waiting for a command...</p>
        </div>
        <button id="activate-btn" onClick={handleClick}>Activate Voice Assistant</button>
    </div>
    
    </div>
  );
}

export default App;
