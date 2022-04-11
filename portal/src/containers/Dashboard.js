import React, { useEffect, useState } from 'react';
import { Box, Container } from '@chakra-ui/react';
import { useSelector } from 'react-redux';
import Navbar from '../components/Nav/Navbar';

import MeasurementTable from '../components/Patients/MeasurementTable';
import axios from '../axios-api';

// const measurements = [
// 	{
// 		deviceType: 'thermometer',
// 		reading: 33,
// 		unit: 'celsius'
// 	},
// 	{
// 		deviceType: 'scale',
// 		reading: 150,
// 		unit: 'lbs'
// 	},
// 	{
// 		deviceType: 'pulse',
// 		reading: 100,
// 		unit: 'bpm'
// 	}
// ];

export default function Dashboard() {
	const user = useSelector((state) => state.user);

	const [ measurements, setMeasurements ] = useState([]);

	const onAddMeasurement = (measurement) => {
		setMeasurements([ ...measurements, measurement ]);
	};

	useEffect(
		() => {
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
		},
		[ measurements, user.id ]
	);

	return (
		<React.Fragment>
			<Navbar user={user} />
			{/* show patient view */}
			<Container w="100%" p={4}>
				<MeasurementTable measurements={measurements} onAddMeasurement={onAddMeasurement} userId={user.id} />
			</Container>
		</React.Fragment>
	);
}
