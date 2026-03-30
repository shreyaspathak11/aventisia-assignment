import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import MainLayout from './components/layout/MainLayout';
import KnowledgeBasePage from './pages/KnowledgeBasePage';

// Simple placeholder page for router demonstration
const PlaceholderPage = ({ title }) => (
  <div className="flex flex-col items-center justify-center h-[500px] text-gray-400">
    <h1 className="text-2xl font-bold">{title} Page</h1>
    <p>This page is ready to be implemented.</p>
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          {/* Default redirect to Knowledge Base */}
          <Route index element={<Navigate to="/knowledge-base" replace />} />
          
          {/* Scalable modular routes */}
          <Route path="agents" element={<PlaceholderPage title="Agents" />} />
          <Route path="ai-models" element={<PlaceholderPage title="AI Models" />} />
          <Route path="knowledge-base" element={<KnowledgeBasePage />} />
          
          {/* Catch-all */}
          <Route path="*" element={<PlaceholderPage title="404 - Not Found" />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
