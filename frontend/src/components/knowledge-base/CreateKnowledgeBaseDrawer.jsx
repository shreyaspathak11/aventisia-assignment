import { X, ChevronDown } from "lucide-react";
import Button from "../ui/Button";
import { useKnowledgeBaseForm } from "../../hooks/useKnowledgeBaseForm";

const CreateKnowledgeBaseDrawer = ({ isOpen, onClose, onCreate }) => {
  const { form, onSubmit } = useKnowledgeBaseForm({ isOpen, onCreate });

  const {
    register,
    formState: { errors, isValid },
  } = form;

  return (
    <div
      className={`fixed top-0 right-0 h-full w-[480px] bg-white border-l border-gray-100 z-[100] transform transition-transform duration-300 ease-in-out flex flex-col ${
        isOpen ? "translate-x-0" : "translate-x-full"
      }`}
    >
      {/* Header */}
      <div className="px-8 flex justify-between items-start pt-8 pb-4">
        <div>
          <h2 className="text-xl font-bold text-gray-900 tracking-tight">
            Create New Knowledge Base
          </h2>
          <p className="text-[14px] text-gray-500 mt-1.5 font-medium">
            Best for quick answers from documents, websites and text files.
          </p>
        </div>
        <Button
          variant="ghost"
          onClick={onClose}
          icon={<X size={24} strokeWidth={2} />}
          className="text-gray-400 hover:text-gray-800 -mr-2 -mt-2"
        />
      </div>

      <div className="border-b border-gray-100/60 w-full mb-1"></div>

      {/* Form Body */}
      <div className="flex-1 overflow-y-auto px-8 pt-4 pb-8">
        <form id="create-kb-form" onSubmit={onSubmit} className="space-y-7">
          {/* Name Field */}
          <div>
            <label className="block text-[12px] font-semibold text-gray-700 mb-1.5 mt-1">
              Name (Cannot be edited later)
              <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              {...register("name")}
              placeholder="Name"
              className={`w-full border rounded-[6px] px-3 py-2 text-[13px] focus:outline-none focus:ring-[2px] transition-colors placeholder-gray-400 shadow-sm ${
                errors.name
                  ? "border-red-500 focus:ring-red-500/20 focus:border-red-500"
                  : "border-gray-300 focus:ring-primary/20 focus:border-primary"
              }`}
            />
            {errors.name && (
              <p className="text-red-500 text-[11px] font-medium mt-1.5">
                {errors.name.message}
              </p>
            )}
          </div>

          {/* Description Field */}
          <div>
            <label className="block text-[12px] font-semibold text-gray-700 mb-1.5">
              Description
            </label>
            <textarea
              rows={4}
              {...register("description")}
              placeholder="Description"
              className="w-full border border-gray-300 rounded-[6px] px-3 py-2 text-[13px] focus:outline-none focus:ring-[2px] focus:ring-primary/20 focus:border-primary transition-colors placeholder-gray-400 shadow-sm resize-none"
            />
          </div>

          {/* Vector Store */}
          <div>
            <label className="block text-[12px] font-semibold text-gray-700 mb-1.5">
              Vector Store<span className="text-red-500">*</span>
            </label>
            <div className="relative">
              <select
                {...register("vectorStore")}
                className="w-full appearance-none border border-gray-300 rounded-[6px] px-3 py-2 text-[13px] focus:outline-none focus:ring-[2px] focus:ring-primary/20 focus:border-primary bg-white transition-colors cursor-pointer shadow-sm"
              >
                <option value="Qdrant">Qdrant</option>
                <option value="Pinecone">Pinecone</option>
                <option value="Chroma">Chroma</option>
              </select>
              <ChevronDown className="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500 pointer-events-none" />
            </div>
          </div>

          {/* Setup LLM Model */}
          <div>
            <label className="block text-[12px] font-semibold text-gray-700 mb-1.5">
              LLM Embedding Model<span className="text-red-500">*</span>
            </label>
            <div className="relative">
              <select
                {...register("embeddingModel")}
                className="w-full appearance-none border border-gray-300 rounded-[6px] px-3 py-2 text-[13px] focus:outline-none focus:ring-[2px] focus:ring-primary/20 focus:border-primary bg-white transition-colors cursor-pointer shadow-sm truncate pr-10"
              >
                <option value="text-embedding-ada-002">
                  text-embedding-ada-002
                </option>
                <option value="text-embedding-3-small">
                  text-embedding-3-small
                </option>
                <option value="text-embedding-3-large">
                  text-embedding-3-large
                </option>
              </select>
              <ChevronDown className="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500 pointer-events-none" />
            </div>
          </div>
        </form>
      </div>

      {/* Footer */}
      <div className="px-8 py-6 mb-2 flex justify-end bg-white">
        <Button
          form="create-kb-form"
          type="submit"
          variant="primary"
          className="px-6 py-2 text-[13px] rounded-[6px]"
          disabled={!isValid}
        >
          Create
        </Button>
      </div>
    </div>
  );
};

export default CreateKnowledgeBaseDrawer;
