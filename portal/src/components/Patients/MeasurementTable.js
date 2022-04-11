import React, { useState } from 'react';

import { Table, Thead, Tbody, Tfoot, Tr, Th, Td, TableContainer, Button, Text, Stack, Center } from '@chakra-ui/react';
import AddModal from '../Modal/AddModal';

const Entry = ({ children }) => (
	<Tr>
		<Td>{children.deviceType}</Td>
		<Td isNumeric>{children.reading}</Td>
		<Td>{children.unit}</Td>
	</Tr>
);

export default function MeasurementTable({ measurements }) {
	const [ deviceId, setDeviceId ] = useState('');
	const [ deviceType, setDeviceType ] = useState('');
	const [ reading, setReading ] = useState(0);
	const [ unit, setUnit ] = useState('');

	const AddForm = <h1>Add form here</h1>;

	// const AddForm = (
	// 	<form action="" onSubmit={addMeasurementHandler}>
	// 		<Box rounded={'lg'} bg={useColorModeValue('white', 'gray.700')} boxShadow={'lg'} p={8}>
	// 			<Stack spacing={4}>
	// 				<FormControl id="email" onChange={(e) => setEmail(e.target.value)} value={email}>
	// 					<FormLabel>Email address</FormLabel>
	// 					<Input type="email" />
	// 				</FormControl>
	// 				<FormControl id="password">
	// 					<FormLabel>Password</FormLabel>
	// 					<Input type="password" onChange={(e) => setPassword(e.target.value)} value={password} />
	// 				</FormControl>
	// 				<Stack spacing={10}>
	// 					<Stack direction={{ base: 'column', sm: 'row' }} align={'start'} justify={'space-between'}>
	// 						<Checkbox>Remember me</Checkbox>
	// 						<Link color={'blue.400'}>Forgot password?</Link>
	// 					</Stack>
	// 					<Button
	// 						bg={'blue.400'}
	// 						color={'white'}
	// 						_hover={{
	// 							bg: 'blue.500'
	// 						}}
	// 						type="submit"
	// 					>
	// 						Sign in
	// 					</Button>
	// 				</Stack>
	// 			</Stack>
	// 		</Box>
	// 	</form>
	// );

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
					<AddModal buttonText={'Add Measurement'} title="Add Measurement" body={AddForm} />
				</Center>
			</Stack>
		</TableContainer>
	);
}
