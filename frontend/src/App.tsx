// src/App.tsx
import React from 'react';
import { Box, Container, Typography } from '@mui/material';
import { ChatInterface } from './components/Chat/ChatInterface';
import { FileUpload } from './components/FileUpload/FileUpload';

function App() {
  return (
    <Box sx={{ 
      minHeight: '100vh',
      bgcolor: '#0052FF', // Blue background color
      color: 'white',
      pt: 8
    }}>
      <Container maxWidth="lg">
        <Typography
          variant="h2"
          component="h1"
          sx={{
            textAlign: 'center',
            mb: 4,
            fontWeight: 'bold',
            fontSize: { xs: '2rem', md: '3.5rem' }
          }}
        >
          What if students could get instant answers
          <br />
          to their academic questions?
        </Typography>
        
        <Typography
          variant="h6"
          sx={{
            textAlign: 'center',
            mb: 6,
            maxWidth: '800px',
            mx: 'auto'
          }}
        >
          Our AI assistant is here to help you learn better. Upload your study materials and get instant, accurate responses.
        </Typography>

        <Box sx={{
          maxWidth: '800px',
          mx: 'auto',
          bgcolor: 'white',
          borderRadius: 4,
          boxShadow: 3,
          overflow: 'hidden'
        }}>
          <Box sx={{ p: 2, borderBottom: '1px solid #eee' }}>
            <FileUpload />
          </Box>
          <ChatInterface />
        </Box>
      </Container>
    </Box>
  );
}

export default App;