import { Plus } from "lucide-react";
import Button from "../ui/Button";
import SearchBox from "../ui/SearchBox";

const KnowledgeBaseHeader = ({ onCreateClick }) => {
  return (
    <div className="flex items-center justify-between pb-6 pt-4 border-b border-gray-100/0 bg-transparent mb-4">
      <h1 className="text-[20px] font-bold text-gray-800 tracking-tight">
        Knowledge Base
      </h1>

      <div className="flex items-center gap-4">
        {/* Knowledge Base Search */}
        <SearchBox
          placeholder="Search..."
          inputClass="w-[320px] bg-white border border-gray-200 text-gray-800 shadow-sm py-2 rounded-full"
        />

        {/* Create Button */}
        <Button
          onClick={onCreateClick}
          variant="primary"
          icon={<Plus className="w-4 h-4" />}
        >
          Create New
        </Button>
      </div>
    </div>
  );
};

export default KnowledgeBaseHeader;
