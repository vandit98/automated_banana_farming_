import React from 'react';
import ReactDOM from 'react-dom';
import { Auth0Provider } from '@auth0/auth0-react';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <Auth0Provider
      domain="dev-lglwplylbe8gtz5y.us.auth0.com"
      clientId="kTVQRhlbk7XT8fcByJrI7KXYHdlB4x5F"
      authorizationParams={{
        redirect_uri: 'https://automated-banana-farming-879626.spheron.app/landing'
      }}
    >
    <App />
  </Auth0Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
