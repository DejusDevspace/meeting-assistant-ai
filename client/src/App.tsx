import { useState } from "react";
import Header from "./layout/Header";

function App() {
  const [activeTab, setActiveTab] = useState("dashboard");

  return (
    <div className="min-h-screen">
      <Header activeTab={activeTab} setActiveTab={setActiveTab} />
    </div>
  );
}

export default App;
