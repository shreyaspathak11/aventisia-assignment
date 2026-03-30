# Knowledge Base UI Documentation - React Frontend

This repository contains the front-end implementation for the "Knowledge Base" UI assignment. The project accurately replicates the provided Figma designs, implementing a responsive, scalable, and modular component architecture.

## Features & Implementation Specifics
- **Pixel-Accurate UI**: Developed to adhere rigorously to the padding, spacing, and typography scales seen in the Figma designs.
- **Strict Color Palette**: Accurately utilizes requested brand tokens natively injected into Tailwind (`Primary #4F46E5`, `Secondary #1E1B4B`).
- **Scalable Architecture**: Configured with `react-router-dom` using a `MainLayout` wrap (`react-router` Outlet pattern) to comfortably support additional multipage views (i.e., /agents, /models).
- **Modular Components**: Engineered custom primitive implementations for `Button`, `SearchBox`, and `Avatar` controls emphasizing reusability without code duplication.
- **Dynamic State Management**: 
    - Handles "Empty states" intuitively. 
    - Employs a fully functioning Right-hand Drawer slide-in mechanism activated via `+ Create New`.
    - Features a 3-dots Context Menu allowing users to natively `Remove` injected cards using simulated local React state.
- **Premium Interactivity**: Formulated with modern web standards incorporating transition speeds, hover micro-animations, and clean blurred overlays (`backdrop-blur`).

## Tech Stack Guidelines Met
- **Framework**: React (using the latest stable Functional Components + Hooks context)
- **Tooling**: Vite (ensuring lightning-fast HMR compilation steps)
- **Styling**: Tailwind CSS (Leveraging utility classes over arbitrary CSS drops)
- **Icons**: Lucide-React (Mirroring the design's standard crisp iconography footprint)

## Setup & Getting Started

### Prerequisites
Make sure your environment has **Node.js** (v18+) and **npm** ready.

### Installation
1. If you aren't already there, open a terminal window inside the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install the necessary development dependencies:
   ```bash
   npm install
   ```

3. Spin up the Vite development server:
   ```bash
   npm run dev
   ```

4. View the frontend locally by navigating to the prompt. Commonly: `http://localhost:5173`.
