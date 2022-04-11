import React from 'react';
import { Box, VStack, Grid } from '@chakra-ui/react';
import { ColorModeSwitcher } from './ColorModeSwitcher';
import LandingPage from './containers/LandingPage';

function App() {
	return (
		<Box textAlign="center" fontSize="xl">
			<Grid minH="100vh" p={3}>
				<ColorModeSwitcher justifySelf="flex-end" />
				<VStack spacing={8}>
					<LandingPage />
				</VStack>
			</Grid>
		</Box>
	);
}

export default App;
