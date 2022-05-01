import React, { useState } from 'react';

import {
	HStack,
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
	useDisclosure,
	Radio,
	RadioGroup,
	NumberInput,
	NumberInputField,
	NumberInputStepper,
	NumberIncrementStepper,
	NumberDecrementStepper
} from '@chakra-ui/react';
import AddModal from '../Modal/AddModal';


const Entry = ({ children }) => (
	<Tr>
		<Td>{`${children.firstName} ${children.lastName}`}</Td>
		<Td>{children.age}</Td>
		<Td>{children.gender}</Td>
		<Td>{children.dateOfBirth}</Td>
	</Tr>
);

export default function PatientsTable({ patients, onAddPatient }) {
	const [ firstName, setFirstName ] = useState('');
	const [ lastName, setLastName ] = useState('');
	const [ email, setEmail ] = useState('');
	const [ gender, setGender ] = useState('');
	const [ dateOfBirth, setDateOfBirth ] = useState('');
	const [ address, setAddress ] = useState('');
	const [ age, setAge ] = useState('');

	// modal state
	const { isOpen, onOpen, onClose } = useDisclosure();

	const addPatientHandler = async () => {
		const newPatient = {
			id: `${firstName + lastName}`,
			firstName,
			lastName,
			userRole: 'patient',
			dateOfBirth,
			address,
			age,
            gender
		};
		console.log('here');
		onAddPatient(newPatient);
		onClose();
	};

	const AddForm = (
		<form action="" onSubmit={addPatientHandler}>
			<Box rounded={'lg'} bg={useColorModeValue('white', 'gray.700')} boxShadow={'lg'} p={8}>
				<Stack spacing={4}>
					<HStack>
						<Box>
							<FormControl id="firstName" isRequired>
								<FormLabel>First Name</FormLabel>
								<Input type="text" onChange={(e) => setFirstName(e.target.value)} value={firstName} />
							</FormControl>
						</Box>
						<Box>
							<FormControl id="lastName" isRequired>
								<FormLabel>Last Name</FormLabel>
								<Input type="text" onChange={(e) => setLastName(e.target.value)} value={lastName} />
							</FormControl>
						</Box>
					</HStack>
					<FormControl id="email" isRequired>
						<FormLabel>Email Address</FormLabel>
						<Input type="email" onChange={(e) => setEmail(e.target.value)} value={email} />
					</FormControl>

					<FormControl as="fieldset" isRequired>
						<FormLabel as="legend">Select Your Gender</FormLabel>
						<RadioGroup id="gender" onChange={setGender} value={gender}>
							<HStack spacing="24px">
								<Radio value="male">Male</Radio>
								<Radio value="female">Female</Radio>
								<Radio value="other">Other</Radio>
							</HStack>
						</RadioGroup>
					</FormControl>

					<HStack>
						<FormControl id="age" isRequired>
							<FormLabel>Age</FormLabel>
							<NumberInput size="md" maxW={24} defaultValue={15} min={10} onChange={setAge} value={age}>
								<NumberInputField />
								<NumberInputStepper>
									<NumberIncrementStepper />
									<NumberDecrementStepper />
								</NumberInputStepper>
							</NumberInput>
						</FormControl>
						<FormControl id="dateOfBirth" isRequired>
							<FormLabel>Birth Date</FormLabel>
							<Input
								placeholder="MM-DD-YYYY"
								onChange={(e) => setDateOfBirth(e.target.value)}
								value={dateOfBirth}
							/>
						</FormControl>
					</HStack>
					<FormControl id="address" isRequired>
						<FormLabel>Address</FormLabel>
						<Input type="text" onChange={(e) => setAddress(e.target.value)} value={address} />
					</FormControl>
				</Stack>
			</Box>
		</form>
	);

	return (
		<TableContainer marginTop={5}>
			<Stack spacing={3}>
				<Text fontSize="xl" color={'gray.600'}>
					Patients
				</Text>
				<Table variant="simple" colorScheme="gray" size={'lg'}>
					<Thead bgColor={'gray.100'}>
						<Tr>
							<Th>Name</Th>
							<Th>Age</Th>
							<Th>Gender</Th>
							<Th>DoB</Th>
						</Tr>
					</Thead>
					<Tbody>{patients.map((patient) => <Entry key={patient.id}>{patient}</Entry>)}</Tbody>
				</Table>
				<Center>
					<AddModal
						buttonText={'Add Patient'}
						title="Adding a patient"
						body={AddForm}
						submitHandler={addPatientHandler}
						isOpen={isOpen}
						onOpen={onOpen}
						onClose={onClose}
					/>
				</Center>
			</Stack>
		</TableContainer>
	);
}
