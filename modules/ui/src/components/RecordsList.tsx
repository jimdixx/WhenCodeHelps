import { useEffect, useState } from "react";
import { Player } from "./Player";
import { Recording } from "../types";

export const RecordsList = () => {
  const [recordings, setRecordings] = useState<Recording[]>([]);
  useEffect(() => {
    const records: Recording[] = [
      {
        url: "https://storage.googleapis.com/media-session/elephants-dream/the-wires.mp3",
        timestamps: [1.2, 2.43, 3.55, 4.9, 6.12, 8.24],
      },
    ];
    setRecordings(records);
  }, []);

  return (
    <div>
      {recordings.map((rec, i) => (
        <Player url={rec.url} timestamps={rec.timestamps} key={i} />
      ))}
    </div>
  );
};
