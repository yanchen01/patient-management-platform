import React from 'react';
import { Box, Container } from '@chakra-ui/react';
import { useSelector } from 'react-redux';
import Navbar from '../components/Nav/Navbar';

import MeasurementTable from '../components/Patients/MeasurementTable';

const measurements = [
	{
		deviceType: 'thermometer',
		reading: 33,
		unit: 'celsius'
	},
	{
		deviceType: 'scale',
		reading: 150,
		unit: 'lbs'
	},
	{
		deviceType: 'pulse',
		reading: 100,
		unit: 'bpm'
	}
];

export default function Dashboard() {
	const user = useSelector((state) => state.user);

	return (
		<React.Fragment>
			<Navbar user={user} />
			{/* show patient view */}

			<Container w="100%" p={4}>
				<MeasurementTable measurements={measurements}/>
			</Container>
		</React.Fragment>
	);
}
