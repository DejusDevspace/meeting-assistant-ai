import React, { useState } from "react";
import {
  Card,
  CardHeader,
  CardDescription,
  CardTitle,
  CardContent,
} from "@/components/ui/card";
import { Mic, Square } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

const RecordingMain = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);

  const startRecording = () => {
    setIsRecording(true);
    // Start timer simulation
    const timer = setInterval(() => {
      setRecordingTime((prev) => prev + 1);
    }, 1000);
  };

  const stopRecording = () => {
    setIsRecording(false);
    setRecordingTime(0);
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, "0")}:${secs
      .toString()
      .padStart(2, "0")}`;
  };

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <Card>
        <CardHeader className="text-center">
          <CardTitle className="text-2xl">Record New Meeting</CardTitle>
          <CardDescription>
            Start recording your meeting or audio session
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Recording Controls */}
          <div className="text-center space-y-4">
            <div
              className="w-32 h-32 mx-auto bg-gradient-to-br from-blue-500 to-purple-600 rounded-full cursor-pointer flex items-center justify-center relative"
              onClick={isRecording ? stopRecording : startRecording}
            >
              {isRecording && (
                <div className="absolute inset-0 rounded-full border-4 border-white animate-pulse"></div>
              )}
              <Button
                size="lg"
                variant={isRecording ? "destructive" : "default"}
                className="w-20 h-20 rounded-full cursor-pointer"
              >
                {isRecording ? (
                  <Square className="w-8 h-8" />
                ) : (
                  <Mic className="w-8 h-8" />
                )}
              </Button>
            </div>

            {isRecording && (
              <div className="space-y-2">
                <div className="text-2xl font-mono font-bold text-red-600">
                  {formatTime(recordingTime)}
                </div>
                <div className="flex justify-center">
                  <div className="flex space-x-1">
                    {[...Array(20)].map((_, i) => (
                      <div
                        key={i}
                        className="w-1 bg-red-500 rounded-full animate-pulse"
                        style={{
                          height: `${Math.random() * 20 + 10}px`,
                          animationDelay: `${i * 0.1}s`,
                        }}
                      ></div>
                    ))}
                  </div>
                </div>
                <p className="text-sm text-gray-600">
                  Recording in progress...
                </p>
              </div>
            )}
          </div>

          {/* Meeting Details */}
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2">
                Meeting Title
              </label>
              <Input placeholder="Enter meeting title..." />
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">
                Participants
              </label>
              <Input placeholder="Add participant names..." />
            </div>
          </div>

          {/* Action Buttons */}
          {!isRecording && (
            <div className="flex space-x-3">
              <Button className="flex-1" onClick={startRecording}>
                <Mic className="w-4 h-4 mr-2" />
                Start Recording
              </Button>
              <Button variant="outline" className="flex-1 bg-transparent">
                Upload Audio File
              </Button>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default RecordingMain;
