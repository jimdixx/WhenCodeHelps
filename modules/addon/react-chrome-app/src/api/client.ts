export const API_URL = "http://localhost:8000";

export const getAudioTimestamps = async () => {
  const response = await fetch(`${API_URL}/audio`).then((res) => res.json());
  console.log({ response });

  const timestamps: number[] = [];
  const responseObj = response.map((res: any) => JSON.parse(res));
  for (let i = 0; i < response.length; i++) {
    i === 0
      ? timestamps.push(responseObj[i].time)
      : timestamps.push(responseObj[i].time + timestamps[i - 1]);
  }
  console.log({ timestamps });

  return timestamps;
};

export const pushText = async (text: string) => {
  const response = await fetch(`${API_URL}/uploadText`, {
    method: 'POST',
    body: JSON.stringify({ text }),
    headers: {
      "Accept": "*/*"

    }
  }).then((res) => res.json());
  console.log({ response });
}

export const getRecord = async () => {
  const response = await fetch(`${API_URL}/static/beta.mp3`).then((res) => {
      console.log('RRRRR', res)
      return res.json()
    }
  );
  return response;
};

export const getUser = async (username: string) => {
  const response = await fetch(`${API_URL}/user/${username}`).then((res) =>
    res.json()
  );
  return response;
};

export const loginUser = async (body: any) => {
  return await fetch(`${API_URL}/user`, { method: "POST", body });
};
