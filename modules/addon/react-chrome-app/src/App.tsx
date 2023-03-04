import {useEffect, useState} from 'react'
import reactLogo from './assets/react.svg'
import './App.css'

function App() {
  const [content, setContent] = useState("")

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
          <img src="/vite.svg" className="logo" alt="Vite logo" />
        </a>
        <a href="https://reactjs.org" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <p>
          Content: "{content}"
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}

export default App
