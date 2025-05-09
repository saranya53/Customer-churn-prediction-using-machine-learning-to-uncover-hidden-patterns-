import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { BarChart2, UploadCloud } from "lucide-react";

export default function App() {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    if (!file) return alert("Please upload a CSV file.");
    // Simulate prediction
    setPrediction({
      churnRate: "24%",
      atRiskCustomers: 120,
      insights: ["High monthly charges", "Short tenure", "No contract"]
    });
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-3xl font-bold text-center mb-8">
        Customer Churn Prediction Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card className="p-4">
          <CardContent>
            <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
              <UploadCloud size={20} /> Upload Customer Data
            </h2>
            <Input type="file" accept=".csv" onChange={handleFileChange} />
            <Button className="mt-4 w-full" onClick={handleUpload}>
              Predict Churn
            </Button>
          </CardContent>
        </Card>

        <Card className="p-4">
          <CardContent>
            <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
              <BarChart2 size={20} /> Prediction Results
            </h2>
            {prediction ? (
              <div className="space-y-2">
                <p><strong>Churn Rate:</strong> {prediction.churnRate}</p>
                <p><strong>At-risk Customers:</strong> {prediction.atRiskCustomers}</p>
                <div>
                  <strong>Top Risk Factors:</strong>
                  <ul className="list-disc list-inside">
                    {prediction.insights.map((item, i) => (
                      <li key={i}>{item}</li>
                    ))}
                  </ul>
                </div>
              </div>
            ) : (
              <p>No predictions yet.</p>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
