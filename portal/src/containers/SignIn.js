import {
	Flex,
	Box,
	FormControl,
	FormLabel,
	Input,
	Checkbox,
	Stack,
	Link,
	Button,
	Heading,
	Text,
	useColorModeValue
} from '@chakra-ui/react';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import axios from '../axios-api';

export default function SignIn() {
	let navigate = useNavigate();

	const [ email, setEmail ] = useState('');
	const [ password, setPassword ] = useState('');

	async function loginUserHandler(e) {
		e.preventDefault();

		const user = {
			id: email,
			password
		};

		try {
			const res = await axios.post('/user/login', user);

			console.log(res);

			if (res.status === 200) {
				navigate('/dashboard');
			}
		} catch (e) {
			console.error(e);
		}
	}
	return (
		<Flex minH={'100vh'} align={'center'} justify={'center'} bg={useColorModeValue('gray.50', 'gray.800')}>
			<Stack spacing={8} mx={'auto'} maxW={'lg'} py={12} px={6}>
				<Stack align={'center'}>
					<Heading fontSize={'4xl'}>Sign in to your account</Heading>
					<Text fontSize={'lg'} color={'gray.600'}>
						to enjoy all of our cool <Link color={'blue.400'}>features</Link> ✌️
					</Text>
				</Stack>
				<form action="" onSubmit={loginUserHandler}>
					<Box rounded={'lg'} bg={useColorModeValue('white', 'gray.700')} boxShadow={'lg'} p={8}>
						<Stack spacing={4}>
							<FormControl id="email" onChange={(e) => setEmail(e.target.value)} value={email}>
								<FormLabel>Email address</FormLabel>
								<Input type="email" />
							</FormControl>
							<FormControl id="password">
								<FormLabel>Password</FormLabel>
								<Input type="password" onChange={(e) => setPassword(e.target.value)} value={password} />
							</FormControl>
							<Stack spacing={10}>
								<Stack
									direction={{ base: 'column', sm: 'row' }}
									align={'start'}
									justify={'space-between'}
								>
									<Checkbox>Remember me</Checkbox>
									<Link color={'blue.400'}>Forgot password?</Link>
								</Stack>
								<Button
									bg={'blue.400'}
									color={'white'}
									_hover={{
										bg: 'blue.500'
									}}
									type="submit"
								>
									Sign in
								</Button>
							</Stack>
						</Stack>
					</Box>
				</form>
			</Stack>
		</Flex>
	);
}
