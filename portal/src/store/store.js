import { configureStore } from '@reduxjs/toolkit';
import userReducer from './userSlice';
import appointmentReducer from './appointmentSlice';
import patientReducer from './patientSlice';

export default configureStore({
	reducer: {
		user: userReducer,
		appointments: appointmentReducer,
		patients: patientReducer
	}
});
