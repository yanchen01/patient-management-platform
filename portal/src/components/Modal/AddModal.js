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

export default function AddModal({ buttonText, title, body, addMeasurementHandler, isOpen, onOpen, onClose }) {
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
					<ModalBody>{body}</ModalBody>

					<ModalFooter>
						<Button onClick={addMeasurementHandler} colorScheme="blue" mr={3}>
							Submit
						</Button>
						<Button variant="ghost" onClick={onClose}>
							Close
						</Button>
					</ModalFooter>
				</ModalContent>
			</Modal>
		</React.Fragment>
	);
}
