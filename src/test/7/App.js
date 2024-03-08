import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import './App.css';

const App = () => {
  const [image, setImage] = useState(null);
  const [params, setParams] = useState({
    prompt: 'Test Prompt Socket',
    style: 'Test Style Socket',
    negative_prompt: 'Test Negative Prompt Socket',
    output_type: 'Test Output Type Socket',
    num_inference_steps: 12,
    guidance_scale: 0.6,
    lcm_origin_steps: 6,
    width: 600,
    height: 400,
  });
  const [processingTime, setProcessingTime] = useState(null);
  const [startTime, setStartTime] = useState(null);
  const [buttonClickedTime, setButtonClickedTime] = useState(null);

  const socket = io('http://localhost:5000');

  socket.on('yeni_socket_event_response', (data) => {
    console.log('Received image from server:', data.image);
    setImage(data.image);

    // Resim alındığında işlem süresini hesapla
    if (buttonClickedTime !== null) {
      setProcessingTime(performance.now() - buttonClickedTime);
    }
  });

  const handleInputChange = (e) => {
    const { name, value, type } = e.target;
    const parsedValue = type === 'number' && value !== '' ? parseFloat(value) : value;
    setParams({ ...params, [name]: parsedValue });
  };

  const sendParamsToServer = () => {
    setStartTime(performance.now());
    setButtonClickedTime(performance.now());

    // Stil değişikliği için rastgele bir değer ekleyebilirsiniz.
    params.style = Date.now();

    socket.emit('yeni_socket_event', params);
  };

  useEffect(() => {
    // Resim alındığında işlem süresini hesapla
    if (startTime !== null && image !== null) {
      setProcessingTime(performance.now() - startTime);
    }
  }, [startTime, image]);

  return (
    <div className="app-container">
      <div className="left-section">
        <h1>Parameters</h1>
        <form className="params-form">
          {Object.entries(params).map(([paramName, paramValue]) => (
            <div key={paramName} className="form-group">
              <label className="param-label">
                {paramName.charAt(0).toUpperCase() + paramName.slice(1)}:
                <input
                  className="param-input"
                  type={typeof paramValue === 'number' ? 'number' : 'text'}
                  name={paramName}
                  value={paramValue}
                  onChange={handleInputChange}
                />
              </label>
            </div>
          ))}
          <button className="send-button" type="button" onClick={sendParamsToServer}>
            Generate Image
          </button>
        </form>
        {processingTime !== null && (
          <p className="processing-time">Processing Time: {processingTime.toFixed(2)} milliseconds</p>
        )}
      </div>
      <div className="right-section">
        <h1>Generated Image</h1>
        {image && <img className="generated-image" src={`data:image/png;base64, ${image}`} alt="Generated" />}
      </div>
    </div>
  );
};

export default App;
