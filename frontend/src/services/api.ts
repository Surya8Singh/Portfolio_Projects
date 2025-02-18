// import axios from 'axios';
// import { ChatResponse } from '../types';

// const API_BASE_URL = 'http://localhost:8000';

// export const api = {
//   createSession: async () => {
//     const response = await axios.post(`${API_BASE_URL}/session`);
//     return response.data.session_id;
//   },

//   sendMessage: async (question: string, sessionId: string): Promise<ChatResponse> => {
//     const response = await axios.post(`${API_BASE_URL}/query`, {
//       question,
//       session_id: sessionId
//     });
//     return response.data;
//   }
// };

import axios from 'axios';
import { ChatResponse } from '../types';

const API_BASE_URL = 'http://localhost:8000';

export const api = {
  createSession: async () => {
    const response = await axios.post(`${API_BASE_URL}/session`);
    return response.data.session_id;
  },

  sendMessage: async (question: string, sessionId: string): Promise<ChatResponse> => {
    const response = await axios.post(`${API_BASE_URL}/query`, {
      question,
      session_id: sessionId
    });
    return response.data;
  },

  // Add the new uploadDocuments method
  uploadDocuments: async (files: File[]) => {
    const formData = new FormData();
    files.forEach(file => {
      formData.append('files', file);
    });

    await axios.post(`${API_BASE_URL}/upload`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
  }
};

// Add TypeScript type definitions for the API object
export type ApiClient = typeof api;