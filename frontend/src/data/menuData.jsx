import {
  Bot,
  Database,
  Library,
  Monitor,
  Layers,
  Zap,
  Briefcase,
  PlaySquare,
  Lock,
  KeySquare,
  Users,
  Link as LinkIcon,
  Box,
} from "lucide-react";

export const menuSections = [
  {
    title: "MY PROJECTS",
    items: [
      {
        name: "Agents",
        icon: <Bot size={16} strokeWidth={2.5} />,
        path: "/agents",
      },
      {
        name: "AI Models",
        icon: <Database size={16} strokeWidth={2.5} />,
        path: "/ai-models",
      },
      {
        name: "Library",
        icon: <Library size={16} strokeWidth={2.5} />,
        path: "/library",
      },
    ],
  },
  {
    title: "ORCHESTRATOR",
    items: [
      {
        name: "Published",
        icon: <Box size={16} strokeWidth={2.5} />,
        path: "/published",
      },
      {
        name: "Machines",
        icon: <Monitor size={16} strokeWidth={2.5} />,
        path: "/machines",
      },
      {
        name: "Queues",
        icon: <Layers size={16} strokeWidth={2.5} />,
        path: "/queues",
      },
      {
        name: "Triggers",
        icon: <Zap size={16} strokeWidth={2.5} />,
        path: "/triggers",
      },
      {
        name: "Jobs",
        icon: <Briefcase size={16} strokeWidth={2.5} />,
        path: "/jobs",
      },
      {
        name: "Executions",
        icon: <PlaySquare size={16} strokeWidth={2.5} />,
        path: "/executions",
      },
      {
        name: "Vault",
        icon: <Lock size={16} strokeWidth={2.5} />,
        path: "/vault",
      },
      {
        name: "Knowledge Base",
        icon: <Database size={16} strokeWidth={2.5} />,
        path: "/knowledge-base",
      },
      {
        name: "Key Store",
        icon: <KeySquare size={16} strokeWidth={2.5} />,
        path: "/key-store",
      },
    ],
  },
  {
    title: "ADMIN",
    items: [
      {
        name: "Tenant",
        icon: <Users size={16} strokeWidth={2.5} />,
        path: "/tenant",
      },
      {
        name: "Integrations",
        icon: <LinkIcon size={16} strokeWidth={2.5} />,
        path: "/integrations",
      },
    ],
  },
];
