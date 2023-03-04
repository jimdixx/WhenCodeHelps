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
          <img src="/codeHelpsIcon.png" className="logo" alt="Code Helps" />
        </a>
      </div>
      <h1>Code Helps</h1>
      <div className="card">
        <p>
          Content: "{content}"
        </p>
      </div>
    </div>
  )
}

export default App
