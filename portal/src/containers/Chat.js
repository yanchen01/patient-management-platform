import './App.css';

import {
	Button,
	Tr,
	Td,
	Stack,
	TableContainer,
	Text,
	Thead,
	Th,
	Tbody,
	Table,
	Heading,
} from '@chakra-ui/react';

import io from 'socket.io-client';

import { useSelector } from 'react-redux';
import { useState, useEffect } from 'react';
import Chat from '../components/Chat/Chat';

import axios from '../axios-api';

const socket = io.connect('http://localhost:3001/');

export default function ChatRoom() {
	const currentUser = useSelector((state) => state.user);
	const [ username, setUsername ] = useState('');
	const [ userId, setUserId ] = useState('');

	const [ users, setUsers ] = useState([]);
	const [ room, setRoom ] = useState('');
	const [ showChat, setShowChat ] = useState(false);

	const joinRoom = (recipientId) => {
		console.log('currentUser', currentUser, 'recipient', recipientId);
		if (currentUser && currentUser.id && currentUser.userRole === 'patient') {
			setRoom(userId);
			socket.emit('join_room', userId);
			setShowChat(true);
		} else if ((currentUser && currentUser.userRole === 'doctor') || currentUser.userRole === 'nurse') {
			setRoom(recipientId);
			socket.emit('join_room', recipientId);
			setShowChat(true);
		}
	};

	const Entry = ({ children }) => (
		<Tr>
			<Td>{`${children.firstName} ${children.lastName}`}</Td>
			<Td>{children.userRole}</Td>
			<Td>{children.email}</Td>
			<Td>
				<Button size={'xs'} colorScheme={'blue'} onClick={() => joinRoom(children.id)}>
					Chat
				</Button>
			</Td>
		</Tr>
	);

	useEffect(() => {
		async function fetchUsers() {
			try {
				const res = await axios.get('/user/');
				if (res.status === 200 && res.data) {
					let users = res.data.data;

					users = users.filter((user) => user.id !== currentUser.id);
					users = users.map((user) => {
						return {
							id: user.id,
							firstName: user.first_name,
							lastName: user.last_name,
							userRole: user.user_role,
							email: user.email
						};
					});
					setUsers(users);
				}
			} catch (e) {
				console.error(e);
			}
		}
		fetchUsers();
		setUsername(currentUser.firstName);
		setUserId(currentUser.id);
	}, []);

	return (
		<div>
			{!showChat ? (
				<Stack w="100%" p={4}>
					<Heading size={'lg'} color={'gray.700'} marginBottom={5}>
						Join a chat
					</Heading>

					<TableContainer marginTop={5}>
						<Stack spacing={3}>
							<Text fontSize="xl" color={'gray.600'}>
								Users
							</Text>
							<Table variant="simple" colorScheme="gray" size={'lg'}>
								<Thead bgColor={'gray.100'}>
									<Tr>
										<Th>Name</Th>
										<Th>Roles</Th>
										<Th>Email</Th>
										<Th>Actions</Th>
									</Tr>
								</Thead>
								<Tbody>{users.map((user) => <Entry key={user.id}>{user}</Entry>)}</Tbody>
							</Table>
						</Stack>
					</TableContainer>
				</Stack>
			) : (
				<Chat socket={socket} username={username} room={room} />
			)}
		</div>
	);
}
