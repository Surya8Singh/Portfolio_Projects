// src/components/FileUpload/FileUpload.tsx
import React, { useState } from 'react';
import { Box, Button, LinearProgress, Typography } from '@mui/material';
import { api } from '../../services/api';

export const FileUpload: React.FC = () => {
  const [uploading, setUploading] = useState(false);
  const [files, setFiles] = useState<File[]>([]);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFiles(Array.from(event.target.files));
    }
  };

  const handleUpload = async () => {
    if (files.length === 0) return;

    setUploading(true);
    try {
      await api.uploadDocuments(files);
      setFiles([]);
    } catch (error) {
      console.error('Upload error:', error);
    } finally {
      setUploading(false);
    }
  };

  return (
    <Box sx={{ p: 2 }}>
      <input
        type="file"
        multiple
        accept=".txt,.pdf,.doc,.docx"
        onChange={handleFileChange}
        style={{ display: 'none' }}
        id="file-input"
      />
      <label htmlFor="file-input">
        <Button
          variant="outlined"
          component="span"
          sx={{
            borderRadius: '12px',
            borderColor: '#0052FF',
            color: '#0052FF',
            '&:hover': {
              borderColor: '#0043CC',
              bgcolor: 'rgba(0, 82, 255, 0.04)'
            }
          }}
        >
          Upload Study Materials
        </Button>
      </label>
      
      {files.length > 0 && (
        <Box sx={{ mt: 2 }}>
          <Typography color="text.secondary">
            Selected files:
          </Typography>
          {files.map((file, index) => (
            <Typography 
              key={index} 
              variant="body2"
              color="text.primary"
            >
              {file.name}
            </Typography>
          ))}
          <Button
            variant="contained"
            onClick={handleUpload}
            disabled={uploading}
            sx={{
              mt: 1,
              borderRadius: '12px',
              bgcolor: '#0052FF',
              '&:hover': {
                bgcolor: '#0043CC'
              }
            }}
          >
            {uploading ? 'Uploading...' : 'Start Learning'}
          </Button>
        </Box>
      )}
      
      {uploading && <LinearProgress sx={{ mt: 2 }} />}
    </Box>
  );
};