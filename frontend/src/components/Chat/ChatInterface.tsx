import React, { useState, useEffect } from 'react';
import { Box, TextField, Button, Container, Paper } from '@mui/material';
import { ChatMessage } from './ChatMessage';
import { api } from '../../services/api';
import { Message } from '../../types';

export const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [sessionId, setSessionId] = useState<string>('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const initSession = async () => {
      try {
        const id = await api.createSession();
        setSessionId(id);
      } catch (error) {
        console.error('Failed to initialize session:', error);
      }
    };
    initSession();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || !sessionId) return;

    const userMessage: Message = {
      role: 'user',
      content: input
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await api.sendMessage(input, sessionId);
      const assistantMessage: Message = {
        role: 'assistant',
        content: response.formatted_answer || response.answer
      };
      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage: Message = {
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please try again.'
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ 
      height: '600px',
      display: 'flex',
      flexDirection: 'column'
    }}>
      <Box sx={{ 
        flexGrow: 1, 
        overflow: 'auto', 
        p: 3,
        bgcolor: '#f8f9fa'
      }}>
        {messages.map((message, index) => (
          <ChatMessage key={index} message={message} />
        ))}
      </Box>
      
      <Box 
        component="form" 
        onSubmit={handleSubmit}
        sx={{
          p: 2,
          bgcolor: 'white',
          borderTop: '1px solid #eee'
        }}
      >
        <TextField
          fullWidth
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={loading}
          placeholder="Ask anything..."
          variant="outlined"
          sx={{
            '& .MuiOutlinedInput-root': {
              borderRadius: '12px',
              bgcolor: '#f8f9fa'
            }
          }}
        />
        <Button 
          type="submit"
          variant="contained"
          disabled={loading}
          sx={{
            mt: 1,
            width: '100%',
            borderRadius: '12px',
            py: 1.5,
            bgcolor: '#0052FF',
            '&:hover': {
              bgcolor: '#0043CC'
            }
          }}
        >
          {loading ? 'Thinking...' : 'Send Message'}
        </Button>
      </Box>
    </Box>
  );
};