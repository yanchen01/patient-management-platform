import React from 'react';

import {
	Modal,
	ModalOverlay,
	ModalContent,
	ModalHeader,
	ModalFooter,
	ModalBody,
	ModalCloseButton,
	useDisclosure,
	Button
} from '@chakra-ui/react';
import { AddIcon } from '@chakra-ui/icons';


export default function AddModal({ buttonText, title, body }) {
	const { isOpen, onOpen, onClose } = useDisclosure();
	return (
		<React.Fragment>
			<Button
				variant={'solid'}
				colorScheme={'blue'}
				size={'sm'}
				mr={4}
				leftIcon={<AddIcon />}
				width={80}
				onClick={onOpen}
			>
				{buttonText}
			</Button>

			<Modal isOpen={isOpen} onClose={onClose}>
				<ModalOverlay />
				<ModalContent>
					<ModalHeader>{title}</ModalHeader>
					<ModalCloseButton />
					<ModalBody>
						{body}
					</ModalBody>

					<ModalFooter>
						<Button colorScheme="blue" mr={3} onClick={onClose}>
							Submit
						</Button>
						<Button variant="ghost">Close</Button>
					</ModalFooter>
				</ModalContent>
			</Modal>
		</React.Fragment>
	);
}
