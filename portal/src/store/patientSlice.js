import { createSlice } from '@reduxjs/toolkit';

export const patientSlice = createSlice({
	name: 'patients',
	initialState: {
		patients: [
			{
				id: 'ychen1116@gmail.com',
				firstName: 'Yan',
				lastName: 'Chen',
				email: 'ychen1116@gmail.com',
				userRole: 'patient',
				gender: 'male',
				dateOfBirth: '11-16-2000',
				address: 'Boston University',
				age: 21
			}
		]
	},
	reducers: {
		addPatient: (state, action) => {
			state.patients.push(action.payload);
			console.log('success add patient');
		}
	}
});

// Action creators are generated for each case reducer function
export const { addPatient } = patientSlice.actions;

export default patientSlice.reducer;
