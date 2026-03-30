import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";

// Define the validation schema using Zod outside the hook
const schema = z.object({
  name: z.string().min(1, { message: "Name is required" }),
  description: z.string().optional(),
  vectorStore: z.string(),
  embeddingModel: z.string(),
});

export const useKnowledgeBaseForm = ({ isOpen, onCreate }) => {
  const form = useForm({
    resolver: zodResolver(schema),
    defaultValues: {
      name: "",
      description: "",
      vectorStore: "Qdrant",
      embeddingModel: "text-embedding-ada-002",
    },
    mode: "onChange", // Enables live validation for the submit button disabled state
  });

  const { reset, handleSubmit } = form;

  const onSubmit = (data) => {
    onCreate(data);
    reset(); // Reset form smoothly via react-hook-form
  };

  // Reset form when drawer is closed without generic submission
  useEffect(() => {
    if (!isOpen) {
      reset();
    }
  }, [isOpen, reset]);

  return {
    form,
    onSubmit: handleSubmit(onSubmit),
  };
};
