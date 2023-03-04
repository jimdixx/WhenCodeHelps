export const API_URL = 'http://localhost:8000'

export const getAudioTimestamps = async () => {
    const response = await fetch(`${API_URL}/audio`).then(res => res.json());
    const timestamps: number[] = [];
    for (let i = 0; i < response.length; i++) {
        i === 0 ? timestamps.push(response[i].timestamp) : timestamps.push(response[i] + response[i-1]);
    }
    console.log({timestamps});
    
    return timestamps;
}