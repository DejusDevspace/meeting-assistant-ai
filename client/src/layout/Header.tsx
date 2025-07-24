import React from "react";
import { Mic, Settings, User } from "lucide-react";
import { Button } from "@/components/ui/button";

type HeaderProps = {
  activeTab: string;
  setActiveTab: React.Dispatch<React.SetStateAction<string>>;
};

const Header = ({ activeTab, setActiveTab }: HeaderProps) => {
  return (
    <header className="bg-white border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                <Mic className="w-5 h-5 text-white" />
              </div>
              <h1 className="text-xl font-bold text-gray-900">Scriptly</h1>
            </div>
          </div>

          <nav className="hidden md:flex space-x-8">
            <button
              onClick={() => setActiveTab("dashboard")}
              className={`px-3 py-2 text-sm font-medium rounded-md transition-colors ${
                activeTab === "dashboard"
                  ? "bg-blue-100 text-blue-700"
                  : "text-gray-600 hover:text-gray-900"
              } cursor-pointer`}
            >
              Dashboard
            </button>
            <button
              onClick={() => setActiveTab("record")}
              className={`px-3 py-2 text-sm font-medium rounded-md transition-colors ${
                activeTab === "record"
                  ? "bg-blue-100 text-blue-700"
                  : "text-gray-600 hover:text-gray-900"
              } cursor-pointer`}
            >
              Record
            </button>
            <button
              onClick={() => setActiveTab("meetings")}
              className={`px-3 py-2 text-sm font-medium rounded-md transition-colors ${
                activeTab === "meetings"
                  ? "bg-blue-100 text-blue-700"
                  : "text-gray-600 hover:text-gray-900"
              } cursor-pointer`}
            >
              Meetings
            </button>
          </nav>

          <div className="flex items-center space-x-4">
            <Button variant="ghost" size="sm">
              <Settings className="w-4 h-4" />
            </Button>
            <Button variant="ghost" size="sm">
              <User className="w-4 h-4" />
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
