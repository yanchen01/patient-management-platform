import { createSlice } from '@reduxjs/toolkit';

export const userSlice = createSlice({
	name: 'user',
	initialState: {
		id: '',
		firstName: '',
		lastName: '',
		email: '',
		userRole: '',
		gender: '',
		dateOfBirth: '',
		address: '',
		age: 0
	},
	reducers: {
		signin: (state, action) => {
			console.log(action.payload);
			state.id = action.payload.id;
			state.firstName = action.payload.first_name;
			state.lastName = action.payload.last_name;
			state.email = action.payload.email;
			state.userRole = action.payload.user_role;
			state.gender = action.payload.gender;
			state.dateOfBirth = action.payload.date_of_birth;
			state.address = action.payload.address;
			state.age = action.payload.age;

			console.log('success signin user');
		},
		logout: (state) => {
			state = null;
		}
	}
});

// Action creators are generated for each case reducer function
export const { signin, logout } = userSlice.actions;

export default userSlice.reducer;
