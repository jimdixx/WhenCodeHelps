const messagesFromReactAppListener = (
  message,
  sender,
  sendResponse) => {

  if (message.type === 'getSelection')
    sendResponse({ title: document.title, data: window.getSelection().toString()});
  else
    sendResponse({title: document.title, data: ''}); // snub them.

}

/**
 * Fired when a message is sent from either an extension process or a content script.
 */
chrome.runtime.onMessage.addListener(messagesFromReactAppListener);