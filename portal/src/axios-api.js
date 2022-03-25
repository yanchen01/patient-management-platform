import axios from 'axios';

let API_URL = '';
if (process.env.REACT_APP_ENV === 'DEV') {
	API_URL = 'http://localhost:4000/api';
} else if (process.env.REACT_APP_ENV === 'PROD') {
	API_URL = 'http://ec2-34-229-204-202.compute-1.amazonaws.com:4000/api';
}

const instance = axios.create({
	baseURL: API_URL,
	headers: {
		'Access-Control-Allow-Origin': '*',
		'Content-Type': 'application/json'
	}
});

export default instance;
