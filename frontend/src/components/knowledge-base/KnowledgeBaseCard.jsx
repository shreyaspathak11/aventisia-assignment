import { useState, useRef, useEffect } from "react";
import { MoreVertical, Trash2 } from "lucide-react";
import Button from "../ui/Button";

const KnowledgeBaseCard = ({ item, onDelete }) => {
  const [showMenu, setShowMenu] = useState(false);
  const menuRef = useRef(null);

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setShowMenu(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className="bg-white rounded-[16px] border border-gray-200 p-6 flex flex-col h-[240px] hover:shadow-lg transition-all shadow-sm group">
      {/* Header */}
      <div className="flex justify-between items-start mb-5">
        <h3 className="text-[16px] font-bold text-gray-900 tracking-tight line-clamp-1">
          {item.name || "Test"}
        </h3>
        <div className="relative" ref={menuRef}>
          <Button
            variant="ghost"
            onClick={() => setShowMenu(!showMenu)}
            className="p-1 -mr-2 text-gray-400 hover:text-gray-900 transition-colors"
            icon={<MoreVertical size={20} />}
          />
          {showMenu && (
            <div className="absolute right-0 top-full mt-1 w-32 bg-white rounded-md shadow-lg border border-gray-100 py-1 z-10">
              <button
                onClick={() => {
                  setShowMenu(false);
                  onDelete();
                }}
                className="w-full text-left px-4 py-2 text-[13px] text-red-600 hover:bg-red-50 flex items-center gap-2"
              >
                <Trash2 size={14} /> Remove
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Body */}
      <div className="flex-1 text-[13px] text-gray-500 line-clamp-4 leading-relaxed overflow-hidden pr-2 font-medium">
        {item.description ||
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."}
      </div>

      {/* Footer */}
      <div className="pt-4 mt-auto border-t border-gray-100/50 flex items-center text-[12px] text-gray-400 font-semibold tracking-wide">
        <span>Created On: {item.createdOn}</span>
      </div>
    </div>
  );
};

export default KnowledgeBaseCard;
