import React, { useState } from 'react';

import {
	Table,
	Thead,
	Tbody,
	Tr,
	Th,
	Td,
	TableContainer,
	Button,
	Text,
	Stack,
	Center,
	Box,
	useColorModeValue,
	FormControl,
	FormLabel,
	Input,
	Select,
	useDisclosure
} from '@chakra-ui/react';
import AddModal from '../Modal/AddModal';

import axios from '../../axios-api';

const Entry = ({ children }) => (
	<Tr>
		<Td>{children.deviceType}</Td>
		<Td isNumeric>{children.reading}</Td>
		<Td>{children.unit}</Td>
	</Tr>
);

export default function MeasurementTable({ measurements, userId, onAddMeasurement }) {
	const [ deviceId, setDeviceId ] = useState('');
	const [ deviceType, setDeviceType ] = useState('');
	const [ reading, setReading ] = useState(0);
	const [ unit, setUnit ] = useState('');

	// modal state
	const { isOpen, onOpen, onClose } = useDisclosure();

	const addMeasurementHandler = async () => {
		const newMeasurement = {
			id: deviceId,
			device_id: deviceId,
			device_type: deviceType,
			reading,
			unit,
			user_id: userId
		};

		try {
			const res = await axios.post('/measurement/', newMeasurement);

			if (res.status === 200) {
				onClose();
				onAddMeasurement({
					deviceType,
					reading,
					unit
				});
			}
		} catch (e) {
			console.error(e);
		}
	};

	const AddForm = (
		<form action="" onSubmit={addMeasurementHandler}>
			<Box rounded={'lg'} bg={useColorModeValue('white', 'gray.700')} boxShadow={'lg'} p={8}>
				<Stack spacing={4}>
					<FormControl
						id="deviceId"
						onChange={(e) => setDeviceId(e.target.value)}
						value={deviceId}
						isRequired
					>
						<FormLabel>Device Id</FormLabel>
						<Input type="text" />
					</FormControl>

					<FormControl id="deviceType" isRequired>
						<Select
							placeholder="Device Type"
							onChange={(e) => setDeviceType(e.target.value)}
							value={deviceType}
						>
							<option value="thermometer">thermometer</option>
							<option value="scale">scale</option>
							<option value="pulse">pulse</option>
							<option value="oximeter">oximeter</option>
							<option value="glucometer">glucometer</option>
							<option value="blood_pressure">blood pressure</option>
						</Select>
					</FormControl>

					<FormControl id="reading" onChange={(e) => setReading(e.target.value)} value={reading} isRequired>
						<FormLabel>Reading</FormLabel>
						<Input type="number" />
					</FormControl>

					<FormControl id="unit" isRequired>
						<Select placeholder="Unit" onChange={(e) => setUnit(e.target.value)} value={unit} isRequired>
							<option value="celsius">celsius</option>
							<option value="fahrenheit">fahrenheit</option>
							<option value="lbs">lbs</option>
							<option value="kg">kg</option>
							<option value="bpm">bpm</option>
							<option value="percent">percent</option>
							<option value="mg/dl">mg/dl</option>
							<option value="mmhg">mmhg</option>
						</Select>
					</FormControl>
				</Stack>
			</Box>
		</form>
	);

	return (
		<TableContainer>
			<Stack spacing={3}>
				<Text fontSize="xl" color={'gray.600'}>
					Device Measurements
				</Text>
				<Table variant="simple" colorScheme="gray" size={'lg'}>
					<Thead bgColor={'gray.100'}>
						<Tr>
							<Th>Type</Th>
							<Th isNumeric>Reading</Th>
							<Th>Unit</Th>
						</Tr>
					</Thead>
					<Tbody>
						{measurements.map((measurement) => <Entry key={measurement.reading}>{measurement}</Entry>)}
					</Tbody>
				</Table>
				<Center>
					<AddModal
						buttonText={'Add Measurement'}
						title="Add Measurement"
						body={AddForm}
						addMeasurementHandler={addMeasurementHandler}
						isOpen={isOpen}
						onOpen={onOpen}
						onClose={onClose}
					/>
				</Center>
			</Stack>
		</TableContainer>
	);
}
