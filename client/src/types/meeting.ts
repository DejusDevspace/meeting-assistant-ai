export interface Meeting {
  readonly id: number;
  title: string;
  date: string;
  duration: string;
  status: "completed" | "pending" | "failed";
  summary: string;
}
