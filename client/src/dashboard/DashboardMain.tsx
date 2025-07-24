import React, { useState } from "react";
import { Mic, Play, Clock, Calendar, FileText } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardTitle,
  CardHeader,
  CardDescription,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import type { Meeting } from "@/types/meeting";

type DashboardMainProps = {
  setActiveTab: React.Dispatch<React.SetStateAction<string>>;
};

// Mock data for recent meetings
const recentMeetings: Meeting[] = [
  {
    id: 1,
    title: "Product Strategy Meeting",
    date: "2024-01-15",
    duration: "45:32",
    status: "completed",
    summary:
      "Discussed Q1 roadmap, feature prioritization, and resource allocation...",
  },
  {
    id: 2,
    title: "Client Onboarding Call",
    date: "2024-01-14",
    duration: "32:18",
    status: "completed",
    summary:
      "Walked through platform features, discussed implementation timeline...",
  },
  {
    id: 3,
    title: "Team Standup",
    date: "2024-01-14",
    duration: "15:45",
    status: "pending",
    summary:
      "Sprint progress updates, blocker discussions, and task assignments...",
  },
];

const DashboardMain = ({ setActiveTab }: DashboardMainProps) => {
  const [recentStats] = useState({
    totalMeetings: 20,
    hoursRecorded: "120",
    meetingsThisWeek: 5,
  });

  return (
    <div className="space-y-6">
      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card className="border-2 border-dashed border-gray-200 hover:border-blue-300 transition-colors">
          <CardContent className="flex flex-col items-center justify-center p-8 text-center">
            <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-4">
              <Mic className="w-8 h-8 text-blue-600" />
            </div>
            <h3 className="text-lg font-semibold mb-2">Start New Recording</h3>
            <p className="text-gray-600 mb-4">
              Record a new meeting or audio session
            </p>
            <Button onClick={() => setActiveTab("record")} className="w-full">
              <Mic className="w-4 h-4 mr-2" />
              Start Recording
            </Button>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold">Recent Activity</h3>
              <Badge variant="secondary">3 new</Badge>
            </div>
            <div className="space-y-3">
              <div className="flex items-center space-x-3">
                <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                <span className="text-sm">Product meeting transcribed</span>
              </div>
              <div className="flex items-center space-x-3">
                <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                <span className="text-sm">Summary generated</span>
              </div>
              <div className="flex items-center space-x-3">
                <div className="w-2 h-2 bg-yellow-500 rounded-full"></div>
                <span className="text-sm">Action items extracted</span>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Quick stats */}
        <Card>
          <CardContent className="p-6">
            <h3 className="text-lg font-semibold mb-4">Quick Stats</h3>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span className="text-gray-600">Total Meetings</span>
                <span className="font-semibold">
                  {recentStats.totalMeetings}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Hours Recorded</span>
                <span className="font-semibold">
                  {recentStats.hoursRecorded}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">This Week</span>
                <span className="font-semibold">
                  {recentStats.meetingsThisWeek}
                </span>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Recent Meetings */}
      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <div>
              <CardTitle>Recent Meetings</CardTitle>
              <CardDescription>
                Your latest recorded sessions and transcripts
              </CardDescription>
            </div>
            <Button variant="outline" onClick={() => setActiveTab("meetings")}>
              View All
            </Button>
          </div>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {recentMeetings.map((meeting) => (
              <div
                key={meeting.id}
                className="flex items-center justify-between p-4 border rounded-lg hover:bg-gray-50 transition-colors"
              >
                <div className="flex items-center space-x-4">
                  <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                    <FileText className="w-5 h-5 text-blue-600" />
                  </div>
                  <div>
                    <h4 className="font-medium">{meeting.title}</h4>
                    <div className="flex items-center space-x-4 text-sm text-gray-600">
                      <span className="flex items-center">
                        <Calendar className="w-4 h-4 mr-1" />
                        {meeting.date}
                      </span>
                      <span className="flex items-center">
                        <Clock className="w-4 h-4 mr-1" />
                        {meeting.duration}
                      </span>
                    </div>
                  </div>
                </div>
                <div className="flex items-center space-x-2">
                  <Badge
                    variant="outline"
                    className={`${
                      meeting.status === "completed"
                        ? "bg-green-100 text-green-700"
                        : meeting.status === "pending"
                        ? "bg-yellow-100 text-yellow-700"
                        : "bg-red-100 text-red-700"
                    } `}
                  >
                    {meeting.status}
                  </Badge>
                  <Button variant="ghost" size="sm">
                    <Play className="w-4 h-4" />
                  </Button>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default DashboardMain;
