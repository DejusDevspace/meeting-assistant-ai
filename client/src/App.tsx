import { useState } from "react";
import Header from "./layout/Header";
import DashboardMain from "./dashboard/DashboardMain";
import Footer from "./layout/Footer";

function App() {
  const [activeTab, setActiveTab] = useState("dashboard");

  return (
    <div className="min-h-screen">
      <Header activeTab={activeTab} setActiveTab={setActiveTab} />

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === "dashboard" && (
          <DashboardMain setActiveTab={setActiveTab} />
        )}
        {activeTab === "record" && "Record Component Placeholder"}
        {activeTab === "meetings" && "Meetings Component Placeholder"}
      </main>

      <Footer />
    </div>
  );
}

export default App;
