// src/components/LiveTutor/LiveTutorChat.tsx
import React from 'react';
import { Box, Avatar } from '@mui/material';
import { ChatInterface } from '../Chat/ChatInterface';
import { FileUpload } from '../FileUpload/FileUpload';

export const LiveTutorChat: React.FC = () => {
  return (
    <Box sx={{ display: 'flex', gap: 2, p: 2 }}>
      <Avatar
        sx={{ 
          width: 60, 
          height: 60,
          bgcolor: 'primary.main'
        }}
      >
        AI
      </Avatar>
      <Box sx={{ flexGrow: 1 }}>
        <FileUpload />
        <ChatInterface />
      </Box>
    </Box>
  );
};