import { createSlice } from '@reduxjs/toolkit';

export const appointmentSlice = createSlice({
	name: 'appointments',
	initialState: {
		appointments: [
			// {
			// 	id: '1',
			// 	name: 'Yan Chen',
			// 	role: 'Doctor',
			// 	date: '11-16-2022 3:00 PM'
			// },
			// {
			// 	id: '2',
			// 	name: 'Khoa Tran',
			// 	role: 'Nurse',
			// 	date: '03-02-2023 11:00 AM'
			// }
		]
	},
	reducers: {
		addAppointment: (state, action) => {
			state.appointments.push(action.payload);
			console.log('success add appointment');
		}
	}
});

// Action creators are generated for each case reducer function
export const { addAppointment } = appointmentSlice.actions;

export default appointmentSlice.reducer;
