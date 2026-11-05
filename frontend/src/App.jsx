import React, { useState } from "react";
import "./App.css";

const API = "https://automatic-space-cod-qpx9wggx4jv2476w-8000.app.github.dev/";

export default function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const inspect = async () => {
    if (!file) return alert("Please upload a product image");

    setLoading(true);
    setResult(null);

    const data = new FormData();
    data.append("file", file);

    try {
      const response = await fetch(`${API}/inspect`, {
        method: "POST",
        body: data
      });

      const output = await response.json();

      if (!response.ok) throw new Error(output.detail || "Inspection failed");

      setResult(output);
    } catch (error) {
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">
      <header>
        <h1>AI Quality Inspection</h1>
        <p>Intelligent Packaging Defect Detection System</p>
      </header>

      <section className="upload">
        <h2>Product Inspection</h2>

        <input
          type="file"
          accept="image/jpeg,image/png,image/webp"
          onChange={e => setFile(e.target.files[0])}
        />

        {file && (
          <img
            className="preview"
            src={URL.createObjectURL(file)}
            alt="Uploaded product"
          />
        )}

        <button onClick={inspect} disabled={loading}>
          {loading ? "Inspecting..." : "Start Inspection"}
        </button>
      </section>

      {result && (
        <section className="results">
          <h2>Inspection Results</h2>

          <h3 className={
            result.total_detections ? "fail" : "pass"
          }>
            {result.status}
          </h3>

          <p>Total detections: {result.total_detections}</p>

          <img
            className="preview"
            src={`${API}${result.annotated_image}`}
            alt="Detection results"
          />

          <h3>Detected Defects</h3>

          {result.detections.map((item, index) => (
            <div className="defect" key={index}>
              <strong>{item.class}</strong>
              <span>
                Confidence: {(item.confidence * 100).toFixed(2)}%
              </span>
              <span>
                Bounding Box: {item.bbox.join(", ")}
              </span>
            </div>
          ))}

          <h3>AI Inspection Report</h3>
          <p>{result.ai_report}</p>
        </section>
      )}
    </div>
  );
}