import {
	Select,
	Flex,
	Box,
	FormControl,
	FormLabel,
	Input,
	InputGroup,
	HStack,
	InputRightElement,
	Stack,
	Button,
	Heading,
	Text,
	useColorModeValue,
	Link,
	Radio,
	RadioGroup,
	NumberInput,
	NumberInputField,
	NumberInputStepper,
	NumberIncrementStepper,
	NumberDecrementStepper
} from '@chakra-ui/react';
import { Link as RedirectLink, useNavigate } from 'react-router-dom';
import { useState } from 'react';
import { ViewIcon, ViewOffIcon } from '@chakra-ui/icons';

import axios from '../axios-api';

export default function SignUp() {
	let navigate = useNavigate();

	const [ showPassword, setShowPassword ] = useState(false);
	const [ firstName, setFirstName ] = useState('');
	const [ lastName, setLastName ] = useState('');
	const [ email, setEmail ] = useState('');
	const [ password, setPassword ] = useState('');
	const [ userRole, setUserRole ] = useState('');
	const [ gender, setGender ] = useState('');
	const [ dateOfBirth, setDateOfBirth ] = useState('');
	const [ address, setAddress ] = useState('');
	const [ age, setAge ] = useState('');

	async function registerUserHandler(e) {
		e.preventDefault();

		const newUser = {
			id: email,
			first_name: firstName,
			last_name: lastName,
			email: email,
			password,
			user_role: userRole,
			gender,
			date_of_birth: dateOfBirth,
			address,
			age
		};

		try {
			const res = await axios.post('/user/', newUser);

			if (res.status === 200) {
				navigate('/signin');
			}
		} catch (e) {
			console.error(e);
		}
	}

	return (
		<Flex minH={'100vh'} align={'center'} justify={'center'} bg={useColorModeValue('gray.50', 'gray.800')}>
			<Stack spacing={8} mx={'auto'} maxW={'lg'} py={12} px={6}>
				<Stack align={'center'}>
					<Heading fontSize={'4xl'} textAlign={'center'}>
						Sign up
					</Heading>
					<Text fontSize={'lg'} color={'gray.600'}>
						to enjoy all of our cool features ✌️
					</Text>
				</Stack>
				<Box rounded={'lg'} bg={useColorModeValue('white', 'gray.700')} boxShadow={'lg'} p={8}>
					<form onSubmit={registerUserHandler}>
						<Stack spacing={4}>
							<HStack>
								<Box>
									<FormControl id="firstName" isRequired>
										<FormLabel>First Name</FormLabel>
										<Input
											type="text"
											onChange={(e) => setFirstName(e.target.value)}
											value={firstName}
										/>
									</FormControl>
								</Box>
								<Box>
									<FormControl id="lastName" isRequired>
										<FormLabel>Last Name</FormLabel>
										<Input
											type="text"
											onChange={(e) => setLastName(e.target.value)}
											value={lastName}
										/>
									</FormControl>
								</Box>
							</HStack>
							<FormControl id="email" isRequired>
								<FormLabel>Email Address</FormLabel>
								<Input type="email" onChange={(e) => setEmail(e.target.value)} value={email} />
							</FormControl>
							<FormControl id="password" isRequired>
								<FormLabel>Password</FormLabel>
								<InputGroup>
									<Input
										onChange={(e) => setPassword(e.target.value)}
										value={password}
										type={showPassword ? 'text' : 'password'}
									/>
									<InputRightElement h={'full'}>
										<Button
											variant={'ghost'}
											onClick={() => setShowPassword((showPassword) => !showPassword)}
										>
											{showPassword ? <ViewIcon /> : <ViewOffIcon />}
										</Button>
									</InputRightElement>
								</InputGroup>
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
							<FormControl id="role" isRequired>
								<Select
									placeholder="Select Your Role"
									onChange={(e) => setUserRole(e.target.value)}
									value={userRole}
								>
									<option value="patient">Patient</option>
									<option value="family">Family</option>
									<option value="nurse">Nurse</option>
									<option value="admin">Admin</option>
									<option value="developer">Developer</option>
									<option value="doctor">Doctor</option>
								</Select>
							</FormControl>
							<HStack>
								<FormControl id="age" isRequired>
									<FormLabel>Age</FormLabel>
									<NumberInput
										size="md"
										maxW={24}
										defaultValue={15}
										min={10}
										onChange={setAge}
										value={age}
									>
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
							<Stack spacing={10} pt={2}>
								<Button
									loadingText="Submitting"
									size="lg"
									bg={'blue.400'}
									color={'white'}
									_hover={{
										bg: 'blue.500'
									}}
									type="submit"
								>
									Sign up
								</Button>
							</Stack>
							<Stack pt={6}>
								<Text align={'center'}>
									Already a user? {' '}
									<Link as={RedirectLink} to="/signin" color={'blue.400'}>
										Login
									</Link>
								</Text>
							</Stack>
						</Stack>
					</form>
				</Box>
			</Stack>
		</Flex>
	);
}
