// // src/App.tsx
// import React from 'react';
// import { Box, Container, Typography, Button, AppBar, Toolbar } from '@mui/material';
// import { ChatInterface } from './components/Chat/ChatInterface';
// import { FileUpload } from './components/FileUpload/FileUpload';

// function App() {
//   const [showChat, setShowChat] = React.useState(false);

//   return (
//     <Box sx={{ minHeight: '100vh', bgcolor: '#f5f5f5' }}>
//       {/* Navigation Bar */}
//       <AppBar position="static" color="transparent" elevation={0}>
//         <Toolbar sx={{ justifyContent: 'space-between' }}>
//           <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
//             Student Assistant
//           </Typography>
//           <Box>
//             <Button color="inherit" sx={{ mr: 2 }}>About</Button>
//             <Button color="inherit" sx={{ mr: 2 }}>Features</Button>
//             <Button variant="contained" color="primary">
//               Get Started
//             </Button>
//           </Box>
//         </Toolbar>
//       </AppBar>

//       {/* Hero Section */}
//       {!showChat && (
//         <Container maxWidth="lg" sx={{ mt: 8, textAlign: 'center' }}>
//           <Typography
//             variant="h2"
//             component="h1"
//             sx={{
//               fontWeight: 'bold',
//               mb: 3,
//               fontSize: { xs: '2.5rem', md: '3.5rem' }
//             }}
//           >
//             Learn at Your Own Pace
//           </Typography>
          
//           <Typography
//             variant="h6"
//             color="text.secondary"
//             sx={{ mb: 6, maxWidth: '600px', mx: 'auto' }}
//           >
//             Unlock your potential with our AI tutor. Upload your materials or connect with a live tutor.
//           </Typography>

//           <Box sx={{ display: 'flex', gap: 2, justifyContent: 'center' }}>
//             <Button
//               variant="contained"
//               size="large"
//               color="primary"
//               onClick={() => setShowChat(true)}
//               sx={{
//                 py: 2,
//                 px: 4,
//                 borderRadius: 2,
//                 textTransform: 'none',
//                 fontSize: '1.1rem'
//               }}
//             >
//               Learn with a Live Tutor
//             </Button>
//             <Button
//               variant="outlined"
//               size="large"
//               color="primary"
//               onClick={() => setShowChat(true)}
//               sx={{
//                 py: 2,
//                 px: 4,
//                 borderRadius: 2,
//                 textTransform: 'none',
//                 fontSize: '1.1rem'
//               }}
//             >
//               Upload Your Material and Learn
//             </Button>
//           </Box>
//         </Container>
//       )}

//       {/* Chat Interface */}
//       {showChat && (
//         <Container maxWidth="lg" sx={{ mt: 4 }}>
//           <Box sx={{
//             bgcolor: 'white',
//             borderRadius: 4,
//             boxShadow: 1,
//             overflow: 'hidden'
//           }}>
//             <FileUpload />
//             <ChatInterface />
//           </Box>
//         </Container>
//       )}
//     </Box>
//   );
// }

// export default App;

// src/App.tsx
import React, { useState } from 'react';
import { Box, Container } from '@mui/material';
import { Welcome } from './components/Welcome/Welcome';
import { LiveTutorChat } from './components/LiveTutor/LiveTutorChat';
import { ChatInterface } from './components/Chat/ChatInterface';
import { FileUpload } from './components/FileUpload/FileUpload';

type Mode = 'welcome' | 'liveTutor' | 'selfStudy';

function App() {
  const [mode, setMode] = useState<Mode>('welcome');

  return (
    <Box sx={{ minHeight: '100vh', bgcolor: '#f5f5f5', py: 4 }}>
      <Container maxWidth="lg">
        {mode === 'welcome' && (
          <Welcome
            onSelectLiveTutor={() => setMode('liveTutor')}
            onSelectSelfStudy={() => setMode('selfStudy')}
          />
        )}

        {mode === 'liveTutor' && (
          <Box sx={{ 
            bgcolor: 'white', 
            borderRadius: 2, 
            boxShadow: 1,
            overflow: 'hidden'
          }}>
            <LiveTutorChat />
          </Box>
        )}

        {mode === 'selfStudy' && (
          <Box sx={{ 
            bgcolor: 'white', 
            borderRadius: 2, 
            boxShadow: 1,
            overflow: 'hidden'
          }}>
            <FileUpload />
            <ChatInterface />
          </Box>
        )}
      </Container>
    </Box>
  );
}

export default App;