import {useEffect, useState} from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import {Player} from "./components/Player";

const simplifyKey = 'simplify'
function App() {
  const [content, setContent] = useState("")
  const [simplify, setSimplify] = useState<boolean | undefined>(undefined)
  const [record, setRecord] = useState<{ url: string, timestamps: number[] } | undefined>({
    url: "https://storage.googleapis.com/media-session/elephants-dream/the-wires.mp3",
    timestamps: [1,2,5],
  })

  useEffect(() => {
    chrome.storage.local.get().then(res => setSimplify(!!res[simplifyKey]))
  }, [])
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
        <p>
          Content: "{content}"
        </p>
        {record && (
          <Player url={record.url} timestamps={record.timestamps} />
        )}
      </div>
    </div>
  )
}

export default App
