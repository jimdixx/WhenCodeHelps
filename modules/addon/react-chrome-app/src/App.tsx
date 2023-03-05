import {useCallback, useEffect, useState} from 'react'
import './App.css'
import {Player} from "./components/Player";
import {API_URL, getAudioTimestamps, getRecord, pushText} from "./api/client";

const simplifyKey = 'simplify'
function App() {
  const [content, setContent] = useState("")
  const [simplify, setSimplify] = useState<boolean | undefined>(undefined)
  const [timestamps, setTimestamps] = useState<number[] | undefined>(undefined)
  const [cycle, setCycle] = useState(0)
  const record = `${API_URL}/static/beta.mp3`
  useEffect(() => {
    chrome.storage.local.get().then(res => setSimplify(!!res[simplifyKey]))
  }, [])

  useEffect(() => {
    if (simplify!==undefined){
      pushText(content)
      setCycle(1)
    }
  }, [simplify])

  useEffect(() => {
    if(cycle > 0 && ! timestamps) {
      fetchAudioTimestamps();
    }
  }, [cycle]);

  const fetchAudioTimestamps = useCallback(async () => {
    return await getAudioTimestamps().then((stamps) =>
      setTimestamps(stamps)
    ).catch(() => {setTimeout(() => setCycle(prev => prev + 1), 12000)})
  }, []);
  useEffect(() => {
    chrome.tabs && chrome.tabs.query({
      active: true,
      currentWindow: true
    }, (tabs) => {
      // Callback function
      chrome.tabs.sendMessage(
        tabs[0]?.id || 0,
        {type: 'getSelection'},
        (response) => {
          setContent(`${response?.data}`)
        })
    })
    }, [])
  return (
    <div className="App">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src="/codeHelpsIcon.png" className="logo" alt="Code Helps" />
        </a>
      </div>
      <h1>Code Helps</h1>
      <label>{simplify === undefined ? '?' : <input type="checkbox" checked={simplify} onChange={() => setSimplify(prev => {
        chrome.storage.local.set({[simplifyKey]: !prev})
        return !prev
      })} />} Simplify</label>
      <div className="card">
        {timestamps ? (
          <Player url={record} timestamps={timestamps || []} />
        ) : 'LOADING...'}
        <p>
          Content: "{content}"
        </p>
      </div>
    </div>
  )
}

export default App
