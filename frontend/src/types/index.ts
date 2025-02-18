// src/types/index.ts
export interface Message {
    role: 'user' | 'assistant';
    content: string;
  }
  
  export interface ChatResponse {
    answer: string;
    formatted_answer: string;
    sources: Source[];
  }
  
  export interface Source {
    content: string;
    metadata?: Record<string, any>;
  }