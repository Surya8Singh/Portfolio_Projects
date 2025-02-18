// src/components/Welcome/Welcome.tsx
import React from 'react';
import { Box, Typography, Button, Container } from '@mui/material';

interface WelcomeProps {
  onSelectLiveTutor: () => void;
  onSelectSelfStudy: () => void;
}

export const Welcome: React.FC<WelcomeProps> = ({ onSelectLiveTutor, onSelectSelfStudy }) => {
  return (
    <Container maxWidth="md" sx={{ textAlign: 'center', mt: 8 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Welcome to Student Assistant
      </Typography>
      
      <Typography variant="body1" color="text.secondary" sx={{ mb: 4 }}>
        Choose how you'd like to learn today
      </Typography>
      
      <Box sx={{ display: 'flex', gap: 3, justifyContent: 'center' }}>
        <Button
          variant="contained"
          size="large"
          onClick={onSelectLiveTutor}
          sx={{ minWidth: 200 }}
        >
          Learn with a Live Tutor
        </Button>
        
        <Button
          variant="outlined"
          size="large"
          onClick={onSelectSelfStudy}
          sx={{ minWidth: 200 }}
        >
          Upload Material and Learn
        </Button>
      </Box>
    </Container>
  );
};