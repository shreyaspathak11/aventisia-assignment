import { useState } from "react";
import KnowledgeBaseHeader from "../components/knowledge-base/KnowledgeBaseHeader";
import KnowledgeBaseGrid from "../components/knowledge-base/KnowledgeBaseGrid";
import Pagination from "../components/knowledge-base/Pagination";
import CreateKnowledgeBaseDrawer from "../components/knowledge-base/CreateKnowledgeBaseDrawer";
import { Database } from "lucide-react";

const KnowledgeBasePage = () => {
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);
  const [knowledgeBases, setKnowledgeBases] = useState([]);

  const handleCreate = (newData) => {
    const newItem = {
      ...newData,
      id: Date.now().toString(),
      createdOn: new Date().toLocaleDateString("en-GB", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
      }),
    };
    setKnowledgeBases([...knowledgeBases, newItem]);
    setIsDrawerOpen(false);
  };

  const handleDelete = (id) => {
    setKnowledgeBases((prev) => prev.filter((item) => item.id !== id));
  };

  return (
    <div className="flex flex-col h-full relative p-2">
      <KnowledgeBaseHeader onCreateClick={() => setIsDrawerOpen(true)} />

      <div className="flex-1 mt-4">
        {knowledgeBases.length > 0 ? (
          <div className="flex flex-col h-full justify-between pb-8">
            <KnowledgeBaseGrid items={knowledgeBases} onDelete={handleDelete} />
            <div className="mt-12 pt-6 border-t border-gray-200/60 flex justify-end">
              <Pagination totalRows={knowledgeBases.length} />
            </div>
          </div>
        ) : (
          <div className="flex flex-col items-center justify-center h-full min-h-[500px] text-gray-400">
            <div className="p-8 bg-gray-100 rounded-full mb-6">
              <Database className="w-20 h-20 text-gray-300" strokeWidth={1.5} />
            </div>
            <p className="text-xl font-semibold text-gray-500 tracking-tight">
              No Knowledge Bases Found
            </p>
            <p className="text-[15px] mt-2 font-medium">
              Click "Create New" to add your first knowledge base.
            </p>
          </div>
        )}
      </div>

      {isDrawerOpen && (
        <div
          className="fixed inset-0 bg-[#0F172A]/40 z-[90] backdrop-blur-[2px] transition-all"
          onClick={() => setIsDrawerOpen(false)}
        ></div>
      )}

      <CreateKnowledgeBaseDrawer
        isOpen={isDrawerOpen}
        onClose={() => setIsDrawerOpen(false)}
        onCreate={handleCreate}
      />
    </div>
  );
};

export default KnowledgeBasePage;
