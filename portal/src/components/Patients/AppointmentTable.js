import React, { useState } from 'react';

import {
	Table,
	Thead,
	Tbody,
	Tr,
	Th,
	Td,
	TableContainer,
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

const Entry = ({ children }) => (
	<Tr>
		<Td>{children.name}</Td>
		<Td>{children.role}</Td>
		<Td>{children.date}</Td>
	</Tr>
);

export default function AppointmentTable({ appointments, onAddAppointment }) {
	const [ name, setName ] = useState('');
	const [ role, setRole ] = useState('');
	const [ date, setDate ] = useState('');

	// modal state
	const { isOpen, onOpen, onClose } = useDisclosure();

	const addAppointmentHandler = async () => {
		const newAppointment = {
			id: `${name + role + date}`,
			name,
			role,
			date
		};
		onClose();
		onAddAppointment(newAppointment);

		// try {
		// 	const res = await axios.post('/measurement/', newMeasurement);
		// 	if (res.status === 200) {
		// 		onClose();
		// 		onAddMeasurement({
		// 			deviceType,
		// 			reading,
		// 			unit
		// 		});
		// 	}
		// } catch (e) {
		// 	console.error(e);
		// }
	};

	const AddForm = (
		<form action="" onSubmit={onAddAppointment}>
			<Box rounded={'lg'} bg={useColorModeValue('white', 'gray.700')} boxShadow={'lg'} p={8}>
				<Stack spacing={4}>
					<FormControl id="name" isRequired>
						<FormLabel>Doctor/Nurse Name</FormLabel>
						<Select placeholder="select a name" onChange={(e) => setName(e.target.value)} value={name}>
							<option value="Yan Chen">Yan Chen</option>
							<option value="Khoa Tran">Khoa Tran</option>
						</Select>
					</FormControl>

					<FormControl id="role" isRequired>
						<FormLabel>MP Role</FormLabel>
						<Select placeholder="select a role" onChange={(e) => setRole(e.target.value)} value={role}>
							<option value="doctor">doctor</option>
							<option value="nurse">nurse</option>
							<option value="patient">patient</option>
						</Select>
					</FormControl>

					<FormControl id="date" onChange={(e) => setDate(e.target.value)} value={date} isRequired>
						<FormLabel>Date</FormLabel>
						<Input />
					</FormControl>
				</Stack>
			</Box>
		</form>
	);

	return (
		<TableContainer marginTop={5}>
			<Stack spacing={3}>
				<Text fontSize="xl" color={'gray.600'}>
					Upcoming Appointments
				</Text>
				<Table variant="simple" colorScheme="gray" size={'lg'}>
					<Thead bgColor={'gray.100'}>
						<Tr>
							<Th>Name</Th>
							<Th>Role</Th>
							<Th>Date</Th>
						</Tr>
					</Thead>
					<Tbody>
						{appointments.map((appointment) => <Entry key={appointment.id}>{appointment}</Entry>)}
					</Tbody>
				</Table>
				<Center>
					<AddModal
						buttonText={'Book Appointment'}
						title="Booking an Appointment"
						body={AddForm}
						submitHandler={addAppointmentHandler}
						isOpen={isOpen}
						onOpen={onOpen}
						onClose={onClose}
					/>
				</Center>
			</Stack>
		</TableContainer>
	);
}
