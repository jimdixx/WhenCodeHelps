import { useCallback, useEffect, useState } from "react";
import { Player } from "./Player";
import { Recording } from "../types";
import { getAudioTimestamps } from "../api/client";

export const RecordsList = () => {
  const [recordings, setRecordings] = useState<Recording[]>([]);
  useEffect(() => {
    fetchAudioTimestamps();
  }, []);

  const fetchAudioTimestamps = useCallback(async () => {
    return await getAudioTimestamps().then((stamps) =>
      setRecordings([
        {
          url: "https://storage.googleapis.com/media-session/elephants-dream/the-wires.mp3",
          timestamps: stamps,
        },
      ])
    );
  }, []);

  return (
    <div>
      {recordings.map((rec, i) => (
        <Player url={rec.url} timestamps={rec.timestamps} key={i} />
      ))}
    </div>
  );
};
