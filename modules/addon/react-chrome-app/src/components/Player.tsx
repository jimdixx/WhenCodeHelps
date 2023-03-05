import { MutableRefObject, useRef } from "react";

export const Player = (props: { url: string; timestamps: number[] }) => {
  const { url, timestamps } = props;
  const audio =
    useRef<HTMLAudioElement>() as MutableRefObject<HTMLAudioElement>;

  const previousWord = () => {
    const previousStamps: number[] = [];
    // console.log({ audio, timestamps });
    const currentTime = audio.current.currentTime;
    for (let i = 0; i < timestamps.length; i++) {
      if (timestamps[i] < currentTime) {
        previousStamps.push(timestamps[i]);
      }
    }

    const rewindWord = previousStamps.pop();
    // console.log({ rewindWord });

    if (!!rewindWord) audio.current.currentTime = rewindWord;
  };

  return (
    <div className="rounded-lg shadow-lg shadow-black p-4 flex justify-center text-center prose">
      <audio controls ref={audio} autoPlay>
        <source src={url} type="audio/mpeg"></source>
        Your browser does not support the <code>audio</code> element.
      </audio>
      <button className="btn btn-primary ml-2" onClick={previousWord}>
        Previous word
      </button>
    </div>
  );
};
