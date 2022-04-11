import { ColorModeScript } from '@chakra-ui/react';
import React, { StrictMode } from 'react';
import ReactDOM from 'react-dom';
import reportWebVitals from './reportWebVitals';
import * as serviceWorker from './serviceWorker';

import store from './store/store';
import { Provider } from 'react-redux';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import { ChakraProvider, theme } from '@chakra-ui/react';

import App from './App';
import SignIn from './containers/SignIn';
import SignUp from './containers/SignUp';
import Dashboard from './containers/Dashboard';

ReactDOM.render(
	<Provider store={store}>
		<StrictMode>
			<ColorModeScript />
			<ChakraProvider theme={theme}>
				<BrowserRouter>
					<Routes>
						<Route path="/" element={<App />} />
						<Route path="/signup" element={<SignUp />} />
						<Route path="/signin" element={<SignIn />} />
						<Route path="/dashboard" element={<Dashboard />} />
					</Routes>
				</BrowserRouter>
			</ChakraProvider>
		</StrictMode>
	</Provider>,
	document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://cra.link/PWA
serviceWorker.unregister();

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
