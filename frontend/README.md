# GitHub Cloud Connector Frontend

A responsive React-based user interface developed with Tailwind CSS and the Lucide icon set. It serves as a comprehensive dashboard for managing GitHub repository metadata and user-level GitHub data.

---

## Design System and Typography

The frontend adheres to a professional design system focusing on:
1.  **Vibrant Dark Theme**: A sophisticated color palette utilizing custom HSL values for readability and visual depth.
2.  **Layered Visual Hierarchy**: Semi-transparent, blur-heavy containers for structured layouts.
3.  **Refined Typography**: Utilizing the `Inter` and `Outfit` font families from Google Fonts for clear hierarchy in repository lists and issue data.
4.  **Micro-interactions**: Subtle CSS-based transitions and hover states for improved user feedback.

---

## Component Architecture

The frontend is modularized into discrete functional components for reusability and testing:

### Layout Components
*   **Sidebar**: A collapsible navigation interface for dashboard-level actions.
*   **TopBar**: Dynamic breadcrumbs and user authentication status display.
*   **DashboardLayout**: A higher-order component (HOC) used to maintain structural consistency across pages.

### Dashboard and Data Components
*   **KnowledgeBasePage**: The primary state management container and page view.
*   **KnowledgeBaseGrid**: Grid-based display logic for listing multiple repository cards.
*   **KnowledgeBaseCard**: A feature-rich data card displaying repository status and metadata.
*   **SearchBox**: Real-time client-side filtering and search query management.
*   **Pagination**: Modular control for handling large data sets with smooth list navigation.

---

## State and Data Management

*   **React State Hooks**: Utilizes `useState` and `useEffect` for local component lifecycle management.
*   **Modular Formatting**: Custom hooks (`useKnowledgeBaseForm`) isolate business and validation logic from pure UI components.
*   **Ready for Integration**: Current implementation uses a high-fidelity mock state, designed for direct backend connection via standardized API calls.

---

## Development Environment Setup

1.  **Package Installation**: `npm install`.
2.  **Launch Development Server**: `npm run dev`.
3.  **Build production-ready bundle**: `npm run build`.

---

## Project Dependencies

*   **Logic**: React 18
*   **Styling**: Tailwind CSS
*   **Visual Assets**: Lucide React
*   **Navigation**: React Router DOM

---

A premium interface for efficient GitHub management.
