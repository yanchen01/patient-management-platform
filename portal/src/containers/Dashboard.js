import React, { useEffect, useState } from 'react';
import { Container } from '@chakra-ui/react';

import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
import { addAppointment } from '../store/appointmentSlice';
import { addPatient } from '../store/patientSlice';

import Navbar from '../components/Nav/Navbar';
import MeasurementTable from '../components/Patients/MeasurementTable';
import AppointmentTable from '../components/Patients/AppointmentTable';
import PatientsTable from '../components/MP/PatientsTable';

import axios from '../axios-api';

export default function Dashboard() {
	const user = useSelector((state) => state.user);
	const appointments = useSelector((state) => state.appointments.appointments);
	const patients = useSelector((state) => state.patients.patients);

	const dispatch = useDispatch();

	const [ measurements, setMeasurements ] = useState([]);

	const onAddMeasurement = (measurement) => {
		setMeasurements([ ...measurements, measurement ]);
	};

	const onAddPatient = (patient) => {
		dispatch(addPatient(patient));
	};

	const onAddAppointment = (appointment) => {
		console.log('dashboard add apt', appointment);
		dispatch(addAppointment(appointment));
	};

	useEffect(() => {
		async function fetchMeasurements() {
			try {
				const res = await axios.get('/measurement/');
				if (res.status === 200 && res.data) {
					let userMeasurements = res.data.data;

					// get current user's measurements
					userMeasurements = userMeasurements.filter((measurement) => measurement.user_id === user.id);
					userMeasurements = userMeasurements.map((measurement) => {
						return {
							deviceType: measurement.device_type,
							reading: measurement.reading,
							unit: measurement.unit
						};
					});
					setMeasurements(userMeasurements);
				}
			} catch (e) {
				console.error(e);
			}
		}
		fetchMeasurements();
	}, []);

	let view;

	if (user.userRole === 'patient') {
		// show patient view
		view = (
			<Container w="100%" p={4}>
				<MeasurementTable measurements={measurements} onAddMeasurement={onAddMeasurement} userId={user.id} />
				<AppointmentTable appointments={appointments} onAddAppointment={onAddAppointment} />
			</Container>
		);
	} else if (user.userRole === 'doctor' || user.userRole === 'nurse') {
		// show MP view
		view = (
			<Container w="100%" p={4}>
				<PatientsTable patients={patients} onAddPatient={onAddPatient} />
				<AppointmentTable appointments={appointments} onAddAppointment={onAddAppointment} />
			</Container>
		);
	}

	return (
		<React.Fragment>
			<Navbar user={user} />
			{view}
		</React.Fragment>
	);
}
